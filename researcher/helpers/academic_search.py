from bs4 import BeautifulSoup
from typing import List

from ..models.entities import Article
from ..models.exceptions import ArticleNotFound
 

import requests


def search_articles(query: str) -> List[Article]:
    query = query.replace(" ", "+")
    res = requests.get(f"https://search.scielo.org/?lang=en&from=0&q={query}")
    html = BeautifulSoup(res.text, "lxml")
    tags = [item.find_parent("a") for item in html.find_all("strong", class_="title")]

    if not tags:
        raise ArticleNotFound("Article not Found!")

    articles = list()

    for tag in tags:
        article = Article(link=tag.get("href"), title=tag.find("strong").text,)
        articles.append(article)

    return articles
