"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     TESTS_PY
     Python (PROJECTS_PY)
 Module:
     BacFiles.py

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
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\LOG',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
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

    GDir = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU\\TEST_LUFileUtils'
    GDir = 'G:\\WORK\\TEST_QT6_PY'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GDirDest = 'D:\\WORK'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDirDest = {GDirDest}')
    GMask = '.*'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')

    _Option = 0
    _OutFile = 'DirFiles.txt'
    _OutFile = 'CONSOLE'
    # LUFile.FileDelete (_OutFile)

    LUFileUtils.BacFiles(GDir, GMask, True, GDirDest, _OutFile, _Option)

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
