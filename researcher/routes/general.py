from flask import Blueprint, render_template, request
from ..controller import article_controller

general_scope = Blueprint("general", __name__)

@general_scope.route("/", methods=['GET', 'POST'])
def home():
    """Landing page route."""

    articles = []

    nav = [
        {"name": "API", "url": "/api/Ethical and social issues"},
    ]

    parameters = {
        "title": "Researcher",
        "description": "A simple page made for implement a basic academic search engine"
    }

    if request.method == "POST":
        query = request.form["query"]
        articles = article_controller.search(query)

    return render_template("home.html", articles=articles, nav=nav, **parameters)
