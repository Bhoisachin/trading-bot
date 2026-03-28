def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side Use BUY or SELL only")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

def validate_quantity(qty):
    if float(qty) <= 0:
        raise ValueError("Quantity must be positive")

def validate_price(price, order_type):
    if order_type == "LIMIT" and (price is None or float(price) <= 0):
        raise ValueError("Valid price required for LIMIT orders")