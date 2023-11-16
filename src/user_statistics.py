from flask import Blueprint, render_template, session
import pickle
import json


def statistics():
    data = session['portfolio']
    portfolio = pickle.loads(data)
    data = [{'symbol': portfolio.cryptos[crypto_id]['symbol'], 'value': portfolio.cryptos[crypto_id]['value'], 'logo': portfolio.cryptos[crypto_id]['logo']}
            for crypto_id in portfolio.cryptos]
    data_json = json.dumps(data)
    return render_template('statistics.html', id=session['id'], username=session['username'], data=data_json)
