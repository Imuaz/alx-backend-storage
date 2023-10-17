#!/usr/bin/env python3
'''
MongoDB module
'''


def update_topics(mongo_collection, name, topics):
    '''changes all topics of a chool document based on the name'''
    return mongo_collection.update_many(name, topics)
