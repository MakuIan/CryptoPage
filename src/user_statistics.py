from flask import Blueprint, render_template, session


def statistics():
    return render_template('statistics.html', id=session['id'], username=session['username'])
