from flask import Flask, flash, redirect, render_template, request, session, abort, request
from random import randint
from pymongo import MongoClient
import json
import os

app = Flask(__name__)
mongo_uri=os.environ['MONGODB_URI']
client = MongoClient(mongo_uri)
db = client['quotes_db']


@app.route('/api/v1/get-quotes', methods=['GET'])
def get_quotes():
    quotes = db['quotes']
    cursor = quotes.find({},{"_id":0})
    response = list()
    for quote in cursor:
        response.append(quote)

    return json.dumps({"response": response}), 200, {'ContentType':'application/json'}

@app.route('/api/v1/add-quote', methods=['POST'])
def add_quote():
    quote = request.get_json()
    try:
        response = db['quotes'].insert_one(quote)
    except Exception as e:
        return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

# This API will run on port 3000 on host 0.0.0.0.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
