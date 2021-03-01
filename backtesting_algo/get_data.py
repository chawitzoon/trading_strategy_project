import sys, os

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(sys.path[0])),'package'))
import config
import csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()

# for price in prices:
#     print(price)

csvfile = open('data/data_1day_BTCUSDT.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

# candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2020", "12 Jul, 2020")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "12 Jul, 2020")
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "1 Mar, 2021")

for candlestick in  candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()
