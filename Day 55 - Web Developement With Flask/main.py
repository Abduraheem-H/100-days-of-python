from flask import Flask, render_template
import requests
from post import Post
import datetime as dt


app = Flask(__name__)


@app.route("/")
def home():
    current_year = dt.datetime.now().year
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts, year=current_year)


@app.route("/post/<int:post_id>")
def get_blog(post_id):
    post = Post(post_id)
    requested_post = post.get_post_by_id()
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
