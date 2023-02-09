
import json
import requests
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod


    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'введены две одинаковые ошибки {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'не удалось обработаь валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'не удалось обработаь валюту {base}')

        try:
            amount = float(amount)
        except ValueErrorError:
            raise ConvertionException(f'не удалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
