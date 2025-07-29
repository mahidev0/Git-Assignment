from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():

    return 'This is my flask application, I am successfully Login'
if __name__ == '__main__':

    app.run(debug=True)