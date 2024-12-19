import pandas as pd
from pymongo import MongoClient

# Path to your CSV file
csv_path = 'D:/Users/Ashka/PycharmProjects/realestae/yad4.csv'  # <-- Replace with your actual CSV file path

# Load CSV data
data = pd.read_csv(csv_path)

# Define the field mapping
field_mapping = {
    "item-layout_itemLink__CZZ7w href": "url",
    "item-image_img__ki7ke src": "image",
    "price_price__xQt90": "price",
    "item-data-content_heading__tphH4": "address",
    "item-data-content_itemInfoLine__AeoPP": "property_type",
    "item-data-content_itemInfoLine__AeoPP 2": "details",
    "tooltip_tooltip__w2sbB": "saved",
    "item-tags_itemTagsBox__Uz23E": "feature_1",
    "item-tags_itemTagsBox__Uz23E 2": "feature_2",
    "item-tags_itemTagsBox__Uz23E 3": "feature_3",
    "gradient-bg-caption_gradientBgCaption__dsYoN":"real estate agency"
}

# Rename columns based on mapping
data = data.rename(columns=field_mapping)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["real_estate"]
properties_collection = db["properties"]

# Convert DataFrame to dictionary format for MongoDB
properties = data.to_dict(orient='records')

# Insert or update documents in MongoDB
for property in properties:
    query = {"url": property["url"]}
    properties_collection.update_one(query, {"$set": property}, upsert=True)

print("Data imported and updated successfully in MongoDB!")
