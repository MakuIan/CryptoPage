import requests  # pylint: disable=import-error
from apikey import CRYPTO_COMPARE_API_KEY as CRYPTO_COMPARE  # pylint: disable=import-error
from crypto import Crypto


def get_crypto_data(symbol):
    # Set up the API request parameters
    try:
        params = {
            'asset_symbol': symbol.upper(),
            'api_key': CRYPTO_COMPARE,
        }

        # Send the API request and parse the response
        response = requests.get(
            'https://data-api.cryptocompare.com/asset/v1/data/by/symbol', params=params)
        data = response.json()

        # Extract the relevant data from the response
        crypto_id = data['Data']['ID']
        symbol = data['Data']['SYMBOL']
        name = data['Data']['NAME']
        logo = data['Data']['LOGO_URL']
        price = data['Data']['PRICE_USD']

        # Return the data as a crypto object
        crypto = Crypto(crypto_id, name, symbol, price, logo)
        return crypto
    except KeyError:
        return None
