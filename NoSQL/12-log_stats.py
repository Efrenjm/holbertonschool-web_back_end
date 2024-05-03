#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Database: logs
        Collection: nginx
    """
    client = MongoClient()
    nginx_collection = client.logs.nginx

    logs_count = nginx_collection.count_documents({})
    print("{} logs".format(logs_count))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(
            method, nginx_collection.count_documents({"method": method})))

    print("{} status check".format(nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})))
    