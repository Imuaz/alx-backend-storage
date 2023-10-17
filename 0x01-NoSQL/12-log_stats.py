#!/usr/bin/env python3
'''
MongoDB Module
'''
from pymongo import MongoClient


def connect_to_mongodb(host='127.0.0.1', port=27017, database='logs', collection='nginx'):
    '''connects to the db'''
    client = MongoClient(f'mongodb://{host}:{port}')
    return client[database][collection]

def main():
    ''' script that provides some stats about Nginx logs '''
    lst = connect_to_mongodb()
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: lst.count_documents({'method': method}) for method in methods}
    
    print(f"{lst.estimated_document_count()} logs\nMethods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    
    status_check_count = lst.count_documents({'method': 'GET', 'path': "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    main()
