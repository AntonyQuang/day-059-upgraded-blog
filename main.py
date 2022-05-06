from flask import Flask, render_template, request
import requests
import smtplib
from config import senders_email, senders_password, recipients_email

app = Flask(__name__)
blog_api = "https://api.npoint.io/a7fc2b78ff4a828460da"
response = requests.get("https://api.npoint.io/a7fc2b78ff4a828460da")
blog_posts = response.json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=blog_posts)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        entry = request.form
        name = entry["name"]
        email = entry["email"]
        phone = entry["phone"]
        message = entry["message"]
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=senders_email, password=senders_password)
            connection.sendmail(from_addr=senders_email, to_addrs=recipients_email, msg=f"Subject:New Message from your blog!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<blog_id>')
def post(blog_id):
    for blog_post in blog_posts:
        if blog_post["id"] == int(blog_id):
            requested_post = blog_post
            return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)