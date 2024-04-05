"""TEST_LUos.py"""
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
     TEST_LUos.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
# import logging

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pandas

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
import LULog
import LUConst
from LUDoc import *
import LUos

def TEST_LUos ():
    """TEST_LUos"""
#beginfunction
    PrintInfoObject('---------TEST_LUos----------')
    PrintInfoObject(TEST_LUos)
    s = 'os.name->',os.name
    LULog.LoggerAPPSAdd (LULog.TEXT, s)
    s = "os.environ['PYTHONPATH']->", os.environ['PYTHONPATH']
    LULog.LoggerAPPSAdd (LULog.TEXT, s)
    ...
#endfunction

def TEST_GetEnvVar ():
    """TEST_GetEnvVar"""
#beginfunction
    PrintInfoObject('---------TEST_GetEnvVar----------')
    PrintInfoObject(TEST_GetEnvVar)

    s = f'LUos.cHOME={LUos.GetEnvVar (LUos.cHOME)}'
    LULog.LoggerAPPSAdd (LULog.TEXT, s)
    s = f'LUos.cWINDIR={LUos.GetEnvVar (LUos.cWINDIR)}'
    LULog.LoggerAPPSAdd (LULog.TEXT, s)
#endfunction

def TEST_SetEnvVar ():
    """TEST_SetEnvVar"""
#beginfunction
    PrintInfoObject('---------TEST_SetEnvVar----------')
    PrintInfoObject(TEST_SetEnvVar)

    LUos.SetEnvVar(LUos.cTEST,'ValueTEST')
    s = LUos.GetEnvVar (LUos.cTEST)
    LULog.LoggerAPPSAdd (LULog.TEXT, f'{LUos.cTEST}={s}')
    ...
#endfunction

def TEST_TFolders ():
    """TEST_TFolders"""
#beginfunction
    PrintInfoObject('---------TEST_TFolders----------')
    PrintInfoObject(TEST_TFolders)

    LULog.PrintHandlers (LULog.LoggerAPPS)
    LULog.LoggerAPPSAdd_debug('LULogger.debug')
    LTFolders = LUos.TFolders()
    s = f'LTFolders.cuDesktop={LTFolders.cuDesktop}'
    LULog.LoggerAPPSAdd (LULog.TEXT, s)
    LULog.LoggerAPPSAdd_info (s)
    ...
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging ('LOG', 'LOGGING_FILEINI.log', 'LOGGING_FILEINI_json.log')

    TEST_LUos ()
    TEST_GetEnvVar ()
    TEST_SetEnvVar ()

    TEST_TFolders ()
    ...
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule

