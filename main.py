from flask import Flask, render_template
import requests
from datetime import datetime

current_date = str(datetime.now().date())

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
data = response.json()
posts = [x for x in data]


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts, date=current_date)

@app.route('/about')
def get_about():

    return render_template('about.html')

@app.route('/contact')
def get_contact():
    
    return render_template('contact.html')


@app.route('/post/<int:num>')
def get_post(num):
    return render_template("post.html", posts=posts, index=num, date=current_date)

if __name__ == "__main__":
    app.run(debug=True)
