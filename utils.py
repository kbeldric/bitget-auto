import requests

def get_bgb_price(default_price=4):
    """
    Ambil harga terakhir BGB/USDT dari Bitget Market API.
    """
    url = f"https://api.bitget.com/api/v2/spot/market/tickers?symbol=BGBUSDT"
    params = {
        "symbol": "BGBUSDT"
    }
    try:
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
    price = get_bgb_price()
    
    if price is None:
        print("Gagal mengambil harga. Tidak bisa menghitung order size.")
        return 0

    qty = (usdt_balance * used_percent) / price
    return round(qty, 2)
