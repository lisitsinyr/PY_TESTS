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
GDir: str = ''
GMask: str = '*.*'
GDirCount: int = 0
GLevel: int = 0

# -------------------------------------------------------------------------------
# WorkFile (AFile_path)
# -------------------------------------------------------------------------------
def WorkFile (AFullFileName):
    # global Shablon
#beginfunction
    LFileNameSource: str = AFullFileName
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

    # if Shablon == Shablon1:
    #     #Shablon1: str = '{FullFileDir} {FileName} {FileTime} {FileSize}'
    #     message = Shablon.format(FullFileDir=LFullFileName,FileName=LFileName,FileTime=LFileTimeSource,FileSize=LFileSize)
    #     print (message)
    # #endif
    # if Shablon == Shablon2:
    #     #Shablon2: str = '{FileName={FullFileName}|{FullFileDir}|{FileDir}'
    #     message = Shablon.format(FileName=LFileName,FullFileName=LFullFileName,FullFileDir=LFullFileName,FileDir=LFileDir)
    #     print (message)
    # #endif
#endfunction

#-------------------------------------------------------------------------------
# ListFile (ASourcePath, AMask)
#-------------------------------------------------------------------------------
def ListFile (ASourcePath, AMask, _OutFile, _Option, _FuncDir, _FuncFile):
#beginfunction
    """
    if ($OutFile) and (UCase($OutFile) <> "CONSOLE")
        $HandleFile = FreeFileHandle
        $Res = Open ($HandleFile, $OutFile, 1+4)
    #endif
    """

    #LDay = EncodeDate(@Year,@MonthNo,@MDayNo)

    # LFileMask = os.path.join (ASourcePath, '*.*')
    LSourcePath = ASourcePath

    LFiles = os.listdir (LSourcePath)
    LListFile = 0
    for LFileName in LFiles:
        LListFile = LListFile + 1

        LFullFileName: str = os.path.join (ASourcePath, LFileName)
        if os.path.isfile (LFullFileName):
            #Это файл
            #Lstats = os.stat (LFullFileName)
            # LULog.LoggerAPPS_AddLevel (LULog.TEXT, LFullFileName)
            LULog.LoggerAPPS_AddLevel (LULog.TEXT, LFileName)

            WorkFile (LFullFileName)
        #endif
    #endfor
#endfunction

#-------------------------------------------------------------------------------
# ListDir (ASourcePath, AMask)
#-------------------------------------------------------------------------------
def ListDir (ASourcePath, AMask, _OutFile, _Option, _FuncDir, _FuncFile):
    global GLevel
#beginfunction
    global GLevel
    global GDirCount
    GLevel = GLevel + 1
    #------------------------------------------------------------
    # Dir
    #------------------------------------------------------------
    LFullDirName = ASourcePath
    # LULog.LoggerAPPS_AddDebug (LFullDirName)
    LDirName = os.path.basename (ASourcePath)
    LULog.LoggerAPPS_AddDebug (LDirName)
    GDirCount = GDirCount + 1

    """
       # FileCount = ListFile(ASourcePath, AMask, $OutFile, $Option, FuncFile)
       if $Option = 10 or $Option = 11 or $Option = 12
          if ($OutFile) and (UCase($OutFile) <> "CONSOLE")
             $HandleDir = FreeFileHandle
             $Res = Open ($HandleDir, $OutFile, 1+4)
          #endif
          if $OutFile
             if UCase($OutFile) = "CONSOLE"
                ? ASourcePath
             else
                $Res = WriteLine ($HandleDir, ASourcePath+" "+$DirCount+@CRLF)
             #endif
          #endif
          if ($OutFile) and (UCase($OutFile) <> "CONSOLE")
             $Res = Close ($HandleDir)
          #endif
       #endif
    """

    LFiles = os.listdir (ASourcePath)
    for LFile in LFiles:
        # LSourcePath: str = os.sep.join ([ASourcePath, LFile])
        LSourcePath = os.path.join (ASourcePath, LFile)
        #Lstats = os.stat (LSourcePath)
        if os.path.isdir (LSourcePath):
            #Это каталог
            LSourcePath = os.path.join (ASourcePath, LFile)
            # LULog.LoggerAPPS_AddDebug (LSourcePath)
            # LULog.LoggerAPPS_AddLevel (LULog.TEXT, LSourcePath)

            ListFile (LSourcePath, AMask, _OutFile, _Option, _FuncDir, _FuncFile)
            # FileCount = ListFile(LSourcePath, AMask, _OutFile, _Option, _FuncFile)

            #if FuncDir
            #   $s = '$$Res = FuncDir ($$DirCount, $LSourcePath, $FileCount)'
            #   $ResExe = execute ($s)
            ##endif

            #WorkFile(LSourcePath)

            ListDir (LSourcePath, AMask, _OutFile, _Option, _FuncDir, _FuncFile)
        #endif
    #endfor
    GLevel = GLevel - 1
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

    ListDir (GDir, GMask, '', '', '', '')
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
    # LULog.LoggerTOOLS_AddLevel (LULog.TEXT, "Тест")
    # LULog.LoggerTOOLS_AddDebug ("debug")
    # LULog.LoggerTOOLS_AddLevel (logging.DEBUG, "debug")

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    # LPDir = LUParserARG.GetParam ('PDir', "")
    # s = f'Format = {LPDir}'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, LPDir)
    # LPMask = LUParserARG.GetParam ('PMask', "")
    # s = f'PMask = {LPMask}'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, LPMask)

    Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    Lparser.add_argument ('PDir', type = str, default='', help = 'PDir')
    Lparser.add_argument ('PMask', type = str, default='', help = 'PMask')
    # Lparser.add_argument ('-PDir', type = str, nargs = '?', default = '', dest = 'PDir', help = 'PDir')
    # Lparser.add_argument ('-PMask', type = str, nargs = '?', default = '', dest = 'PMask', help = 'PMask')
    Largs = Lparser.parse_args ()
    
    GDir = Largs.PDir
    GMask = Largs.PMask
    GDir = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY'
    GMask = '*.*'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'GDir = {GDir}')
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'GMask = {GMask}')

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
