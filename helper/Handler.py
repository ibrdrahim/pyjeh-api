import json
from datetime import datetime
from time import mktime

class Handler(json.JSONEncoder):

    def default(self, obj = None):
        if isinstance(obj, datetime):
            return obj.__str__()
        elif obj == "":
            return None

        return obj