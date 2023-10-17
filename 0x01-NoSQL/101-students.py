#!/usr/bin/env python3
'''
MongoDB module
'''


def top_students(mongo_collection):
    ''' returns all students sorted by average score:'''
    return mongo_collection.aggregate([
    {
        "$addFields": {
            "averageScore": {"$avg": "$topics.score"}
        }
    },
    {"$sort": {"averageScore": -1}},
    {
        "$project": {
            "name": 1,
            "averageScore": 1,
            "_id": 0
        }
    }
])
