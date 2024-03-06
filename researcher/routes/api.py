from flask import Blueprint, request, jsonify, redirect, url_for

from ..controller import article_controller


api_scope = Blueprint("api", __name__)


@api_scope.route("/<query>", methods=["GET"])
def get_articles(query):
    articles = article_controller.search(query)

    return jsonify(articles)
