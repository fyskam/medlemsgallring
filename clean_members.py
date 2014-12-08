#import subprocess

#subprocess.call(["touch", "foo.bar"]) #dummy command

import mysql.connector as sql
import datetime
import sc_mail, sc_compose, sc_cron

sql_config = {
    'user': 'fyskam',
    'password': 'abc123',
    'host': '130.238.247.3',
    'database': 'register_copy',
    'raise_on_warnings': True,
}

try:
    con = sql.connect(**sql_config)
except sql.Error as err:
    print("There was an error {}".format(err))
else:
    cursor = con.cursor()
    query = ("DELETE FROM members WHERE active=0")
    cursor.execute(query)

    cursor.close()
    con.close()
