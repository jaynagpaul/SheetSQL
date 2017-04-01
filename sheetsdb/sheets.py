import pygsheets

class Connection():
    """
    Login to Google Sheets API using OAuth2 or Service File credentials.
    This function creates the connection to your database.

    :param oauth: path to OAuth2 credentials file, or tokens file
    :param service_file: path to service credentials file
    :param credentials: OAuth2 credentials object
    :returns: :class:`Client` instance.
    >>> conn = sheetsdb.Connection(oauth=OAuthCredentialObject)
    """
    def __init__(self, oauth=None, service_file=None, credentials=None):
        if oauth:
            self.api = pygsheets.authorize(outh_file=oauth)
        elif service_file:
            self.api = pygsheets.authorize(service_file=service_file)
        elif credentials:
            self.api = pygsheets.authorize(credentials=credentials)
        else:
            raise TypeError("Must pass at least 1 argument: oauth, service_file, or credentials")
    #Add more based off of psycopg2
#@property will probably be useful
