import json
import requests
from config import keys, TOKEN
class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount:str):
       # values = message.text.split(' ')
       # quote, base, amount = values
        if quote == base:
            raise ConvertionException(f'Equals currencys {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Problem with {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Problem with {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Failed with amount {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base