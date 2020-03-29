import job_board

def exists(table, column_name, value):
    """Return if value exists in column_name in table."""
    exists_query = \
        '''SELECT EXISTS(
        SELECT 1
        FROM {}
        WHERE {} = \'{}\')'''.format(table, column_name, value)
    existsb = job_board.model.get_db().cursor().execute(exists_query).fetchone()
    for k in existsb:
        existsb = existsb[k]
    return existsb


def get(get_column_name, table, column_name, value):
    """Get the value in get_column_name in table."""
    query = \
        '''SELECT {}
        FROM {}
        WHERE {} = \'{}\''''.format(get_column_name, table, column_name, value)
    return job_board.model.get_db().cursor().execute(
        query).fetchone()[get_column_name]