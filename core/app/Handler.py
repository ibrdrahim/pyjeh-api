__author__ = 'fuadsuyudi@gmal.com'
__license__ = 'MIT'

import json
from datetime import datetime
from time import mktime

class Str(json.JSONEncoder):

    def default(self, obj = None):
        if isinstance(obj, datetime):
            return obj.__str__()
        elif obj == "":
            return None

        return obj

class Format:

    def __init__(self):
        pass

    def build(self, data, message = None, code = 0, status = True):
        json_data = json.dumps(data, cls=Str)
             
        return {'status': status, 'code': code, 'message': message, 'data': json.loads(json_data)}