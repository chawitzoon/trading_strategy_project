import multiprocessing

from flask import Flask, render_template
# from flask_socketio import SocketIO
# from SocketIO import Client
import websocket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# https://medium.com/@kendhia/run-python-webserver-flask-as-a-websocket-client-also-175c130f7ca4
# https://socket.io/get-started/private-messaging-part-1/
# https://pypi.org/project/websocket_client/

# if __name__ == '__main__':
  
@app.route('/')
def hello():
    return "Hello World!"

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

async def startws():
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@ticker",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    # ws.on_open = on_open
    ws.run_forever()

asyncio.get_event_loop().run_until_complete(startws)



# websocat -v wss://stream.binance.com:9443/ws/BTCUSDT@kline_1m