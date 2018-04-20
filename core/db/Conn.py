__author__ = 'fuadsuyudi@gmal.com'
__license__ = 'MIT'

import MySQLdb
from DBUtils.PersistentDB import PersistentDB
from library.logging.Log import logger

class MySql:
    def __init__(self, creator, *args, **kwargs):
        self.pool = PersistentDB(creator, *args, **kwargs)
        self._creator = creator
        self._args, self._kwargs = args, kwargs
        
    def connection(self):
        try:
            connection = self.pool.connection()
            
            return connection
        except Exception as er:
            logger(str(er))
