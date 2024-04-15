"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     PATTERNS_PY
     Python (PROJECTS_PY)
 Module:
     ListDir.py

 =======================================================
"""
#------------------------------------------
#БИБЛИОТЕКИ
#------------------------------------------
import argparse
import datetime
#------------------------------------------
#БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import LUConst
import LUStrUtils
import LUSupport
import LUFileUtils
import LULog

#------------------------------------------
#CONST
#------------------------------------------
GLevel: int = 0
GMask: str = "*.*"
GLog: str = ""
GDir: str = ""
GShablon: str = ""

#------------------------------------------
DirName: str = ""
Shablon: str = ""
Shablon0: str = 'call arjd.bat \"{DirName}\"'
Shablon1: str = "{FullFileDir} {FileName} {FileTime} {FileSize}"
Shablon2: str = "{FileName={FullFileName}|{FullFileDir}|{FileDir}"
#------------------------------------------

#------------------------------------------
# Разбор аргументов
#------------------------------------------
parser = argparse.ArgumentParser(description='Параметры')
parser.add_argument('-Format', type=int, nargs='?', default=-1, dest='Format', help='Номер шаблона')
parser.add_argument('-NLevel', type=int, nargs='?', default=-1, dest='NLevel', help='Уровень')
args = parser.parse_args()
print('-Format =',args.Format)
print('-NLevel =',args.NLevel)
#------------------------------------------
Format: int = 0
if args.Format != -1:
    Format = args.Format
#endif
#------------------------------------------
NLevel: int = 1
if args.NLevel != -1:
    NLevel = args.NLevel
#endif
if NLevel is None:
    NLevel = 0
#endif
#------------------------------------------

#------------------------------------------
# FuncDir ()
#------------------------------------------
# def FuncDir (ADir: os.DirEntry):
def FuncDir (ADir: str):
    """FuncDir"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, ADir.path)
    Lstat = os.stat(ADir)
    # print('stat_name:',Lstat)
    # Lstat = os.stat(AFile.path)
    # print('stat_path:',Lstat)
    # print (GLevel, NLevel)
    LBaseName = os.path.basename (ADir)
    if GShablon == Shablon0:
        message = GShablon.format (DirName = LBaseName)
        print (message)
    #endif
#endfunction

#------------------------------------------
# FuncFile ()
#------------------------------------------
# def FuncFile (AFile: os.DirEntry):
def FuncFile (AFile: str, _Older: int):
    """FuncFile"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, AFile.path)
    Lstat = os.stat(AFile)
    # print('stat_name:',Lstat)
    # Lstat = os.stat(AFile.path)
    # print('stat_path:',Lstat)
    ...
#endfunction

def main():
#beginfunction
    global GDir
    global GLog
    global GShablon

    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI, 'LOG_INIT',
                    'LOGGING_FILEINI.log', 'LOGGING_FILEINI_json.log')

    GDir = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY'
    # GDir = os.getcwd()
    match Format:
        case 1:
            GLog = 'sfile.ini'
            GShablon = Shablon1
        case 2:
            GLog = 'sfile.ini'
            GShablon = Shablon2
        case _:
            GLog = 'sdir.bat'
            GShablon = Shablon0
    #endmatch
    print ('GDir     = '+GDir)
    print ('GMask    = '+GMask)
    print ('GLog     = '+GLog)
    print ('GShablon = '+GShablon)

    print ('Format  = ',Format)
    print ('NLevel  = ',NLevel)

    _OutFile = 'ListDir.txt'
    LMask = '.*'
    LUFileUtils.__ListDir (GDir, LMask, False, '', _OutFile, 0, FuncDir, FuncFile)
#endfunction

#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
