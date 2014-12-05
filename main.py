import mysql.connector as sql
import datetime
import sc_mail, sc_compose

sql_config = {
    'user': 'fyskam',
    'password': 'abc123',
    'host': '130.238.93.116',
    'database': 'register_copy',
    'raise_on_warnings': True,
}

try:
    con = sql.connect(**sql_config)
except sql.Error as err:
    print("There was an error {}".format(err))
else:
    cursor = con.cursor()
    query = ("SELECT firstname,lastname,mail,since,hash from members WHERE since <= %s")
    query = ("SELECT firstname,lastname,mail,since,hash from members WHERE id=1")
    update = ("UPDATE members SET active=0 WHERE since <= %s")
    threshold = datetime.datetime.now() - datetime.timedelta(days=365)
    print("{:%Y-%m-%d}".format(threshold))
    cursor.execute(update, [threshold])
#    cursor.execute(query, [threshold])
    cursor.execute(query)

    for (firstname, lastname, mail, since, hashex) in cursor:
        print("{:%Y %b %d} {} {} {} ".format(since, firstname.encode("UTF-8"), lastname.encode("UTF-8"), mail.encode("UTF-8")))
        msg = sc_compose.compose(hashex);
        print(msg)
        sc_mail.send("Medlemskontroll", msg, mail)


    cursor.close()
    con.close()
