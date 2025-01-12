import json
from flask import Flask
from pymongo import MongoClient
from datetime import datetime
import uuid
app = Flask(__name__)
import os
from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv('MONGO_URL')
# Connect to MongoDB
client = MongoClient(mongo_url)
# client = MongoClient('mongodb://localhost:27017/')
db = client['GET_OUT']  # Replace 'your_database_name' with your actual database name
collection = db['restaurants']

def insert_restaurant_data(rest_data):
    pid = str(uuid.uuid4())
    collection.insert_one({"_id":pid,"restaurant_data":rest_data})

# @app.route('/restaurant_data')
# def get_restaurenat_data():
#    data_object = {}
#    data = []
#    no_cuisine = 0
#    with open("data.json",encoding='utf-8') as json_file:
#         json_data = json.load(json_file)
#         print(len(json_data['features']))
#         for feature in json_data['features']:
#             restaurant_object = {}
#             # print(feature['properties']['formatted'])
#             address = feature['properties']['formatted']
#             # print(feature['properties']['datasource']['raw'])
#             restaurant_data = feature['properties']['datasource']['raw']
#             restaurant_object['address'] = address
#             restaurant_object['restaurant_data'] = restaurant_data
#             if 'cuisine' in restaurant_data:
#                 cuisines = restaurant_data['cuisine'].split(';')
#                 restaurant_object['cuisine'] = cuisines
#             else:
#                 no_cuisine += 1
#                 continue
#             data.append(restaurant_object)
#    print(no_cuisine)
#    data_object["restaurant_data"] = data
#    # insert_restaurant_data(data)
#    return data_object
# if __name__=='__main__': 
#    app.run() 


all_cuisines = []
with open("data.json",encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    print(len(json_data['features']))
    for feature in json_data['features']:
        restaurant_object = {}
        # print(feature['properties']['formatted'])
        address = feature['properties']['formatted']
        # print(feature['properties']['datasource']['raw'])
        restaurant_data = feature['properties']['datasource']['raw']
        restaurant_object['address'] = address
        restaurant_object['restaurant_data'] = restaurant_data
        if 'cuisine' in restaurant_data:
            cuisines = restaurant_data['cuisine'].split(';')
            restaurant_object['cuisine'] = cuisines
            for cuisine in cuisines:
                if cuisine not in all_cuisines:
                    all_cuisines.append(cuisine)

print(all_cuisines)










