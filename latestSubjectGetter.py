import json

import pymongo
from flask import jsonify
from pymongo import MongoClient

def latestSubjectGetter():
    cluster = MongoClient("mongodb+srv://tUser:sUqOIWMnEz5a8sqn@tutorfy-ednqp.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster['Tutorfy']
    collection = db['Tutorfy']
    total = collection.count()

    idlist = [total,total-1,total-2]

    reslist = collection.find({ "_id": { "$in": idlist }})
 
    return jsonify(list(reslist))
