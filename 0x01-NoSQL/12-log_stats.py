#!/usr/bin/env python3
"""Script to provide stats about Nginx logs in MongoDB"""

from pymongo import MongoClient


def main():
    '''
    Connect to MongoDB and access the "logs" database and "nginx" collection'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.estimated_document_count()

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: nginx_collection.count_documents({'method': method}) for method in http_methods}

    status_check = nginx_collection.count_documents({'method': 'GET', 'path': '/status'}

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    main()
