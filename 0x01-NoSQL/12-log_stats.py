#!/usr/bin/env python3
''' module for task 12 '''
import os
from pymongo import MongoClient


def connect_to_mongodb():
    connection_string = os.getenv('MONGODB_CONNECTION_STRING')
    if connection_string is None:
        raise ValueError("MONGODB_CONNECTION_STRING environment variable not set")
    
    client = MongoClient(connection_string)
    return client.logs.nginx

def get_unique_http_methods(collection):
    return collection.distinct('method')

def count_documents_with_method(collection, method):
    return collection.count_documents({'method': method})

def main():
    ''' script that provides some stats about Nginx logs '''
    collection = connect_to_mongodb()
    
    method_list = get_unique_http_methods(collection)

    print("{} logs\nMethods:".format(collection.estimated_document_count()))

    for method in method_list:
        method_count = count_documents_with_method(collection, method)
        print("\tmethod {}: {}".format(method, method_count))

    status_check_count = collection.count_documents({'method': 'GET', 'path': "/status"})
    print("{} status check".format(status_check_count))

if __name__ == "__main__":
    main()

