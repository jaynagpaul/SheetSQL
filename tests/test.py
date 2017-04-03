"""
Upcoming test file for CI
"""

import sheetsql

conn = sheetsql.Connection(service_file='creds.json')
conn.create('test')
cur = conn.cursor('test')
