from json import JSONEncoder
from pyflection import PyflectiveEncoder


# Extremely Simple Class.
# only has two string properties.

class RESTfulLogin(PyflectiveEncoder):
    username = ""
    password = ""

    def __init__(self, user: str, pasw: str, *args, **kwargs):
        self.username = user
        self.password = pasw
        super(RESTfulLogin, self).__init__(*args, **kwargs)
