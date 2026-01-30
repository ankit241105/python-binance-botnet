from bot.client import BinanceFuturesClient

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        return self.client.create_order(**params)
