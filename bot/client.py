import os
from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_API_SECRET"),
        )
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"


    def create_order(self, **kwargs):
        try:
            logger.info(f"Sending order: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.exception("API error")
            raise
