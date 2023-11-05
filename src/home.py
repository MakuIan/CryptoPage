"""
This module contains the Home page.
"""
from flask import session, render_template, request
# from apikey import CRYPTO_COMPARE_API_KEY as CRYPTO_COMPARE
import requests  # pylint: disable=import-error

from apikey import CRYPTO_COMPARE_API_KEY as CRYPTO_COMPARE  # pylint: disable=import-error


def home():
    """
    Render home page.
    """
    # if request.form['home_btn'] == 'search_btn':
    #     params = {
    #         'asset_symbol': 'BTC',
    #         'api_key': CRYPTO_COMPARE,
    #     }

    #     response = requests.get(
    #         'https://data-api.cryptocompare.com/asset/v1/data/by/symbol?', params=params)
    #     data = response.json()
    #     symbol = data['Data']['SYMBOL']
    #     name = data['Data']['NAME']
    #     return render_template('home.html', id=session['id'], username=session['username'], symbol=symbol, name=name, )
    return render_template('home.html', id=session['id'], username=session['username'], post='true')
