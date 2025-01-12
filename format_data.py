import json
from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime
import uuid
app = Flask(__name__)
import os
from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv('MONGO_URL2')
# Connect to MongoDB
client = MongoClient(mongo_url)
# client = MongoClient('mongodb://localhost:27017/')
db = client['GET_OUT']  # Replace 'your_database_name' with your actual database name
collection = db['restaurants']

def insert_restaurant_data(rest_data):
    pid = str(uuid.uuid4())
    collection.insert_one({"_id":pid,"restaurant_data":rest_data})

# insert_restaurant_data("test")

@app.route('/restaurant_data')
def get_restaurenat_data():
   data_object = {}
   data = []
   no_cuisine = 0
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
            else:
                no_cuisine += 1
                continue
            data.append(restaurant_object)
   print(no_cuisine)
   data_object["restaurant_data"] = data
   insert_restaurant_data(data)
   return data_object
all_cuisines = []
European = ["german", "austrian", "bavarian", "alsatian", "french", "italian", "sicilian", "portuguese", "spanish", "greek", "Croatian", "Hungarian", "Belgian"]
asian = ["Thai", "Chinese", "Japanese" ,"sushi", "ramen", "Vietnamese", "Korean", "Indian", "Nepalese","Tibetan"]
middle_east = ["Turkish", "Arab","Levantine", "Lebanese", "Persian", "Ethiopian"]
Global = ["American","International","burger","barbecue","Pizza","sandwiches","Salad bowls","fish","Mexican","Brazilian","Argentinain","peruvian","Bistro","tapas"]

@app.route('/restaurant_data_cuisine')
def get_restaurenat_cuisine():
    data_object = {}
    data = []
    cuisine = request.args.get('cuisine')
    if cuisine == "Asian":
        data = list(collection.find())
        rest_data = data[0]['restaurant_data']
        c_data = []
        for re_data in rest_data:
            cuisine_array = re_data['cuisine']
            for asi in asian:
                if asi in cuisine_array:
                    c_data.append(re_data)
        data_object['rest_data'] = c_data
        return data_object
    elif cuisine == "European":
        data = list(collection.find())
        rest_data = data[0]['restaurant_data']
        c_data = []
        print(cuisine)
        for re_data in rest_data:
            cuisine_array = re_data['cuisine']
            print(cuisine_array)
            for asi in European:
                if asi.lower() in cuisine_array:
                    print(re_data)
                    c_data.append(re_data)
        data_object['rest_data'] = c_data
        return data_object

    if cuisine == "Global":
        data = list(collection.find())
        rest_data = data[0]['restaurant_data']
        c_data = []
        for re_data in rest_data:
            cuisine_array = re_data['cuisine']
            for asi in Global:
                if asi.lower() in cuisine_array:
                    c_data.append(re_data)
        data_object['rest_data'] = c_data
        return data_object

    if cuisine == "Middle_east":
        data = list(collection.find())
        rest_data = data[0]['restaurant_data']
        c_data = []
        for re_data in rest_data:
            cuisine_array = re_data['cuisine']
            for asi in middle_east:
                if asi.lower() in cuisine_array:
                    c_data.append(re_data)
        data_object['rest_data'] = c_data
        return data_object


if __name__=='__main__': 
   app.run() 




# all_cuisines = []
# European = ["German", "Austrian", "Bavarian", "Alsatian", "French", "Italian", "Sicilian", "Portuguese", "Spanish", "Greek", "Croatian", "Hungarian", "Belgian"]
# asian = ["Thai", "Chinese", "Japanese" ,"sushi", "ramen", "Vietnamese", "Korean", "Indian", "Nepalese","Tibetan"]
# middle_east = ["Turkish", "Arab","Levantine", "Lebanese", "Persian", "Ethiopian"]
# Global = ["American","International","burger","barbecue","Pizza","sandwiches","Salad bowls","fish","Mexican","Brazilian","Argentinain","peruvian","Bistro","tapas"]


# European: German, Austrian, Bavarian, Alsatian, French, Italian, Sicilian, Portuguese, Spanish, Greek, Croatian, Hungarian, Belgian.
# Asian: Thai, Chinese, Japanese (sushi, ramen), Vietnamese, Korean, Indian, Nepalese/Tibetan.
# Middle Eastern & African: Turkish, Arab/Levantine (Lebanese, Persian), Ethiopian.
# Global, Quick eats and Fusion: American (burger, barbecue),Pizza (Italian pizza), sandwiches,Salad bowls, fish, seafood Latin American (Mexican, Brazilian,Argentinian), Peruvian.Bistro, tapas.

test_data = [["American","ramen","French"],["Pizza","Persian","Spanish"]]
# for euro in European:
#     for test in test_data:
#         if euro in test:
#             print("yes") 
# res = [euro for euro in European if any(euro in test for test in test_data)]
# print(res)
       
result = [test for test in test_data if any(euro in test for euro in European)]

print(result)




# with open("data.json",encoding='utf-8') as json_file:
#     json_data = json.load(json_file)
#     print(len(json_data['features']))
#     for feature in json_data['features']:
#         restaurant_object = {}
#         # print(feature['properties']['formatted'])
#         address = feature['properties']['formatted']
#         # print(feature['properties']['datasource']['raw'])
#         restaurant_data = feature['properties']['datasource']['raw']
#         restaurant_object['address'] = address
#         restaurant_object['restaurant_data'] = restaurant_data
#         if 'cuisine' in restaurant_data:
#             cuisines = restaurant_data['cuisine'].split(';')
#             restaurant_object['cuisine'] = cuisines
#             for cuisine in cuisines:
#                 if cuisine not in all_cuisines:
#                     all_cuisines.append(cuisine)

# print(all_cuisines)










