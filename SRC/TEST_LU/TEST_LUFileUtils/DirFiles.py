"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     TESTS_PY
     Python (PROJECTS_PY)
 Module:
     DirFiles.py

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
import stat
import platform

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
import LUErrors
import LUFile
import LUFileUtils
import LULog
#import LUNetwork
#import LUNumUtils
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
#import LUVersion
import LUYouTube

#------------------------------------------
#CONST
#------------------------------------------

#------------------------------------------
# FuncDir ()
#------------------------------------------
def FuncDir (ADir: str, APathDest: str):
    """FuncDir"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    Lstat = os.stat(ADir)
    LAttr = LUFile.GetFileAttr (ADir)
    LDirSize = LUFile.GetDirectoryTreeSize (ADir)
    LDirDateTime = LUFile.GetDirDateTime (ADir)
    s = f'{LDirDateTime[2]:%d.%m.%Y  %H:%M} {LDirDateTime[3]:%d.%m.%Y  %H:%M} {LDirSize:d}'
    LULog.LoggerTOOLS_AddLevel (LULog.TEXT, s)
#endfunction

#------------------------------------------
# FuncFile ()
#------------------------------------------
def FuncFile (AFile: str, APathDest: str):
    """FuncFile"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    Lstat = os.stat(AFile)
    LAttr = LUFile.GetFileAttr(AFile)
    # Lflags = stat.FILE_ATTRIBUTE_SYSTEM | stat.FILE_ATTRIBUTE_HIDDEN | stat.FILE_ATTRIBUTE_READONLY
    # LUFile.SetFileAttr (AFile, Lflags, True)
    LFileSize = LUFile.GetFileSize (AFile)
    LFileDateTime = LUFile.GetFileDateTime (AFile)
    s = f'{LFileDateTime[2]:%d.%m.%Y  %H:%M} {LFileDateTime[2]:%d.%m.%Y  %H:%M} {LFileSize:d}'
    LULog.LoggerTOOLS_AddLevel (LULog.TEXT, s)
#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')

    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\LOG',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    PrintInfoObject('-----main----')
    PrintInfoObject(main)

    global GDir
    global GMask

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    #----------------------------------------------------------------
    GDir = LUParserARG.GetParam ('PDir', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GMask = LUParserARG.GetParam ('PMask', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    Lparser.add_argument ('PDir', type = str, default='', help = 'PDir')
    Lparser.add_argument ('PMask', type = str, default='', help = 'PMask')
    # Lparser.add_argument ('-PDir', type = str, nargs = '?', default = '', dest = 'PDir', help = 'PDir')
    # Lparser.add_argument ('-PMask', type = str, nargs = '?', default = '', dest = 'PMask', help = 'PMask')
    Largs = Lparser.parse_args ()
    GDir = Largs.PDir
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GMask = Largs.PMask
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    #----------------------------------------------------------------

    # GDir = r'D:\WORK\!!HISTORY'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    # GMask = '.*'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')

    _Option = 1
    _OutFile = 'DirFiles.txt'
    _OutFile = 'CONSOLE'
    # LUFile.FileDelete (_OutFile)

    LULog.LoggerTOOLS.setLevel(logging.INFO)
    LULog.LoggerTOOLS.setLevel(logging.DEBUG)

    LUFileUtils.DirFiles(GDir, GMask, True, _OutFile, _Option, FuncDir, FuncFile)

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
