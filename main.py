import mysql.connector as sql
import datetime

sql_config = {
    'user': 'fyskam',
    'password': 'abc123',
    'host': '130.238.93.229',
    'database': 'register_copy',
    'raise_on_warnings': True,
}

try:
    con = sql.connect(**sql_config)
except sql.Error as err:
    print("There was an error {}".format(err))
else:
    cursor = con.cursor()
    query = ("SELECT firstname,lastname,mail,since from members WHERE since <= %s")
    threshold = datetime.datetime.now() - datetime.timedelta(days=365)
    print("{:%Y-%m-%d}".format(threshold))
    cursor.execute(query, [threshold])

    for (firstname, lastname, mail, since) in cursor:
        print("{:%Y %b %d} {} {} {} ".format(since, firstname.encode("UTF-8"), lastname.encode("UTF-8"), mail.encode("UTF-8")))


    cursor.close()
    con.close()
