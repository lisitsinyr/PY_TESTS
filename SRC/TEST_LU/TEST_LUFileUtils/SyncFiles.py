"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     TESTS_PY
     Python (PROJECTS_PY)
 Module:
     SyncFiles.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys
import time
import datetime
import logging
import argparse

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pandas

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import LUConsole
import LUConst
import LUDateTime
import LUDecotators
import LUDict
from LUDoc import *
#import LUDoc
import LUErrors
import LUFile
import LUFileUtils
import LULog
import LUNetwork
import LUNumUtils
import LUObjects
import LUObjectsYT
import LUos
import LUParserARG
import LUParserINI
#import LUParserREG
import LUProc
import LUQThread
import LUQTimer
import LUSheduler
import LUStrDecode
import LUStrUtils
import LUSupport
import LUsys
import LUThread
#import LUTimer
import LUVersion
import LUYouTube

#------------------------------------------
#CONST
#------------------------------------------

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')

    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    PrintInfoObject('-----main----')
    PrintInfoObject(main)

    global GDir
    global GDirDest
    global GMask

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    #----------------------------------------------------------------
    GDir = LUParserARG.GetParam ('PDir', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GDirDest = LUParserARG.GetParam ('PDirDest', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDirDest = {GDirDest}')
    GMask = LUParserARG.GetParam ('PMask', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    Lparser.add_argument ('PDir', type = str, default='', help = 'PDir')
    Lparser.add_argument ('PDirDest', type = str, default='', help = 'PDirDest')
    Lparser.add_argument ('PMask', type = str, default='', help = 'PMask')
    # Lparser.add_argument ('-PDir', type = str, nargs = '?', default = '', dest = 'PDir', help = 'PDir')
    # Lparser.add_argument ('-PDirDest', type = str, nargs = '?', default = '', dest = 'PDirDest', help = 'PDirDest')
    # Lparser.add_argument ('-PMask', type = str, nargs = '?', default = '', dest = 'PMask', help = 'PMask')
    Largs = Lparser.parse_args ()
    GDir = Largs.PDir
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GDirDest = Largs.PDirDest
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDirDest}')
    GMask = Largs.PMask
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    #----------------------------------------------------------------

    GDir = r'D:\WORK\08_SUBD\01_ORACLE\БИБЛИОТЕКИ'
    GDir = r'D:\WORK\08_SUBD\01_ORACLE\PROJECTS\oracle-db-examples'
    GDir = r'D:\WORK\08_SUBD'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GDirDest = r'D:\WORK\SYNC\08_SUBD'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDirDest = {GDirDest}')
    GMask = '.*'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')

    _Option = 0
    _OutFile = 'SyncFiles.txt'
    _OutFile = 'CONSOLE'
    # LUFile.FileDelete (_OutFile)

    LULog.LoggerTOOLS.setLevel(logging.INFO)
    # LULog.LoggerTOOLS.setLevel(logging.DEBUG)

    LUFileUtils.SyncFiles(GDir, GMask, GDirDest, _OutFile, _Option)

    LULog.STOPLogging ()
#endfunction

#------------------------------------------
# DirFiles
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
