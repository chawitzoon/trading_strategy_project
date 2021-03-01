# trading_strategy_project

Start in March 2021
Objective:
- app_tradebot folder:
   - retrieve the data from API (via python-binance, and stream from websocket client) and push the order to market
   - interface to display buy and sell history, current holding assets,... (use flask or other frameworks)
- backtesting_algo (Algorithm part):
  - get_data: get the historical data (retrieved via python-binance)
  - backtesting logics by backtrader library wrapper any other method
    - manual logic: use indicator: MACD, RSI, ...
    - machine learning method: train by history
