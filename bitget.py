import os
import requests

API_KEY = os.getenv("BITGET_API_KEY", "xxxxx")
API_SECRET = os.getenv("BITGET_API_SECRET", "xxxxx")
PASSPHRASE = os.getenv("BITGET_PASSPHRASE", "xxxxx")

def place_order(symbol, side, size):
    # Simulasi order (nanti diganti API Bitget)
    return {
        "symbol": symbol,
        "side": side,
        "size": size,
        "status": "mock order executed"
    }
