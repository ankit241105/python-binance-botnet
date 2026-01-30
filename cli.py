import argparse
from bot.orders import OrderService
from bot.validators import validate_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    validate_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    service = OrderService()
    response = service.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\nOrder placed successfully")
    print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Qty: {response.get('executedQty')}")
    print(f"Avg Price: {response.get('avgPrice')}")

if __name__ == "__main__":
    main()
