import sqlite3
class DbOperation(object):
    DIR = 'dbtest/'
    FILE_NAME = 'hydroponics.db'

    def __init__(self):
        self.con = sqlite3.Connection(DbOperation.DIR + DbOperation.FILE_NAME)
        c = self.con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS temp(date text, temp_c real, PRIMARY KEY(date))""")

    def selectRecord(self, limit, offset):
        c = self.con.cursor()
        c.execute("SELECT * FROM temp LIMIT ? OFFSET ?", (limit, offset))
        date_list = []
        temp_list = []
        for date, temp in c.fetchall():
            date_list.append(date)
            temp_list.append(temp)
        return {'temperature':temp_list, 'period':date_list}

    def connectionClose():
        self.con.close()
