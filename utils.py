import requests

#def get_bgb_price(default_price=4):
def get_live_price(symbol="BGBUSDT"):
    """
    Ambil harga terakhir BGB/USDT dari Bitget Market API.
    """
    '''url = "https://api.bitget.com/api/v2/spot/market/tickers?symbol=BGBUSDT"
    params = {
        "symbol": "BGBUSDT"
    }'''
url = f"https://api.bitget.com/api/v2/spot/market/ticker?symbol={symbol}"
    try:
        response = requests.get(url)
        data = response.json()
        return float(data["data"]["close"])
    except Exception as e:
        print(f"❌ Gagal ambil harga market: {e}")
        return 0.01  # fallback jika gagal
    
    '''try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        price = float(data['data']['close'])
        return price
    except Exception as e:
        print(f"[WARN] Gagal mengambil harga dari API: {e}")
        print(f"[INFO] Menggunakan harga fallback: {default_price}")
        return default_price

def calculate_order_size(symbol="BGBUSDT"):
    """
    Hitung size order berdasarkan harga pasar dan saldo yang digunakan.
    """
    usdt_balance = 10
    used_percent = 0.75
    price = get_bgb_price()'''

def calculate_order_size(symbol):
    usdt_balance = 10
    used_percent = 0.75
    price = get_live_price(symbol)
    if price <= 0:
        raise ValueError("Harga tidak valid")
    qty = (usdt_balance * used_percent) / price
    return round(qty, 4)

    
    '''if price is None:
        print("Gagal mengambil harga. Tidak bisa menghitung order size.")
        return 0

    qty = (usdt_balance * used_percent) / price
    return round(qty, 2)'''

print(f"💰 Harga live {symbol}: {price} USDT — Order Size: {qty}")

