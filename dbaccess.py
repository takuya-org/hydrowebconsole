import os
import sqlite3

class DbOperation(object):
    PATH = 'DBPATH'

    def __init__(self):
        self.con = sqlite3.Connection(os.environ.get(PATH))
        c = self.con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS temp(date int, temp_c real""")

    def selectRecord(self, limit, offset):
        c = self.con.cursor()
        c.execute("SELECT * FROM temp ORDER BY date DESC LIMIT ? OFFSET ?", (limit, offset))
        date_list = []
        temp_list = []
        for date, temp in c.fetchall():
            date_list.append(date)
            temp_list.append(temp)
        return {'temperature':temp_list, 'period':date_list}

    def connectionClose(self):
        self.con.close()
