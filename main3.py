from confidential_data import news_api_key
import requests

COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_parameter = {
    "q":COMPANY_NAME,
    "language": "en",
    "pageSize": 3,
    "apiKey": news_api_key
}
top_3_news = []
response = requests.get(url = NEWS_ENDPOINT, params = news_api_parameter)
response.raise_for_status()
data = response.json()
for _ in range(3):
    new_dict = dict()
    new_dict["title"] = data["articles"][_]["title"]
    new_dict["description"] = data["articles"][_]["description"]
    top_3_news.append(new_dict)

for each_news in top_3_news:
    print(f"Title: {each_news['title']}")
    print(f"Description: {each_news['description']}")
    print()
    