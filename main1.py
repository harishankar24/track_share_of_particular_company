from confidential_data import stock_api_key
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": stock_api_key
}
response = requests.get(url = STOCK_ENDPOINT, params = stock_api_parameter)
response.raise_for_status()
data = response.json()
value1 = float(data["Time Series (Daily)"]["2021-01-25"]["4. close"])
value2 = float(data["Time Series (Daily)"]["2021-01-22"]["4. close"])
diff = abs(value1 - value2)
diff_in_percent = int((diff * 100)/value2)
print(diff_in_percent)