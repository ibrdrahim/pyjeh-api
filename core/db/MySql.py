import MySQLdb
import math
import re
from core.db.Conn import MySql
from ConfigParser import ConfigParser
from library.logging.Log import logger

class Select():
    select = []
    query = []
    fetch = ''

    def __init__(self, database = 'mysql'):
        try:
            config = ConfigParser()
            config.read('config/pyjeh.conf')
                
            pool = MySql(MySQLdb, host=config.get(database,'host'), user=config.get(database,'username'), passwd=config.get(database,'password'), db=config.get(database,'database'), port=int(config.get(database,'port')), charset='utf8')
            self.conn = pool.connection()
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        except Exception as er:
			logger(str(er))

    def __del__(self):
        Select.select = []
        Select.query = []
        Select.fetch = ''
        self.cursor.close()
        self.conn.close()

    def fetchall(self):
        Select.fetch = 'all'

    def fetchone(self):
        Select.fetch = 'one'

    def get(self):
        build = Select.select + Select.query
        
        try:
            self.cursor.execute(' '.join(build))
            
            if Select.fetch == 'one':
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchall()
        except Exception as er:
            logger(str(er))
            return None

    def table(self, table, field = '*'):
        Select.select.append("SELECT {} FROM `{}`".format(field, table))
    
    def getpaginate(self, sql, perpage, page):
        data = {}

        try:
            self.cursor.execute(sql)
            lists = self.cursor.fetchall()

            pages = math.ceil(float(len(lists)) / float(perpage))

            next = None
            if page < pages:
                next = page + 1

            prev = None
            if page > 1:
                prev = page - 1

            data = {'total': len(lists), 'perpage': perpage, 'curpage': page, 'next': next, 'prev': prev, 'pages': pages, 'items': None}
            
            return data
        except Exception as er:
            logger(str(er))
            return None

    def raw(self, value):
        Select.query.append("{}".format(value))
    
    def where(self, field, value, operator = '='):
        number = re.search('^(0|[1-9][0-9]*)$', value)
        if len(Select.query) == 0:
            if number:
                Select.query.append("WHERE {} {} {}".format(field, operator, value))
            else:
                Select.query.append("WHERE {} {} '{}'".format(field, operator, value))
        else:
            if number:
                Select.query.append("AND {} {} {}".format(field, operator, value))
            else:
                Select.query.append("AND {} {} '{}'".format(field, operator, value))

    def orWhere(self, field, value, operator = '='):
        number = re.search('^(0|[1-9][0-9]*)$', value)
        if len(Select.query) == 0:
            if number:
                Select.query.append("WHERE {} {} {}".format(field, operator, value))
            else:
                Select.query.append("WHERE {} {} '{}'".format(field, operator, value))
        else:
            if number:
                Select.query.append("OR {} {} {}".format(field, operator, value))
            else:
                Select.query.append("OR {} {} '{}'".format(field, operator, value))

    def notWhere(self, field, value):
        number = re.search('^(0|[1-9][0-9]*)$', value)
        if len(Select.query) == 0:
            if number:
                Select.query.append("WHERE NOT {} = {}".format(field, value))
            else:
                Select.query.append("WHERE NOT {} = '{}'".format(field, value))
        else:
            if number:
                Select.query.append("AND NOT {} = {}".format(field, value))
            else:
                Select.query.append("AND NOT {} = '{}'".format(field, value))

    def Like(self, field, value):
        if len(Select.query) == 0:
            Select.query.append("WHERE {} LIKE '{}'".format(field, value))
        else:
            Select.query.append("AND {} LIKE '{}'".format(field, value))
    
    def inWhere(self, field, value):
        if len(Select.query) == 0:
            Select.query.append("WHERE {} IN ({})".format(field, ','.join(value)))
        else:
            Select.query.append("AND {} IN ({})".format(field, ','.join(value)))

    def between(self, field, value_a, value_b):
        if len(Select.query) == 0:
            Select.query.append("WHERE {} BETWEEN {} AND {}".format(field, value_a, value_b))
        else:
            Select.query.append("AND {} BETWEEN {} AND {}".format(field, value_a, value_b))

    def order_by(self, field_a, field_b = None):
        if field_b:
            Select.query.append("ORDER BY {} {}, {} {}".format(field_a[0], field_a[1], field_b[0], field_b[1]))
        else:
            Select.query.append("ORDER BY {} {}".format(field_a[0], field_a[1]))

    def join(self, join, field, condition):
        Select.query.append("{} JOIN {} ON {}".format(join, field, condition))

    def group_by(self, field, short = 'ASC'):
        Select.query.append("GROUP BY {} {}".format(field, short))
    
    def limit(self, limit, start = 0):
        Select.query.append("LIMIT {},{}".format(start, limit))

    def having(self, field, value, operator = '='):
        num_field = re.search('^(0|[1-9][0-9]*)$', field)
        num_value = re.search('^(0|[1-9][0-9]*)$', value)
        if (num_field and num_value):
            if num_field:
                Select.query.append("HAVING {} {} '{}'".format(field, operator, value))
            elif num_value:
                Select.query.append("HAVING '{}' {} {}".format(field, operator, value))
            else:
                Select.query.append("HAVING {} {} {}".format(field, operator, value))
        else:
            Select.query.append("HAVING '{}' {} '{}'".format(field, operator, value))

    def paginate(self, perpage = 10, page = 1):
        start = (page - 1) * perpage
        limit = perpage

        join = Select.select + Select.query
        sql = ' '.join(join)
        paginate = self.getpaginate(sql, perpage, page)

        Select.query.append("LIMIT {},{}".format(int(start), int(limit)))
        Select.fetch = 'all'

        paginate['items'] = self.get()

        return paginate

class Update():
    update = []
    change = []
    query = []

    def __init__(self, database = 'mysql'):
        try:
            config = ConfigParser()
            config.read('config/pyjeh.conf')
                
            pool = MySql(MySQLdb, host=config.get(database,'host'), user=config.get(database,'username'), passwd=config.get(database,'password'), db=config.get(database,'database'), port=int(config.get(database,'port')), charset='utf8')
            self.conn = pool.connection()
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        except Exception as er:
			logger(str(er))

    def __del__(self):
        Update.update = []
        Update.change = []
        Update.query = []
        self.cursor.close()
        self.conn.close()

    def get(self):
        build = Update.update + [','.join(Update.change)] + Update.query
        
        print ' '.join(build)

        try:
            self.cursor.execute(' '.join(build))
            
            return self.conn.commit()
        except Exception as er:
            logger(str(er))
            self.conn.rollback()
            return None

    def table(self, table):
        Update.update.append("UPDATE {}".format(table))
    
    def raw(self, value):
        Update.query.append("{}".format(value))

    def set(self, value):
        for item in value:
            if value.get(item):
                number = re.search('^(0|[1-9][0-9]*)$', value.get(item))
                if len(Update.change) == 0:
                    if number:
                        Update.change.append("SET {} = {}".format(item, value.get(item)))
                    else:
                        Update.change.append("SET {} = '{}'".format(item, value.get(item)))
                else:
                    if number:
                        Update.change.append("{} = {}".format(item, value.get(item)))
                    else:
                        Update.change.append("{} = '{}'".format(item, value.get(item)))
    
    def where(self, field, value, operator = '='):
        number = re.search('^(0|[1-9][0-9]*)$', value)
        if len(Update.query) == 0:
            if number:
                Update.query.append("WHERE {} {} {}".format(field, operator, value))
            else:
                Update.query.append("WHERE {} {} '{}'".format(field, operator, value))
        else:
            if number:
                Update.query.append("AND {} {} {}".format(field, operator, value))
            else:
                Update.query.append("AND {} {} '{}'".format(field, operator, value))

    def orWhere(self, field, value, operator = '='):
        number = re.search('^(0|[1-9][0-9]*)$', value)
        if len(Update.query) == 0:
            if number:
                Update.query.append("WHERE {} {} {}".format(field, operator, value))
            else:
                Update.query.append("WHERE {} {} '{}'".format(field, operator, value))
        else:
            if number:
                Update.query.append("OR {} {} {}".format(field, operator, value))
            else:
                Update.query.append("OR {} {} '{}'".format(field, operator, value))

    def notWhere(self, field, value):
        number = re.search('^(0|[1-9][0-9]*)$', value)
        if len(Update.query) == 0:
            if number:
                Update.query.append("WHERE NOT {} = {}".format(field, value))
            else:
                Update.query.append("WHERE NOT {} = '{}'".format(field, value))
        else:
            if number:
                Update.query.append("AND NOT {} = {}".format(field, value))
            else:
                Update.query.append("AND NOT {} = '{}'".format(field, value))

class Insert():
    insert = []
    query = []

    def __init__(self, database = 'mysql'):
        try:
            config = ConfigParser()
            config.read('config/pyjeh.conf')
                
            pool = MySql(MySQLdb, host=config.get(database,'host'), user=config.get(database,'username'), passwd=config.get(database,'password'), db=config.get(database,'database'), port=int(config.get(database,'port')), charset='utf8')
            self.conn = pool.connection()
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        except Exception as er:
			logger(str(er))

    def __del__(self):
        Insert.insert = []
        Insert.query = []
        self.cursor.close()
        self.conn.close()

    def get(self):
        build = Insert.insert + Insert.query

        print ' '.join(build)
        
        try:
            self.cursor.execute(' '.join(build))
        
            return self.conn.commit()
        except Exception as er:
            logger(str(er))
            self.conn.rollback()
            return None
        
    def table(self, table):
        Insert.insert.append("INSERT INTO {}".format(table))
    
    def raw(self, value):
        Insert.query.append("{}".format(value))

    def fields(self, field):
        Insert.query.append("({})".format(','.join(field)))

    def values(self, value):
        Insert.query.append("VALUES('{}')".format("','".join(value)))

class Delete():
    delete = []
    query = []

    def __init__(self, database = 'mysql'):
        try:
            config = ConfigParser()
            config.read('config/pyjeh.conf')
                
            pool = MySql(MySQLdb, host=config.get(database,'host'), user=config.get(database,'username'), passwd=config.get(database,'password'), db=config.get(database,'database'), port=int(config.get(database,'port')), charset='utf8')
            self.conn = pool.connection()
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        except Exception as er:
			logger(str(er))

    def __del__(self):
        Delete.delete = []
        Delete.query = []
        self.cursor.close()
        self.conn.close()

    def get(self):
        build = Delete.delete + Delete.query

        try:
            self.cursor.execute(' '.join(build))
        
            return self.conn.commit()
        except Exception as er:
            logger(str(er))
            self.conn.rollback()
            return None
        
    def table(self, table):
        Delete.delete.append("DELETE FROM `{}`".format(table))
    
    def raw(self, value):
        Delete.query.append("{}".format(value))
    
    def where(self, field, value, operator = '='):
        number = re.search('^(0|[1-9][0-9]*)$', value)
        if len(Delete.query) == 0:
            if number:
                Delete.query.append("WHERE {} {} {}".format(field, operator, value))
            else:
                Delete.query.append("WHERE {} {} '{}'".format(field, operator, value))
        else:
            if number:
                Delete.query.append("AND {} {} {}".format(field, operator, value))
            else:
                Delete.query.append("AND {} {} '{}'".format(field, operator, value))

    def orWhere(self, field, value, operator = '='):
        number = re.search('^(0|[1-9][0-9]*)$', value)
        if len(Delete.query) == 0:
            if number:
                Delete.query.append("WHERE {} {} {}".format(field, operator, value))
            else:
                Delete.query.append("WHERE {} {} '{}'".format(field, operator, value))
        else:
            if number:
                Delete.query.append("OR {} {} {}".format(field, operator, value))
            else:
                Delete.query.append("OR {} {} '{}'".format(field, operator, value))

    def notWhere(self, field, value):
        number = re.search('^(0|[1-9][0-9]*)$', value)
        if len(Delete.query) == 0:
            if number:
                Delete.query.append("WHERE NOT {} = {}".format(field, value))
            else:
                Delete.query.append("WHERE NOT {} = '{}'".format(field, value))
        else:
            if number:
                Delete.query.append("AND NOT {} = {}".format(field, value))
            else:
                Delete.query.append("AND NOT {} = '{}'".format(field, value))