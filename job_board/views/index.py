"""
job_board index (main) view.

URLs include:
/
/applicant/
/employer/
"""

import flask
import job_board


@job_board.app.route('/', methods=['GET'])
def show_index():
    """Renders view for index."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for("show_login"))

    if flask.session['account_type'] == "Applicant":
        return flask.redirect(flask.url_for("show_applicant_index"))
    else:
        return flask.redirect(flask.url_for("show_employer_index"))


@job_board.app.route('/applicant/', methods=['GET', 'POST'])
def show_applicant_index():
    """Renders view of job openings for applicant."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for("show_login"))

    # get all openings
    context = {"openings": []}

    get_openings_query = """
    SELECT *
    FROM openings, employers
    WHERE employers.email = openings.email
    ORDER BY date_posted DESC
    """
    openings = job_board.model.get_db().execute(get_openings_query).fetchall()

    for opening in openings:
        state = int(opening['state'])


    context["openings"] = openings

    return flask.render_template("applicant_index.html", **context)


@job_board.app.route('/employer/', methods=['GET', 'POST'])
def show_employer_index():
    """Renders view of employer's listings."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for("show_login"))

    # get all openings that belong to employer
    openings_query = """
    SELECT *
    FROM employers, openings
    WHERE employers.email = openings.email
    """
    openings_query = job_board.model.get_db().execute(openings_query).fetchall()

    context = {"openings": openings_query}

    return flask.render_template("employer_index.html", **context)
