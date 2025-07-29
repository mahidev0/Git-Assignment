from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["todoDB"]
collection = db["items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({"error": "Both fields are required"}), 400

    item = {
        "name": item_name,
        "description": item_description
    }

    collection.insert_one(item)
    return jsonify({"message": "Item saved successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():

    return 'This is my flask application, I am successfully Login'
if __name__ == '__main__':

    app.run(debug=True)
