"""TEST_LU.py"""
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
     TEST_LU.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU
#------------------------------------------
import lyrpy.LUConst as LUConst
import lyrpy.LUos as LUos
import lyrpy.LULog as LULog
import lyrpy.LUDoc as LUDoc

def TEST_01 ():
    """TEST_"""
#beginfunction
    LUDoc.PrintInfoObject('-----TEST_01----')
    LUDoc.PrintInfoObject(TEST_01)
#endfunction

#------------------------------------------
def main ():
#beginfunction
    if LUos.GOSInfo.system == 'Windows':
        LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI, 'LOG', 'LOGGING_FILEINI.log', 'LOGGING_FILEINI_json.log')
    #endif
    if LUos.GOSInfo.system == 'Linux':
        LULog.STARTLogging (LULog.TTypeSETUPLOG.tslCONFIG, 'LOG', 'LOGGING_FILEINI.log', 'LOGGING_FILEINI_json.log')
        # raise 'Linux не поддерживается'
    #endif

    TEST_01 ()

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
