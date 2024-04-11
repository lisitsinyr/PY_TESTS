"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     TESTS_PY
     Python (PROJECTS_PY)
 Module:
     DelFiles.py

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
# FuncDir ()
#------------------------------------------
def FuncDir (ADir: os.DirEntry):
    """FuncDir"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, ADir.path)
    # Lstat = os.stat(AFile.name)
    # print('stat_name:',Lstat)
    # Lstat = os.stat(AFile.path)
    # print('stat_path:',Lstat)
    ...
#endfunction

#------------------------------------------
# FuncFile ()
#------------------------------------------
def FuncFile (AFile: os.DirEntry):
    """FuncFile"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, AFile.path)
    # Lstat = os.stat(AFile.name)
    # print('stat_name:',Lstat)
    # Lstat = os.stat(AFile.path)
    # print('stat_path:',Lstat)
    ...
#endfunction

#------------------------------------------
# TEST_01 ()
#------------------------------------------
def TEST_01 ():
    """TEST_01"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    PrintInfoObject('-----TEST_01----')
    PrintInfoObject(TEST_01)

    _OutFile = 'DirFiles.txt'
    _OutFile = 'CONSOLE'
    LUFile.FileDelete (_OutFile)

    LUFileUtils.DelFiles(GDir, GMask, _OutFile, 100)
#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    global GDir
    global GMask

    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    #----------------------------------------------------------------
    # LPDir = LUParserARG.GetParam ('PDir', "")
    # s = f'Format = {LPDir}'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, LPDir)
    # LPMask = LUParserARG.GetParam ('PMask', "")
    # s = f'PMask = {LPMask}'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, LPMask)
    #----------------------------------------------------------------
    Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    Lparser.add_argument ('PDir', type = str, default='', help = 'PDir')
    Lparser.add_argument ('PMask', type = str, default='', help = 'PMask')
    Lparser.add_argument ('PDays', type = int, default=100, help = 'PDays')
    # Lparser.add_argument ('-PDir', type = str, nargs = '?', default = '', dest = 'PDir', help = 'PDir')
    # Lparser.add_argument ('-PMask', type = str, nargs = '?', default = '', dest = 'PMask', help = 'PMask')
    # Lparser.add_argument ('-PDays', type = int, nargs = '?', default = 100, dest = 'PDays', help = 'PDays')
    # Largs = Lparser.parse_args ()
    # GDir = Largs.PDir
    # GMask = Largs.PMask
    # GDays = Largs.PDays

    GDir = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY'
    GMask = '.*'
    GDays = 100

    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'Pdays = {GDays}')
    print('!!!!')

    TEST_01 ()

    LULog.STOPLogging ()
#endfunction

#------------------------------------------
# ListDir2
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
