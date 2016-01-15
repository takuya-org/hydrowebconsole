import datetime
import sqlite3
DIR = ''
FILE_NAME = 'hydroponics.db'

con = sqlite3.Connection(DIR + FILE_NAME)
c = con.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS temp(date int, temp_c real""")

c = con.cursor()
c.execute("INSERT INTO temp(date, temp_c) VALUES(?, ?)", ('2016-01-12', 11.5))
c.execute("INSERT INTO temp(date, temp_c) VALUES(?, ?)", ('2016-01-13', 12.4))
c.execute("INSERT INTO temp(date, temp_c) VALUES(?, ?)", ('2016-01-14', 10.7))
c.execute("INSERT INTO temp(date, temp_c) VALUES(?, ?)", ('2016-01-15', 9.3))
c.execute("INSERT INTO temp(date, temp_c) VALUES(?, ?)", ('2016-01-16', 12.1))
c.execute("INSERT INTO temp(date, temp_c) VALUES(?, ?)", ('2016-01-17', 8.9))
con.commit()
con.close()
