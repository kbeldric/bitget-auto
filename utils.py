import requests

def get_bgb_price(default_price=4):
    """
    Ambil harga terakhir BGB/USDT dari Bitget Market API.
    """
    url = "https://api.bitget.com/api/v2/spot/market/tickers?symbol=BGBUSDT_SPBL"
    params = {
        "symbol": "BGBUSDT_SPBL"  # Pastikan menggunakan symbol format SPBL di Bitget 
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Cek apakah respons memiliki data dan format yang benar
        if data.get('code') == '0' and len(data.get('data', [])) > 0:
            price = float(data['data'][0]['close'])  # Akses index 0 karena bentuknya list
            return price
        else:
            print("[ERROR] Data tidak ditemukan di respons API.")
            return default_price

    except Exception as e:
        print(f"[WARN] Gagal mengambil harga dari API: {e}")
        print(f"[INFO] Menggunakan harga fallback: {default_price}")
        return default_price


def calculate_order_size(symbol="BGBUSDT_SPBL"):
    """
    Hitung size order berdasarkan harga pasar dan saldo yang digunakan.
    """
    usdt_balance = 10  # Saldo USDT simulasi
    used_percent = 0.75
    price = get_bgb_price()
    
    if price is None or price <= 0:
        print("Gagal mengambil harga. Tidak bisa menghitung order size.")
        return 0

    qty = (usdt_balance * used_percent) / price
    return round(qty, 2)


# Contoh penggunaan
if __name__ == "__main__":
    current_price = get_bgb_price()
    print(f"Harga BGB saat ini: {current_price}")
    order_size = calculate_order_size()
    print(f"Jumlah BGB yang akan dibeli: {order_size}")
