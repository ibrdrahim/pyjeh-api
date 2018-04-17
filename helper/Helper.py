from datetime import datetime
from ConfigParser import ConfigParser

class Helper:

    def __init__(self):
        pass

    def raw(self, data, message = None, code = 0, status = True):
        return {'status': status, 'code': code, 'message': message, 'data': data}