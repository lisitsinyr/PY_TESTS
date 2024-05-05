#=======================================================================================
# TEST_MySQL_PyMySQL.py
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
import pymysql

#------------------------------------------
#БИБЛИОТЕКА LU
#------------------------------------------
import LUConst
import LUStrings
import LUSupport
#------------------------------------------

#------------------------------------------
# Разбор аргументов
#------------------------------------------
print (__name__)
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
    # Выполним соединение к нашей базе данных:
    #-----------------------------------------------
    connection = pymysql.connect (host="ASUS-W10P", user="lyr", password="lyr", db="mysql_test")

    #-----------------------------------------------
    # Создадим курсор, с помощью которого, посредством передачи запросов
    # будем оперировать данными в нашей таблице:
    #-----------------------------------------------
    dbCursor = connection.cursor ()
    #-----------------------------------------------
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
        message TEXT,
        publish_date DATETIME
    );
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
    INSERT INTO posts VALUES(10, 'Hey There', '2016/11/23 18:10:45');
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
    SELECT * FROM posts ORDER BY publish_date DESC;
    """
    dbCursor.execute (qSELECT_Table)
    #row = dbCursor.fetchone()
    for row in dbCursor:
        print ("Message: ", row [0], row [1], row [2])

    #dbCursor.execute (qSELECT_Table)
    #for row in dbCursor:
    #    print ("Message: ", row.post_id, row.message, row.publish_date)
#endfunction

#-------------------------------------------------------------------------------
# SelectTable():
#-------------------------------------------------------------------------------
def SELECT_version():
#beginfunction
    print ('SELECT_version ...')
    #-----------------------------------------------
    # dbCursor.
    #   fetchall() – возвращает число записей в виде упорядоченного списка;
    #   fetchmany(size) – возвращает число записей не более size;
    #   fetchone() – возвращает первую запись
    #-----------------------------------------------
    dbCursor.execute ("select @@version")
    output = dbCursor.fetchall ()
    print (output)

    dbCursor.execute("SELECT @@version")
    #row = dbCursor.fetchone()
    for row in dbCursor:
        print ("version:", row[0])
#endfunction

#------------------------------------------
# main():
#------------------------------------------
def main():
#beginfunction
    CreateConnection()
    #-----------------------------------------------
    SELECT_version()
    #-----------------------------------------------
    DROP_Table()
    #-----------------------------------------------
    CREATE_Table()
    #-----------------------------------------------
    INSERT_Table()
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















