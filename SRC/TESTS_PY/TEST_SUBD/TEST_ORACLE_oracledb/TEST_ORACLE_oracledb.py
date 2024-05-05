#=======================================================================================
# TEST_ORACLE_oracledb.py
#=======================================================================================

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import argparse
import datetime
import getpass
import oracledb

#------------------------------------------
#БИБЛИОТЕКА LU
#------------------------------------------
import LUConst
import LUStrUtils
import LUSupport
#------------------------------------------

#------------------------------------------
# Разбор аргументов
#------------------------------------------
parser = argparse.ArgumentParser(description='Параметры')
parser.add_argument('-P1', type=str, nargs='?', default='', dest='P1', help='P1')
args = parser.parse_args()
print('-P1 =',args.P1)
#------------------------------------------
#------------------------------------------
P1: str = ''
if args.P1 != '':
    P1 = args.P1
#endif
#------------------------------------------

#-------------------------------------------------------------------------------
# CreateConnectio ():
#-------------------------------------------------------------------------------
def CreateConnection ():
    global connection
    global dbCursor
#beginfunction
    print ("CreateConnection ...")
    #-----------------------------------------------
    # Выполним соединение к нашей базе данных:
    #-----------------------------------------------
    connection = oracledb.connect(user='LYR',password='lyr',dsn='localhost/orcl')
    #connection = oracledb.connect(user='ot',password='OT',dsn='localhost/orcl')
    print ("Successfully connected to Oracle Database")
    #-----------------------------------------------
    # Создадим курсор, с помощью которого, посредством передачи запросов
    # будем оперировать данными в нашей таблице:
    #-----------------------------------------------
    dbCursor = connection.cursor ()
#endfunction

#-------------------------------------------------------------------------------
# CREATE_Table ():
#-------------------------------------------------------------------------------
def CREATE_Table ():
#beginfunction
    print ('CREATE_Table posts ...')
    qCREATE_Table = """
    CREATE TABLE posts (
        post_id INT PRIMARY KEY NOT NULL,
        message varchar2(1000),
        publish_date DATE
    )
    """
    dbCursor.execute (qCREATE_Table)
#endfunction

#-------------------------------------------------------------------------------
# DROP_Table ():
#-------------------------------------------------------------------------------
def DROP_Table ():
#beginfunction
    print ('DROP_Table posts ...')
    qDROP_Table = """
    DROP TABLE posts
    """
    dbCursor.execute (qDROP_Table)
#endfunction

#-------------------------------------------------------------------------------
# INSERT_Table ():
#-------------------------------------------------------------------------------
def INSERT_Table ():
#beginfunction
    print ('INSERT_Table posts ...')
    qINSERT_Table = """
    INSERT INTO posts VALUES(10, 'Hey There', '11.11.2016')
    """
    dbCursor.execute (qINSERT_Table)
    # commit your work to database
    connection.commit ()
#endfunction

#-------------------------------------------------------------------------------
# SELECT_Table ():
#-------------------------------------------------------------------------------
def SELECT_Table ():
#beginfunction
    print ('SELECT_Table posts ...')
    qSELECT_Table = """
    SELECT * FROM posts ORDER BY publish_date DESC
    """
    dbCursor.execute (qSELECT_Table)
    #row = dbCursor.fetchone()
    for row in dbCursor:
        print ("Message: ", row [0], row [1], row [2])

    #dbCursor.execute (qSELECT_Table)
    #for row in dbCursor:
    #    print ("Message: ", row.post_id, row.message, row.publish_date)
#endfunction

#------------------------------------------
# main():
#------------------------------------------
def main():
#beginfunction
    CreateConnection ()
    #-----------------------------------------------
    DROP_Table ()
    #-----------------------------------------------
    CREATE_Table ()
    #-----------------------------------------------
    INSERT_Table ()
    #-----------------------------------------------
    SELECT_Table ()
    #-----------------------------------------------
    print ("!!!!!!!!!!")
    connection.close ()
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule















