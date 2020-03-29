"""
Preprocess covid19 datasets.
"""

import pandas as pd
import numpy as np
import us

# Covid19 Cases by State
COVID_CASES_STATE = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")


def convert_state_to_stateobj(row):
    row["state_obj"] = us.states.lookup(row["state"])
    return row


def preprocess_covid_cases_state():
    """Preprocess COVID_CASES_STATE"""

    global COVID_CASES_STATE

    # add column on state objects for comparison
    COVID_CASES_STATE = COVID_CASES_STATE.apply(convert_state_to_stateobj, axis=1)


preprocess_covid_cases_state()
