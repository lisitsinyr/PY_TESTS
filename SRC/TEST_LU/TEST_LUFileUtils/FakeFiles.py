"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     TESTS_PY
     Python (PROJECTS_PY)
 Module:
     FakeFiles.py

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
import LUErrors
import LUFile
import LUFileUtils
import LULog
import LUObjects
import LUObjectsYT
import LUos
import LUParserARG
import LUParserINI
import LUProc
import LUQThread
import LUQTimer
import LUSheduler
import LUStrDecode
import LUStrUtils
import LUSupport
import LUsys
import LUThread
import LUYouTube
import LUDoc

if platform.system() == 'Windows':
    import LUNetwork
    import LUNumUtils
    import LUTimer
    import LUVersion
    import LUParserREG
#endif

#------------------------------------------
#CONST
#------------------------------------------

#------------------------------------------
# FuncDir ()
#------------------------------------------
def FuncDir (ADir: str):
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
def FuncFile (AFile: str):
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
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\LOG',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    LUDoc.PrintInfoObject('-----main----')
    LUDoc.PrintInfoObject(main)

    global GDir
    global GMask

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    #----------------------------------------------------------------
    GDir = LUParserARG.GetParam ('PDir', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    Lparser.add_argument ('PDir', type = str, default='', help = 'PDir')
    # Lparser.add_argument ('-PDir', type = str, nargs = '?', default = '', dest = 'PDir', help = 'PDir')
    Largs = Lparser.parse_args ()
    GDir = Largs.PDir
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    #----------------------------------------------------------------

    # GDir = r'D:\WORK\!!HISTORY'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')

    _Option = 1
    _OutFile = 'FakeFiles.txt'
    _OutFile = 'CONSOLE'
    # LUFile.FileDelete (_OutFile)

    LULog.LoggerTOOLS.setLevel(logging.INFO)
    LULog.LoggerTOOLS.setLevel(logging.DEBUG)

    LDir = os.path.join (GDir, 'FAKE')
    LUFile.ForceDirectories (LDir)

    LUFileUtils.FakeFiles(LDir, _OutFile, _Option, FuncDir, FuncFile)

    if LUFile.DirectoryExists(LDir):
        # LUFile.DeleteDirectoryTree(LDir)
        # LUFile.DirectoryClear (LDir)
        ...
    #endif

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
