def calculate_order_size(symbol):
    # Hitung size order dari saldo, misal 90% dari 10 USDT
    usdt_balance = 10
    used_percent = 0.9
    price = 0.01  # harga BGB, bisa ambil dari API market
    qty = (usdt_balance * used_percent) / price
    return round(qty, 2)
