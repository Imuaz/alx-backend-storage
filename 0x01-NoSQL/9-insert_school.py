#!/usr/bin/env python3
'''
MongoDB module
'''


def insert_school(mongo_collection, **kwargs):
    '''inserts a document in a collection based on kwargs'''
    return mongo_collection.insert_one(kwargs).inserted_id
