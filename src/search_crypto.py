import pickle
from flask import session, render_template, request
from get_crypto_data import get_crypto_data


def search_crypto(portfolio):
    search = request.form['search-input']
    data = get_crypto_data(search)
    if data is None:
        return render_template('home.html', id=session['id'], username=session['username'], msg='Invalid Symbol', portfolio=portfolio)
    if data.id is not None:
        session['crypto'] = pickle.dumps(data)
    return render_template('home.html', id=session['id'], username=session['username'], data=data, portfolio=portfolio)
