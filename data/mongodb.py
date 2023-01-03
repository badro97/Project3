import csv
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://project3:project3@cluster0.3rbuxoe.mongodb.net/?retryWrites=true&w=majority")
db = myclient["project3"]

csvPath = "/Users/badro97/Section3/sprint3/project/Project3/real_finish.csv"


jsonList = []
with open(csvPath, 'r', encoding='utf-8-sig') as file:
    csvReader = csv.DictReader(file)
    for rows in csvReader:
        jsonData = {}

        jsonData['title'] = rows['title'].strip()
        jsonData['category'] = rows['category'].strip()
        jsonData['sub_category'] = rows['sub_category'].strip()
        jsonData['price'] = rows['price'].strip()
            
        jsonList.append(jsonData)
    db.project3.insert_many(jsonList)