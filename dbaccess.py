import os
import sqlite3

class DbOperation(object):
    PATH = 'DBPATH'

    def __init__(self):
        self.con = sqlite3.Connection(os.environ.get(DbOperation.PATH))
        c = self.con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS temp(date text, time text, temp_c real)""")

    def selectRecord(self, limit, offset):
        c = self.con.cursor()
        c.execute("SELECT * FROM temp ORDER BY date, time DESC LIMIT ? OFFSET ?", (limit, offset))
        date_list = []
        temp_list = []
        for date, time, temp in c.fetchall():
            date_list.insert(0, date + ' ' + time)
            temp_list.append(temp)
        return {'temperature':temp_list, 'period':date_list}

    def connectionClose(self):
        self.con.close()
