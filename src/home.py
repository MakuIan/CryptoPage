"""
This module contains the Home page.
"""
from flask import session, render_template, request
# from apikey import CRYPTO_COMPARE_API_KEY as CRYPTO_COMPARE
import requests  # pylint: disable=import-error

from apikey import CRYPTO_COMPARE_API_KEY as CRYPTO_COMPARE  # pylint: disable=import-error


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
        symbol = data['Data']['SYMBOL']
        name = data['Data']['NAME']
        logo = data['Data']['LOGO_URL']
        price = data['Data']['PRICE_USD']

        # Return the data as a dictionary
        return {
            'symbol': symbol,
            'name': name,
            'logo': logo,
            'price': price,
        }
    except KeyError:
        return None


def home():
    """
    Render home page.
    """
    if request.form['home_btn'] == 'search_btn':
        search = request.form['search-input']
        res = get_crypto_data(search)
        if res is None:
            return render_template('home.html', id=session['id'], username=session['username'], msg='Invalid Symbol')
        data = {
            'symbol': res['symbol'],
            'name': res['name'],
            'logo': res['logo'],
            'price': res['price'],
        }
        return render_template('home.html', id=session['id'], username=session['username'], data=data)
    if request.form['home_btn'] == 'add_crypto_btn':
        return render_template('home.html', id=session['id'], username=session['username'], msg='Added')

    return render_template('home.html', id=session['id'], username=session['username'])
