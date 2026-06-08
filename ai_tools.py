from dotenv import  load_dotenv
import os
import requests
from ddgs import DDGS
from  agents import function_tool
load_dotenv()

@function_tool
def web_search(query: str) -> str:
    """Search the web for current information using DuckDuckGo-style results."""
    results = DDGS().text(query, max_results=5)

    if not results:
        return "No search results found."

    formatted_results = []

    for result in results:
        title = result.get("title", "No title")
        href = result.get("href", "")
        body = result.get("body", "")

        formatted_results.append(
            f"Title: {title}\nURL: {href}\nSnippet: {body}"
        )

    return "\n\n".join(formatted_results)


@function_tool
def search_google_books(info: str) -> str:
    """Search Google Books for books related to a topic."""

    api_key=os.getenv("GOOGLEBOOKS_API_KEY")

    url = f"https://www.googleapis.com/books/v1/volumes?q={info}&printType=books&key={api_key}"

    response = requests.get(url)
    data = response.json()
    
    if "error" in data: 
        return "Could not find the information on this topic."
    
    title = data['title']
    author = data['author']
    publisher = data['publisher']
    publishedDate = data['publishedDate']
    description = data['description']
    pageCount = data['pageCount']
    averageRating = data['averageRating']

    return f"title: {title}, author:{author}, publisher: {publisher}, publisherDate: {publishedDate}, description: {description}, pageCount: {pageCount}, Ave Rating: {averageRating} "


