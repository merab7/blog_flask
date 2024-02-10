from flask import Flask, render_template, request
import requests
from datetime import datetime
import smtplib
import os

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


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        my_email =  os.environ.get("MY_EMAIL")
        password = os.environ.get("EMAIL_PASSWORD")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs="merabtodua7@gmail.com", 
                                msg=f"message from blog site\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
   



@app.route('/post/<int:num>')
def get_post(num):
    return render_template("post.html", posts=posts, index=num, date=current_date)



if __name__ == "__main__":
    app.run(debug=True)