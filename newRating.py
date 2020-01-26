import pymongo
from pymongo import MongoClient

def newRating(id, rating):
    cluster = MongoClient("mongodb+srv://tUser:sUqOIWMnEz5a8sqn@tutorfy-ednqp.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster['Tutorfy']
    collection = db['Tutorfy']
    tutor = collection.find_one({"_id":id})
    updatedRating = (tutor['rating']*tutor['numberOfRatings'] + rating)/(tutor['numberOfRatings'] + 1)
    collection.update_one({"_id":id}, {"$set": {"rating":updatedRating, "numberOfRatings": tutor['numberOfRatings']+1}})

    return "updated"
