# -*- coding: utf-8 -*-.

"""
conn.cursor()
~~~~~~~~~~~~~~~~~~~~~

This module contains the cursor class to the database connection.
"""

from .queries import execute

class cursor():
    """
    The cursor class, main class used to interact with the sheets

    """
    def __init__(self, sheet):
        self.sheet = sheet

    def execute(self, query, args=None):
        """
        Executes your sql query
        Parameters may be provided as tuple and will be bound to variables in the operation.
        Variables are specified either with positional (%s) or named (%(name)s) placeholders.

        :param query: query to be executed
        :param vars: (optional) tuple - vars to be passed to the query
        """

        if args is not None:
            query = query % args
        execute(query, self.sheet)
