#Just a script to create hashes if not already done so
import mysql.connector as sql
import datetime
import hashlib, uuid

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
    cursor = con.cursor(buffered=True)
    cursor2 = con.cursor(buffered=True)
    query = ("SELECT id,mail from members WHERE hash<>'';")
    query = ("SELECT id,mail from members WHERE hash IS NULL OR hash='';")
    update = ("UPDATE members SET hash=%s WHERE id=%s")
    cursor.execute(query)

    for (idn, mail) in cursor:
        salt = uuid.uuid4().hex
        hashed = hashlib.sha256(mail).hexdigest()
        salt_hash = hashlib.sha256(mail+salt).hexdigest()
        cursor2.execute(update, [salt_hash, idn])
        con.commit()
        


    cursor.close()
    con.close()
