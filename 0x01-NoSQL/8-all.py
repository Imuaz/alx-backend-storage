#!/usr/bin/env python3
'''
MongoDB module
'''

def list_all(mongo_collection):
    '''List all documents in a collection'''
    return mongo_collection.find()
