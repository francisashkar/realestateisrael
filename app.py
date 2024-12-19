from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import math
import pickle  # Import if you use a saved model for predictions

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['real_estate']
properties_collection = db['properties']


# Uncomment the following if you have a pre-trained model to load
# with open('price_prediction_model.pkl', 'rb') as f:
#     model = pickle.load(f)

@app.route('/')
def index():
    # Get the current page from the URL (default to 1)
    page = int(request.args.get('page', 1))
    per_page = 10
    total_properties = properties_collection.count_documents({})
    total_pages = math.ceil(total_properties / per_page)

    # Calculate the offset and limit for pagination
    offset = (page - 1) * per_page
    properties = list(properties_collection.find().skip(offset).limit(per_page))

    # Pass page, total_pages, and properties to the template
    return render_template('index.html', properties=properties, page=page, total_pages=total_pages)


# Optional route for predicting property prices over time
@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.get_json()
    current_price = data.get('current_price')
    years = data.get('years')

    if current_price is None or years is None:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        # Example prediction: assume 5% annual growth
        predicted_price = current_price * (1.05 ** years)
        return jsonify({'predicted_price': round(predicted_price, 2)})
    except Exception as e:
        print("Prediction Error:", e)
        return jsonify({'error': 'Prediction failed'}), 500


if __name__ == '__main__':
    app.run(debug=True)
