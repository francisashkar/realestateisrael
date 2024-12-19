# Real Estate Property Listing Platform

A modern, responsive web application for displaying and managing real estate property listings with price prediction capabilities. The platform features a beautiful UI, property filtering, and future price predictions based on historical data.

## Features

- 🏠 Responsive property card grid layout
- 💰 Price prediction functionality for future valuations
- 🔍 Advanced property search and filtering
- 📱 Mobile-friendly design
- 📊 Property details with iconic representations
- 📄 Pagination for large property sets
- 🎨 Modern gradient UI with smooth animations
- 🔮 Year-based price prediction selector
- 🌐 MongoDB integration for property data storage

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **Database**: MongoDB
- **Additional Libraries**: 
  - Font Awesome for icons
  - Google Fonts (Roboto)
  - Flask-PyMongo for MongoDB integration

## Prerequisites

Before running the application, ensure you have:
- Python 3.x installed
- MongoDB installed and running
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install required Python packages:
```bash
pip install flask pymongo
```

3. Set up MongoDB:
- Start MongoDB service
- Create a database named 'real_estate'
- Create a collection named 'properties'

## Configuration

1. MongoDB Connection:
   - Update the MongoDB connection string in `app.py` if needed:
```python
client = MongoClient('mongodb://localhost:27017/')
```

2. Customization:
   - Modify the price prediction algorithm in `app.py` as needed
   - Adjust the number of items per page in the pagination settings
   - Customize the styling in the CSS section of `index.html`

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Access the application:
```
http://localhost:5000
```

## Project Structure

```
├── app.py              # Main Flask application
├── templates/
│   ├── index.html     # Main property listing page
│   └── search.html    # Property search interface
├── static/
│   └── images/        # Property images (if any)
└── README.md          # This file
```

## Usage

### Property Listing
- Properties are displayed in a responsive grid
- Each property card shows:
  - Property image
  - Address
  - Price
  - Number of rooms
  - Floor number
  - Property size
  - View listing button
  - Price prediction selector

### Price Prediction
1. Select the number of years from the dropdown
2. The system will calculate and display the predicted price
3. Predictions are based on a 5% annual growth model (customizable)

### Search Functionality
- Search by location
- Filter by price range
- Filter by property type
- Search by specific features
- Results update dynamically

## Customization

### Styling
The application uses custom CSS with:
- Gradient backgrounds
- Card hover effects
- Responsive design
- Custom Google Fonts
- Font Awesome icons

### Prediction Model
To implement a custom prediction model:
1. Uncomment the model loading code in `app.py`
2. Add your trained model file
3. Update the prediction logic in the `/predict_price` route

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Font Awesome for the icon set
- Google Fonts for the Roboto font family
- MongoDB for the database solution
- Flask community for the web framework
