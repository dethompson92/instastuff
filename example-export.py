#!/usr/bin/env python3

from instastuff import *

# Numeric user id of the target user account.
#
# To find a user id use this tool - https://codeofaninja.com/tools/find-instagram-user-id/
#
# Example:
#   target_user_id = '234567890'
target_user_id = '<432768477>'

# Value of the `sessionid` cookie when logged into Instagram web.
#
# To find the session id cookie use Chrome Developer Tools > Application > Cookies.
#
# Example: 
#   session_id = '345678901%3AaGVsbG8geW91%3A1'
session_id = '<432768477%3AYCkLwMEyjeUoYX%3A0%3AAYcY05Z_wYoXTwk2mt89JcNNGRvX70DnmLhgZuhkrA>'

# Run the exporter.
#
# Note: a response status code 429 usually indicates an invalid session id.
write_users(target_user_id, session_id)
