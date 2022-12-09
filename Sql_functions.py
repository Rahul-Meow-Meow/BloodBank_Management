import mysql.connector

con = mysql.connector.connect(host='localhost', user='root',
                              passwd='root', autocommit=True)
cur = con.cursor()


def fetch(table):
    try:
        query = 'select * from {}'.format(table)
        cur.execute(query)
        r = cur.fetchall()
        return r
    except Exception:
        print ('Database doesnt exist')
