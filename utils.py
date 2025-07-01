import requests

def get_live_price(symbol="BGBUSDT"):
    """
    Ambil harga terbaru dari Bitget market API
    """
    url = f"https://api.bitget.com/api/v2/spot/market/ticker?symbol={symbol}"
    try:
        response = requests.get(url)
        data = response.json()
        return float(data["data"]["close"])
    except Exception as e:
        print(f"❌ Gagal ambil harga market: {e}")
        return 0.01  # fallback jika gagal
def calculate_order_size(symbol):
    usdt_balance = 10
    used_percent = 0.75
    price = get_live_price(symbol)
    if price <= 0:
        raise ValueError("Harga tidak valid")
    qty = (usdt_balance * used_percent) / price
    return round(qty, 4)
print(f"💰 Harga live {symbol}: {price} USDT — Order Size: {qty}")
