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
finally:
    cur.close()
    conn.close()

sql_create="""
CREATE TABLE STUDENT1(
    SID NUMBER(5) PRIMARY KEY,
    SNAME VARCHAR(10),
    BRANCH VARCHAR(10),
    AGE NUMBER(4)
)
"""
cur.execute(sql_create)
print('Table created')
