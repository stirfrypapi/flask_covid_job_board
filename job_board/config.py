"""job_board development configuration."""

import os

# Root of this application, useful if it
# doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xe4@\x88\x92\x1d,b\xc1\xaa\xf1&G\xb1q~\xb76\x1bs\xc27\xe5M\x1e'
SESSION_COOKIE_NAME = 'login'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'job_board.sqlite3'
)