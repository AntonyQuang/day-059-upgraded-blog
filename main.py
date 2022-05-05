from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)
blog_api = "https://api.npoint.io/a7fc2b78ff4a828460da"
response = requests.get("https://api.npoint.io/a7fc2b78ff4a828460da")
blog_posts = response.json()

@app.route('/')
def get_all_posts():
    print(blog_posts)
    return render_template("index.html", posts=blog_posts)


@app.route('/contact')
def contact():
    return render_template("contact.html")


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