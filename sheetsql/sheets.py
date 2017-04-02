# -*- coding: utf-8 -*-.

"""
sheetsql.Connection()
~~~~~~~~~~~~~~~~~~~~~

This module contains the connection class to the database.
"""

import gspread #Google Sheets API
from .cursor import cursor
from .utils import signed_creds, setupschema

class Connection():
    """
    Login to Google Sheets API using OAuth2 or Service File credentials.
    This function creates the connection to your database.

    :param service_file: path to service credentials file
    :param credentials: OAuth2 credentials object
    :returns: :class:`Client` instance.
    >>> conn = sheetsql.Connection(oauth=OAuthCredentialObject)
    """

    def __init__(self, service_file=None, credentials=None):
        if service_file:
            service_file = signed_creds(service_file)
            self.api = gspread.authorize(credentials=service_file)
        elif credentials:
            self.api = gspread.authorize(credentials=credentials)
        else:
            raise TypeError("Must pass at least 1 argument: oauth, service_file, or credentials")

    def cursor(self, title=None, url=None, key=None):
        """
        Database cursor, modeled after psycopg2's cursor class
        This function is responsible for executing all queries to the database.

        :param title: title of spreadsheet to open, if multiple found opens first found
        :param url: url of spreadsheet to open
        :param key: id of spreadsheet to open
        >>> cur = conn.cursor()
        """

        if title is not None:
            return cursor(self.api.open(title))
        elif url is not None:
            return cursor(self.api.open_by_url(url))
        elif key is not None:
            return cursor(self.api.open_by_key(key))
        else:
            raise TypeError("Must pass at least 1 argument: title, url, or id")

    def create(self, title, email=None):
        """
        Initiates a new spreadsheet
        Requires Google Drive API access
        TODO:
        Setup Schema

        :param title: title of spreadsheet to be created
        :param email: (optional) email to share the spreadsheet to
        """

        spreadsheet = self.api.create(title)
        if email is not None:
            spreadsheet.share(email, perm_type='user', role='writer')
        setupschema(spreadsheet)
