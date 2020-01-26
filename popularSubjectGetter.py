import json

import pymongo
from flask import jsonify
from pymongo import MongoClient

def popularSubjectGetter():
    cluster = MongoClient("mongodb+srv://tUser:sUqOIWMnEz5a8sqn@tutorfy-ednqp.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster['Tutorfy']
    collection = db['Tutorfy']
    subCount = []
    subjectList = [ "Math", 
                "Biology",
                "Chemistry",
                "Physics",
                "Business",
                "Engineering",
                "Computer Science",
                "Art"] 
                
    for i in subjectList:
        subject = collection.find({"subject": i})
        count = 0
        for j in subject:
            count = count + 1
        subtup = (i, count)
        subCount.append(subtup)

    sortSubs = sorted(subCount, key=lambda tup: tup[1])
    sortSubs.reverse()

    reslist = []
    for i in sortSubs:
        reslist.append({"course" : i[0], "count" : i[1]})

    return jsonify(reslist)
