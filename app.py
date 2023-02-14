'''
Created on 04-Sep-2019

@author: bkadambi
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask  # From module flask import class Flask
from pymongo import MongoClient
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

# url = f"mongodb://myuser:mypassword@my-mongodb.svc.cluster.local"
# 172.21.118.63
# url = f"mongodb://172.21.250.170"
url = f"mongodb://myuser:mypassword@172.21.250.170"
client = MongoClient(url)
print(f"connecting to url: {url}")

# print(client.tododb.list_collection_names())
for db in client.list_databases():
    print(db)

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return 'Hello, world!'

if __name__ == '__main__':  # Script executed directly?
    print("Hello, World. Uses S2I to build the application.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
