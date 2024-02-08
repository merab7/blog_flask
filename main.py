from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()
posts = [x for x in data]


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)
@app.route('/post/<int:id>')
def get_post(id):
    return render_template("post.html", posts=posts, index=id)

if __name__ == "__main__":
    app.run(debug=True)
