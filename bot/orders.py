import logging
import time

def wait_for_order_fill(client, symbol, order_id):
    for _ in range(5):  # 5 retries
        order = client.futures_get_order(symbol=symbol, orderId=order_id)
        status = order.get("status")

        if status == "FILLED":
            return order

        time.sleep(2)

    return order

def place_market_order(client, symbol, side, quantity):
    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logging.info(f"Market Order Response: {response}")
        return response
    except Exception as e:
        logging.error(f"Market Order Error: {e}")
        raise

def place_limit_order(client, symbol, side, quantity, price):
    try:
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logging.info(f"Limit Order Response: {response}")
        return response
    except Exception as e:
        logging.error(f"Limit Order Error: {e}")
        raise