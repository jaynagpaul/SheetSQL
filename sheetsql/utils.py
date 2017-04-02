# -*- coding: utf-8 -*-.

"""
sheetsql.utils
~~~~~~~~~~~~~~

This module contains utils for sheetsql
"""

from oauth2client.service_account import ServiceAccountCredentials
import oauth2client

def signed_creds(path):
    """
    Converts filepath to oauth2client signed account credentials object.

    :param path: path to credentials json file
    """
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
    except oauth2client.client.CryptoUnavailableError: #Used to bypass error in gspread
        import pip
        import site
        from importlib import reload
        pip.main(['install', 'PyOpenSSL'])
        reload(site)
        credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
    return credentials

def setupschema(sheet):
    """
    Setups the spreadsheet 'schema' for use as a database

    :param sheet: spreadsheet to convert to a SheetSQL db
    """

    wkst = sheet.get_worksheet(0)
    wkst.update_title('SheetSQL')
