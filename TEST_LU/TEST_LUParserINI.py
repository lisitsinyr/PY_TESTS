"""TEST_LUParserINI.py"""
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
     TEST_LUParserINI.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import logging

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
import LUParserINI
from LUDoc import *

def TEST_LUParserINI ():
    """TEST_LUParserINI"""
#beginfunction
    PrintInfoObject('---------TEST_LUParserINI----------')
    PrintInfoObject(TEST_LUParserINI)
    ...
#endfunction

def TEST_TINIFile ():
    """TEST_TINIFile"""
#beginfunction
    PrintInfoObject('---------TEST_TINIFile----------')
    PrintInfoObject(TEST_TINIFile)

    LFileName = 'TEST_LU.ini'
    LINIFile = LUParserINI.TINIFile()
    LINIFile.FileNameINI = LFileName

    LSectionName = 'general 01'
    LOptionName = 'OptionName 01'
    LOptionValue = 'Value 01'
    LINIFile.SetOption(LSectionName, LOptionName, LOptionValue)

    LSectionName = 'general 03'
    LOptionName = 'OptionName 03'
    LOptionValue = 'Value 03'
    LINIFile.SetOption(LSectionName, LOptionName, LOptionValue)

    LSectionName = 'general_02'
    LINIFile.DeleteSection(LSectionName)

    LSectionName = 'general_ERROR'
    LOptionName = 'OptionName 03'
    LOptionValue = LINIFile.GetOption(LSectionName, LOptionName, 'Default')
    LULog.LoggerAPPS.log (LULog.TEXT, LOptionValue)

    LSectionName = 'general 03'
    LOptionName = 'OptionName 03'
    LINIFile.DeleteOption(LSectionName, LOptionName)

    LINIFile.UpdateFileINI()

    for Section in LINIFile.Sections:
        s = f'SectionName={Section}'
        LULog.LoggerAPPS.log (LULog.TEXT, s)

        LINIFile.SectionName = Section
        for Option in LINIFile.Options:
            s = f'    OptionName={Option}'
            LULog.LoggerAPPS.log (LULog.TEXT, s)
        #endfor
    #endfor

    del LINIFile
    ...
#endfunction

def TEST_TINIFile_02 ():
    """TEST_TINIFile_02"""
#beginfunction
    PrintInfoObject('---------TEST_TINIFile_02----------')
    PrintInfoObject(TEST_TINIFile_02)

    LFileName = 'TEST_LU.ini'
    LINIFile = LUParserINI.TINIFile()
    LINIFile.FileNameINI = LFileName

    LSectionName = 'general'
    LOptionName = 'optionname'
    LOptionValue = '!!!!!!!!!!!!!!!!!!'
    LINIFile.SetOption(LSectionName, LOptionName, LOptionValue)
    LINIFile.UpdateFileINI()

    for Section in LINIFile.Sections:
        s = f'SectionName={Section}'
        LULog.LoggerAPPS.log (LULog.TEXT, s)
        LINIFile.SectionName = Section
        for Option in LINIFile.Options:
            s = f'    OptionName={Option}'
            LULog.LoggerAPPS.log (LULog.TEXT, s)
        #endfor
    #endfor
#endfunction

#------------------------------------------
def main ():
#beginfunction
    TEST_LUParserINI ()
    TEST_TINIFile ()
    TEST_TINIFile_02 ()
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

