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
        sql_insert="""SELECT * FROM STUDENT1"""

        cur.execute(sql)
        row.cur.fetchall()
        print(row)
    except Exception as err:
        print("error while creating the connection", err)
    else:
        print('completed')
        conn.commit()
    finally:
        cur.close()
finally:
    cur.close()
    conn.close()


