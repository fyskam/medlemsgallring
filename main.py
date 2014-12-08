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
    query = ("SELECT firstname,lastname,mail,since,hash from members WHERE active=0")
    update = ("UPDATE members SET active=0 WHERE since <= %s")
    threshold = datetime.datetime.now() - datetime.timedelta(days=365)
    cursor.execute(update, [threshold]) #Sätt alla som varit medlemar >= 1 år som inaktiva
    cursor.execute(query) #Välj alla inaktiva

    for (firstname, lastname, mail, since, hashex) in cursor:
        print("{:%Y %b %d} {} {} {} ".format(since, firstname.encode("UTF-8"), lastname.encode("UTF-8"), mail.encode("UTF-8")))
        msg = sc_compose.compose(hashex);
        print(msg)
        print("\n\n")
        sc_mail.send("Medlemskontroll", msg, mail)

    sc_cron.set_job(0)
    cursor.close()
    con.close()
