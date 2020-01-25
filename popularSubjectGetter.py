import pymongo
from pymongo import MongoClient


def popularSubjectGetter():
    cluster = MongoClient("mongodb+srv://tUser:sUqOIWMnEz5a8sqn@tutorfy-ednqp.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster['Tutorfy']
    collection = db['Tutorfy']
    math = (collection.find({"subject": "Math"}))
    print(math)
    return math
