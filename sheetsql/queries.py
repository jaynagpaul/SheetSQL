"""
sheetsql.queries
~~~~~~~~~~~~~~~~

All possible SQL queries for sheetsql.
"""
from ast import literal_eval
import sqlparse
from sqlparse.tokens import Keyword, DML, DDL, Punctuation
from sqlparse import sql as Identifiers


Parenthesis = Identifiers.Parenthesis
Identifier = Identifiers.Identifier
def remove_trash(parsed):
    """
    Itterates through parsed sql statement and removes all whitespace and punctuation (Internal)
    Returns list of keywords

    :params parsed: parsed sql statement 'sqlparse.parse(sql)[0]'
    """
    good_stuff = list()
    for i in parsed.tokens:
        if i.ttype is DML or i.ttype is DDL:
            good_stuff.append(i.value.upper()) #Standardizes all DMLs and DDLs
        elif i.ttype is Keyword or isinstance(i, Parenthesis) or isinstance(i, Identifier):
            good_stuff.append(i.value)
    return good_stuff

def execute(query, sheet):
    """
    Parses through the query(s) and executes the corresponding function
    :param query: sql query to be executed on the spreadsheet
    """

    queries = sqlparse.format(query, keyword_case='lower', strip_comments=True) #Standardizes all queries
    for q in queries:
        q = sqlparse.parse(q)[0]
        clean_query = remove_trash(q) #Removes all whitespace and useless punctuation

        if clean_query[0].upper() == 'CREATE' and clean_query[1].upper() == 'TABLE':
            CREATE_TABLE(clean_query, sheet)

def CREATE_TABLE(sql, sheet):
    """
    Creates a table/worksheet in the spreadsheet provided with the columns provided

    :params sql: parsed sql query
    :params sheet: spreadsheet in which the table should be created
    """
    table_name = sql[2]
    column_names = literal_eval(sql[3]) #Safely converts string to tuple
    columns = len(column_names)

    wkst = sheet.add_worksheet(table_name, rows=1000, cols=columns)
    num = 1
    while num <= columns:
        wkst.update_cell(1, num, column_names[num])
        num += 1
        