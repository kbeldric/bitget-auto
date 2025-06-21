from flask import Flask, request
from bitget import place_order
from utils import calculate_order_size
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    signal = data.get("signal")  # "buy" or "sell"
    symbol = "BGBUSDT"

    if signal in ["buy", "sell"]:
        size = calculate_order_size(symbol)
        response = place_order(symbol, signal, size)
        return {"status": "executed", "response": response}

    return {"status": "ignored"}

if __name__ == "__main__":
    app.run(debug=True)
