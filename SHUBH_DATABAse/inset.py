import cx_Oracle
try:
    #create connection
    conn=cx_Oracle.connect('scott/tiger@//loclahost:1050/xe')
except Exception as err:
    print("error while creating the connection",err)
else:
    print(conn.version)
    try:
        # create cursor
        cur = conn.cursor()
        sql_insert="""INSERT INTO STUDENT1 VALUES(1,'MERA','CS',21)"""
        data = [(2, 'asha'.'EC', 23), (3, 'depa', 'mech', 21)]
        cur.executemany(sql_insert)
    except Exception as err:
        print("error while creating the connection", err)
    else:
        print('insert completed')
        conn.commit()
finally:
    cur.close()
    conn.close()


