"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     PATTERNS_PY
     Python (PROJECTS_PY)
 Module:
     ListDir2.py

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
#import LUFileUtils
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
Level: int = 0
Mask: str = "*.*"
Log: str = ""
#------------------------------------------
DirName: str = ""
Shablon: str = ""
Shablon0: str = 'call arjd.bat \"{DirName}\"'
Shablon1: str = "{FullFileDir} {FileName} {FileTime} {FileSize}"
Shablon2: str = "{FileName={FullFileName}|{FullFileDir}|{FileDir}"
#------------------------------------------
Format: int = 0
#------------------------------------------
NLevel: int = 1
#------------------------------------------

# -------------------------------------------------------------------------------
# WorkFile (AFile_path)
# -------------------------------------------------------------------------------
def WorkFile (AFile_path):
    global Shablon
#beginfunction
    LFileNameSource: str = AFile_path
    LFullFileName: str = LFileNameSource
    LFileName: str = os.path.basename(LFullFileName)
    LFileSize: int = os.path.getsize(LFullFileName)
    LFileDir: str = os.path.dirname(LFullFileName)

    #-------------------------------------------------------------------------
    #LFileTimeSource = GetFileTime(LFileNameSource)
    #-------------------------------------------------------------------------
    #file modification
    LFileTimeSource = os.path.getmtime(LFileNameSource)
    #convert timestamp into DateTime object
    LFileTimeSource = datetime.datetime.fromtimestamp(LFileTimeSource)
    #file creation
    LFileTimeSource = os.path.getctime(LFileNameSource)
    #convert creation timestamp into DateTime object
    LFileTimeSource = datetime.datetime.fromtimestamp(LFileTimeSource)

    #-------------------------------------------------------------------------
    if Shablon == Shablon1:
        #Shablon1: str = '{FullFileDir} {FileName} {FileTime} {FileSize}'
        message = Shablon.format(FullFileDir=LFullFileName,FileName=LFileName,FileTime=LFileTimeSource,FileSize=LFileSize)
        print (message)
    #endif
    if Shablon == Shablon2:
        #Shablon2: str = '{FileName={FullFileName}|{FullFileDir}|{FileDir}'
        message = Shablon.format(FileName=LFileName,FullFileName=LFullFileName,FullFileDir=LFullFileName,FileDir=LFileDir)
        print (message)
    #endif
#endfunction

#-------------------------------------------------------------------------------
# ListFile (ASourcePath, AMask)
#-------------------------------------------------------------------------------
def ListFile (ASourcePath, AMask):
#beginfunction
    # LFiles: LListFiles [str] = os.listdir (ASourcePath)
    LFiles = os.listdir (ASourcePath)
    for LFile in LFiles:
        LSourcePath = os.sep.join ([ASourcePath, LFile])
        if os.path.isfile (LSourcePath):
            #Это файл
            #Lstats = os.stat (LSourcePath)
            WorkFile (LSourcePath)
        #endif
    #endfor
#endfunction

#-------------------------------------------------------------------------------
# ListDir (ASourcePath, AMask)
#-------------------------------------------------------------------------------
def ListDir (ASourcePath, AMask):
    global Level
#beginfunction
    Level = Level + 1
    #------------------------------------------------------------
    # Dir
    #------------------------------------------------------------
    #DirName = GetFileName(ASourcePath)
    LDirName = os.path.basename (ASourcePath)
    LFullDirName = ASourcePath
    if Level > NLevel:
        if Shablon == Shablon0:
            message = Shablon.format (DirName=LDirName)
            print (1,message)
        #endif
    #endif
    # LFiles: LListFiles [str] = os.listdir (ASourcePath)
    LFiles = os.listdir (ASourcePath)
    for LFile in LFiles:
        LSourcePath = os.sep.join ([ASourcePath, LFile])
        #Lstats = os.stat (LSourcePath)
        if os.path.isdir (LSourcePath):
            #Это каталог
            ListFile (LSourcePath, AMask)
            #WorkFile(LSourcePath)
            #--------------------------------------------------------
            #if Shablon == Shablon0:
            #    message = Shablon.format(DirName=LFile)
            #    print(2,message)
            ##endif
            #--------------------------------------------------------
            if NLevel >= Level:
                ListDir (LSourcePath, AMask)
            #endif
        #endif
    #endfor
    Level = Level - 1
#endfunction

#------------------------------------------
# TEST_01 ()
#------------------------------------------
def TEST_01 ():
    """TEST_"""
#beginfunction
    print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    PrintInfoObject('-----TEST_01----')
    PrintInfoObject(TEST_01)

    global Log
    global Shablon
    Dir = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY'
    match Format:
        case 1:
            Log = 'sfile.ini'
            Shablon = Shablon1
        case 2:
            Log = 'sfile.ini'
            Shablon = Shablon2
        case _:
            Log = 'sdir.bat'
            Shablon = Shablon0
    #endmatch
    print ('Log     = ' + Log)
    print ('Dir     = ' + Dir)
    print ('Format  = ', Format)
    print ('NLevel  = ', NLevel)
    print ('Mask    = ' + Mask)
    print ('Shablon = ' + Shablon)
    ListDir (Dir, Mask)
#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')
    # LULog.LoggerTOOLS_AddLevel (LULog.TEXT, "Тест")
    # LULog.LoggerTOOLS_AddDebug ("debug")
    # LULog.LoggerTOOLS_AddLevel (logging.DEBUG, "debug")

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    LFormat = LUParserARG.GetParam ('Format', "")
    s = f'Format = {LFormat}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, LFormat)
    LNLevel = LUParserARG.GetParam ('NLevel', "")
    s = f'NLevel = {LNLevel}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, LNLevel)

    # Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    # Lparser.add_argument ('-Format', type = int, nargs = '?', default = -1, dest = 'Format', help = 'Format')
    # Lparser.add_argument ('-NLevel', type = int, nargs = '?', default = -1, dest = 'NLevel', help = 'NLevel')
    # Largs = Lparser.parse_args ()
    # LFormat = Largs.Format
    # s = f'Format = {LFormat}'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    # LNLevel = Largs.NLevel
    # s = f'NLevel = {LNLevel}'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

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
