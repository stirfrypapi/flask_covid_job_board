"""
job_board index (main) view.

URLs include:
/
/applicant/
/employer/
/applicant/filename
"""

from job_board.static.covid_cases import COVID_CASES_STATE

import flask
import job_board
import matplotlib
import matplotlib.pyplot as plt
import us

matplotlib.use('Agg')


@job_board.app.route('/applicant/<path:filename>')
def show_image(filename):
    """Render images in templates."""
    return flask.send_from_directory(job_board.app.config['GRAPHS_FOLDER'],
                                     filename,
                                     as_attachment=True)


@job_board.app.route('/', methods=['GET'])
def show_index():
    """Renders view for index."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for("show_login"))

    if flask.session['account_type'] == "Applicant":
        return flask.redirect(flask.url_for("show_applicant_index"))
    else:
        return flask.redirect(flask.url_for("show_employer_index"))


def get_applicant_context():
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
        opening_state = opening['state']

        # get dataframe of matching states
        state_cases = COVID_CASES_STATE[
            COVID_CASES_STATE["state_obj"] == us.states.lookup(
                opening_state)].sort_values(by="date")

        # create line graph
        sub_plt, ax = plt.subplots()
        state_cases.set_index('date')['cases'].plot(figsize=(6, 4),
                                                    linewidth=2.5,
                                                    color='maroon')

        # update axis and title
        ax.set_xlabel("Date", labelpad=15)
        ax.set_ylabel("Number of Cases", labelpad=15)
        ax.set_title("Number of Cases Over Time in %s" % opening_state, y=1.02,
                     fontsize=14)

        # save figure for html output
        graph_filename = "./job_board/static/graphs/{}_state_cases.png".format(
            opening_state)
        graph_name = '{}_state_cases.png'.format(opening_state)
        sub_plt.savefig(graph_filename)

        opening["graph_filename"] = graph_name

    context["openings"] = openings
    return context


@job_board.app.route('/applicant/', methods=['GET', 'POST'])
def show_applicant_index():
    """Renders view of job openings for applicant."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for("show_login"))

    if flask.request.method == 'POST':
        opening_id = int(flask.request.form['opening_id'])

        # insert into applications table
        insert_query = """
        INSERT INTO applications(email, opening_id, status)
        VALUES (\'[{}]\', {}, 'submitted')
        """.format(flask.session["username"], opening_id)

        print(opening_id, type(opening_id))
        print(flask.session["username"])
        print(insert_query)

        job_board.model.get_db().execute(insert_query)

    context = get_applicant_context()

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
