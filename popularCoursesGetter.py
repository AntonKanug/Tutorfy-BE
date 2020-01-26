
from pymongo import MongoClient
from flask import jsonify


def popularCoursesGetter():
    cluster = MongoClient("mongodb+srv://tUser:sUqOIWMnEz5a8sqn@tutorfy-ednqp.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster['Tutorfy']
    collection = db['Tutorfy']
    courses = (collection.find())

    allCourses = []

    for course in courses:
        allCourses.append((course["_id"], course["rating"], course["numberOfRatings"]))
    
    allCourses = sorted(allCourses, key=lambda course: course[2]*course[1])
    allCourses.reverse()    
    ids = []
    for i in range(6):
        ids.append(allCourses[i][0])

    return jsonify(list(collection.find({"_id": {"$in": ids}})))
