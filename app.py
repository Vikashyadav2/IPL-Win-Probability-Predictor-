#import flask
from flask import Flask, render_template

#create app

app = Flask(__name__)

#routing 

@app.route('/')
def index_page():
    return render_template('index.html')

#call(run) the app 
if __name__ == "__main__":
    app.run(debug=True)