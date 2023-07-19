#=======================================================================================
# TEST_MSSQL_pyodbc.py
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
    # Создаём строку подключения к нашей базе данных:
    #---------------------------------------------------------
    # Trusted Connection
    # Trusted Connection – указывает на способ подключения пользователей к БД.
    # В случае, если указано значение «yes», для проверки подлинности используется учётная запись Windows,
    # а ключи UID и PWD игнорируются, и наоборот, при выборе значения «no»
    #---------------------------------------------------------

    #---------------------------------------------------------
    # 1. Указать имя источника базы данных (DSN)
    #---------------------------------------------------------
    connectionString = ("DSN=MSSQL_TEST;Trusted_Connection=yes")
    #---------------------------------------------------------

    #---------------------------------------------------------
    # 2. Указать имя драйвера
    #-----------------------------------------------
    #connectionString = ("Driver={SQL Server Native Client 11.0};Server=ASUS-W10P;Database=MSSQL_TEST;Trusted_Connection=yes")
    #connectionString = ("Driver={ODBC Driver 17 for SQL Server};Server=ASUS-W10P;Database=MSSQL_TEST;Trusted_Connection=yes")
    #-----------------------------------------------
    #connectionString = ("DSN=MSSQL_TEST;Trusted_Connection=yes")
    connectionString = ("DSN=MSSQL_TEST;UID=lyr;PWD=lyr")
    print (connectionString.title())

    #-----------------------------------------------
    # Выполним соединение к нашей базе данных:
    #-----------------------------------------------
    connection = pyodbc.connect(connectionString, autocommit=True)

    #-----------------------------------------------
    # Создадим курсор, с помощью которого, посредством передачи запросов
    # будем оперировать данными в нашей таблице:
    #-----------------------------------------------
    # для pymssql
    #     to access field as dictionary use cursor(as_dict=True)
    #     для доступа к полю в качестве словаря используйте курсор (as_dict = True)
    #-----------------------------------------------
    #dbCursor = connection.cursor (as_dict=True)
    #-----------------------------------------------
    dbCursor = connection.cursor()
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
    DROP TABLE posts;
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
    INSERT INTO posts VALUES(10, 'Hey There', '2016-23-11 18:03:40');
    INSERT INTO posts VALUES(11, 'Hey There', '2016-23-11 18:03:40');
    INSERT INTO posts VALUES(12, 'Hey There', '2016-23-11 18:03:40');
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
        #-------------------------------------------------
        # if you pass as_dict=True to cursor
        # print (row['post_id'])
        #-------------------------------------------------
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
    dbCursor.execute("SELECT @@version")
    for row in dbCursor:
        print ("version:", row[0])
#endfunction

#------------------------------------------
# main():
#------------------------------------------
def main():
#beginfunction
    CreateConnection()
    #------------------------------------------
    SELECT_version()
    #-----------------------------------------------
    try:
        DROP_Table()
    except:
        print ("Что-то пошло не так...")
    finally:
        pass
    #-----------------------------------------------
    CREATE_Table()
    #-----------------------------------------------
    INSERT_Table()
    #-----------------------------------------------
    SELECT_Table ()
    #-----------------------------------------------
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















