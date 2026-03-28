import typer
from bot.client import get_client
from bot.orders import place_market_order, place_limit_order
from bot.validators import *
from bot.logging_config import setup_logger

app = typer.Typer()

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = typer.Option(None)
):
    setup_logger()

    try:
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        client = get_client()

        print("\n=== Order Request ===")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        if order_type == "MARKET":
            response = place_market_order(client, symbol, side, quantity)
        else:
            response = place_limit_order(client, symbol, side, quantity, price)

        print("\n=== Order Response ===")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")

        if response.get("status") == "FILLED":
          print(f"Executed Qty: {response.get('executedQty')}")
          print(f"Avg Price: {response.get('avgPrice')}")
        else:
           print("Order not filled yet (pending)")

        print("\n Order placed successfully!")

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    app()