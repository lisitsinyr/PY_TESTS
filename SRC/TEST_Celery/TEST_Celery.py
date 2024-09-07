"""TEST_Celery.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     LU_PY
     Python (LU)
 Module:
     TEST_Celery.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
from celery import Celery
from celery.schedules import crontab

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
from lyrpy.LUDoc import *

def TEST_Celery ():
    """TEST_Celery"""
#beginfunction
    PrintInfoObject(TEST_Celery)
    PrintInfoObject(Celery)
#endfunction

def TEST_Celery_01 ():
    """TEST_Celery_01"""
#beginfunction
    PrintInfoObject(TEST_Celery_01)

    app = Celery()

    @app.on_after_configure.connect
    def setup_periodic_tasks (sender, **kwargs):
    #beginfunction
        # Calls test('hello') every 5 seconds.
        sender.add_periodic_task (5.0, test.s ('hello'), name = 'add every 5')

        # Calls test('world') every 30 seconds
        sender.add_periodic_task (30.0, test.s ('world'), expires = 10)

        # Executes every Monday morning at 7:30 a.m.
        sender.add_periodic_task (
            crontab (hour = 7, minute = 30, day_of_week = 1),
            test.s ('Happy Mondays!'),
        )
    #endfunction

    @app.task
    def test (arg):
        print (arg)

    @app.task
    def add (x, y):
        z = x + y
        print (z)

    # @app.task
    # def add (x, y):
    #     sleep (10)
    #     return x + y

    app.start()

#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                    r'D:\PROJECTS_LYR\LOGS',
                    'PATTERN_PY_FILEINI.log',
                    'PATTERN_PY_FILEINI_json.log')

    TEST_Celery ()
    TEST_Celery_01 ()

    LULog.STOPLogging ()
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule

