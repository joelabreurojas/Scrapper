from typing import List

from ..models.entities import Article
from ..helpers.academic_search import search_articles


def search(query: str) -> List[Article]:
    return search_articles(query)
