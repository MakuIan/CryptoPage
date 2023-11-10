from portfolio import Portfolio
from flask import render_template, request, session


def del_crypto(portfolio: Portfolio, crypto_id):
    """
    Delete crypto from portfolio.
    """
    portfolio.del_crypto(crypto_id)
    return render_template('home.html', id=session['id'], username=session['username'], portfolio=portfolio)
