#=======================================================================================
# TEST_ORACLE_pyodbc.py
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
import pyodbc

#------------------------------------------
#БИБЛИОТЕКА LU
#------------------------------------------
import LUConst
import LUStrUtils
import LUSupport
#------------------------------------------

print (__name__)
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


#------------------------------------------
# CreateConnection():
#------------------------------------------
def CreateConnection():
    global connection
    global dbCursor
#beginfunction
    print ('CreateConnection ...')
    #-----------------------------------------------
    # Создаём строку подключения к нашей базе данных:
    #---------------------------------------------------------
    # 2. Указать имя драйвера
    #-----------------------------------------------
    connectionString = ("Driver={ODBC Driver 17 for SQL Server};Server=ASUS-W10P;Database=MSSQL_TEST;Trusted_Connection=yes")
    connectionString = ("Driver={Oracle in OraDB19Home1};DBQ=ORCL;Uid=ot;Pwd=OT")
    #-----------------------------------------------
    connectionString = ("DSN=ORCL;Uid=lyr;Pwd=lyr")
    print (connectionString.title())
    #-----------------------------------------------
    # Выполним соединение к нашей базе данных:
    #-----------------------------------------------
    connection = pyodbc.connect(connectionString, autocommit=True)
    #-----------------------------------------------
    # Создадим курсор, с помощью которого, посредством передачи запросов
    # будем оперировать данными в нашей таблице:
    #-----------------------------------------------
    dbCursor = connection.cursor()
#endfunction

#-------------------------------------------------------------------------------
# CreateTable ():
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
# DropTable ():
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
# InsertTable ():
#-------------------------------------------------------------------------------
def INSERT_Table ():
#beginfunction
    print ('INSERT_Table posts ...')
    qINSERT_Table = """
    INSERT INTO posts VALUES(10, 'Hey There', '23.11.2016');
    """
    dbCursor.execute (qINSERT_Table)
    # commit your work to database
    connection.commit ()
#endfunction

#-------------------------------------------------------------------------------
# SelectTable():
#-------------------------------------------------------------------------------
def SELECT_Table():
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















