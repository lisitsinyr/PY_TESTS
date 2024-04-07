"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     PATTERNS_PY
     Python (PROJECTS_PY)
 Module:
     TEST_LULog_START.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys
import time
import datetime

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
# TEST_01 ()
#------------------------------------------
def TEST_01 ():
    """TEST_"""
#beginfunction
    print (sys._getframe (0).f_code.co_name, '...')
    # print (inspect.currentframe().f_code.co_name, '...')
    # print (inspect.stack () [0] [3], '...')
    # print (traceback.extract_stack () [-1].name, '...')
    PrintInfoObject('-----TEST_01----')
    PrintInfoObject(TEST_01)
#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')
    LULog.LoggerTOOLS_AddLevel (LULog.TEXT, "Тест")
    TEST_01 ()
    LULog.STOPLogging ()

    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslCONFIG, 'LOG_CONFIG',
                        'LOGGING_FILECONFIG.log','LOGGING_FILECONFIG_json.log')
    LULog.LoggerTOOLS_AddLevel (LULog.TEXT, "Тест")
    TEST_01 ()
    LULog.STOPLogging ()

    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslYAML, 'LOG_YAML',
                        'LOGGING_FILEYAML.log','LOGGING_FILEYAML_json.log')
    LULog.LoggerTOOLS_AddLevel (LULog.TEXT, "Тест")
    TEST_01 ()
    LULog.STOPLogging ()

#endfunction

#------------------------------------------
# PATTERNS_PY
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
