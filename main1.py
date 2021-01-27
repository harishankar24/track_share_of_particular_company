#Resource1-See share-market information here: https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/
#Resource2-https://www.alphavantage.co/
#Resource3-https://newsapi.org/

from confidential_data import stock_api_key,news_api_key
import requests

company_code = "KOSS"
company_name = "KOSS CORP"
stock_api = "https://www.alphavantage.co/query"
news_api = "https://newsapi.org/v2/everything"

stock_api_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": company_code,
    "apikey": stock_api_key
}
response = requests.get(url = stock_api, params = stock_api_parameter)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]

yesterday_closing_price = float(data_list[0]["4. close"])
day_before_yesterday_closing_price = float(data_list[1]["4. close"])
difference = (yesterday_closing_price - day_before_yesterday_closing_price)
difference_in_percent = round((difference * 100)/day_before_yesterday_closing_price,2)
if(difference_in_percent >= 0):
    symbol = "🔺"
else:
    symbol = "🔻"
print(f"Share price: {symbol} {abs(difference_in_percent)}%")

if (difference_in_percent > 5):    
    news_api_parameter = {
        "q":company_name,
        "language": "en",
        "pageSize": 4,
        "apiKey": news_api_key
    }
    top_news = []
    response = requests.get(url = news_api, params = news_api_parameter)
    response.raise_for_status()
    data = response.json()
    for _ in range(news_api_parameter["pageSize"]):
        new_dict = dict()
        new_dict["title"] = data["articles"][_]["title"]
        new_dict["description"] = data["articles"][_]["description"]
        top_news.append(new_dict)
    for each_news in top_news:
        print(f"Title: {each_news['title']}")
        print(f"Description: {each_news['description']}")
        print()
    