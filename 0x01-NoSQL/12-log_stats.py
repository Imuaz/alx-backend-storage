#!/usr/bin/env python3
"""MongoDB Module"""
from pymongo import MongoClient

if __name__ == "__main__":
    """function module"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    
    method_names = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}

    for method in method_names:
        method_counts[method] = nginx_collection.count_documents({"method": method})

    status_check = nginx_collection.count_documents({"path": "/status"})

    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")
    
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    
    print(f"{status_check} status check")
