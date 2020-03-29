"""
job_board accounts view.

URLs include:
/accounts/login/
/accounts/create/
"""

from job_board.views.utils import *

import flask
import job_board


def is_correct_account(username, password):
    """Return whether or not the username and password is valid."""
    if not exists('accounts', 'email', username):
        return False

    password_db_string = get("password", "accounts", "email", username)

    return password_db_string == password


@job_board.app.route('/accounts/login/', methods=['GET', 'POST'])
def show_login():
    """Render view for /accounts/login/ route."""
    if flask.request.method == 'POST':
        # check if username and password match what is in database
        if is_correct_account(flask.request.form['username'],
                              flask.request.form['password']):
            flask.session['username'] = flask.request.form['username']
            flask.session['password'] = flask.request.form['password']
            flask.session['account_type'] = get('account_type', 'accounts', 'email', flask.session['username'])

            return flask.redirect(flask.url_for('show_index'))
        return flask.abort(403)
    return flask.render_template("login.html")


@job_board.app.route('/accounts/create/', methods=['GET', 'POST'])
def show_create():
    """Render view for /accounts/create/ route."""
    if 'username' in flask.session:
        # redirect to /accounts/edit
        return flask.redirect(flask.url_for('show_index'))
    if flask.request.method == 'POST':
        flask.session['username'] = flask.request.form['email']
        flask.session['password'] = flask.request.form['password']
        flask.session['account_type'] = flask.request.form['account_type']

        # if username already exists, abort(409)
        if exists('accounts', 'email', flask.request.form['email']):
            flask.abort(409)

        # if password is empty string, abort(400)
        if flask.request.form['password'] == '' or \
                flask.request.form['password'] != \
                flask.request.form["password_again"]:
            flask.abort(400)

        # upon all validation checks, insert into table
        insert_query = """
        INSERT INTO accounts(email, password)
        VALUES(\'{}\', \'{}\')
        """.format(flask.session['username'], flask.session['password'])

        job_board.model.get_db().cursor().execute(insert_query)

        return flask.redirect(flask.url_for('show_applicant_index'))
    return flask.render_template("create.html")
