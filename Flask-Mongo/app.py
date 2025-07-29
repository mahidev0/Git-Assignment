from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Replace with your MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["form_database"]
collection = db["user_data"]

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        try:
            if not name or not email:
                raise ValueError("Name and email are required.")
            collection.insert_one({'name': name, 'email': email})
            return redirect(url_for('success'))
        except Exception as e:
            error = str(e)
    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
