#=======================================================================================
# TEST_ScanDir.py
#=======================================================================================

#------------------------------------------
#  БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys

from os.path import join, getsize

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import argparse
import datetime
from colorama import Fore, Back, Style

#------------------------------------------
# БИБЛИОТЕКА LU
#------------------------------------------
import LUConst
#import LUStrings
import LUStrUtils
import LUSupport
#------------------------------------------

print ('os.name->', os.name)  # ответ: nt
print ("os.environ['PYTHONPATH']->", os.environ ['PYTHONPATH'])
print ("sys.path->", sys.path)

#------------------------------------------
# 
#------------------------------------------
parser = argparse.ArgumentParser(description='Параметры')
parser.add_argument('-P1', type=str, nargs='?', default='', dest='P1', help='P1')
args = parser.parse_args()
print('-P1 = ',args.P1)
#------------------------------------------
P1 = ''
if args.P1 != '':
    P1 = args.P1
#endif
#------------------------------------------

#-------------------------------------------------------------------------------
# TEST_02_01 (APath: str):
#-------------------------------------------------------------------------------
def TEST_02_01 (APath: str):
#beginfunction
    print ("Begin TEST_02_01")
    with os.scandir(APath) as it:
        for Lentry in it:
            if not Lentry.name.startswith('.') and Lentry.is_file():
                print('File=',Lentry.name)
            #endif
        #endfor
    #endwith
    print ("End TEST_02_01")
#endfunction

#-------------------------------------------------------------------------------
# TEST_02_02 (APath: str):
# Delete everything reachable from the directory named in "top",
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
#-------------------------------------------------------------------------------
def TEST_02_02 (APath: str):
#beginfunction
    print ("="*40)
    print ("Begin TEST_02_02")
    print (APath)
    os.system('color')
    for DirPath, DirNames, FileNames in os.walk(APath, topdown=False):
        print (DirPath)
        if len (FileNames) == 0:
            print ('    РљР°С‚Р°Р»РѕРіРѕРІ РЅРµС‚.')
        else:
            for name in DirNames:
                s = os.path.join(DirPath, name)
                #os.rmdir(s)
                print (Style.BRIGHT,
                    Fore.LIGHTWHITE_EX
                       ,Back.LIGHTBLACK_EX
                       ,
                       s,Style.RESET_ALL)
            #endfor
        #endif
        if len (FileNames) == 0:
            print ('    Р¤Р°Р№Р»РѕРІ РЅРµС‚.')
        else:
            for name in FileNames:
                s = os.path.join(DirPath, name)
                #os.remove(s)
                print ('    ',s)
            #endfor
        #endif
    #endfor
    print ("End TEST_02_02")
#endfunction

#-------------------------------------------------------------------------------
# TEST_02_03 (APath: str):
#-------------------------------------------------------------------------------
def TEST_02_03 (APath: str):
#beginfunction
    print ("="*40)
    print ("Begin TEST_02_03")
    for DirPath, DirNames, FileNames in os.walk(APath):
        print(DirPath, "consumes", end=" ")
        print(sum(getsize(join(DirPath, name)) for name in FileNames), end=" ")
        print("bytes in", len(FileNames), "non-directory files")
        if 'CVS' in DirNames:
            #DirNames.remove('CVS')  # don't visit CVS directories
            print ('CVS')
        #endif
    #endfor
    print ("End TEST_02_03")
#endfunction

#-------------------------------------------------------------------------------
# TEST_02_04 (AFileName: str):
#-------------------------------------------------------------------------------
def TEST_02_04 (AFileName: str):
#beginfunction
    print ("Begin TEST_02_04")
    #statinfo = os.stat(AFileName)
    #os.stat_result(st_mode=33188, st_ino=7876932, st_dev=234881026,
    #   st_nlink=1, st_uid=501, st_gid=501, st_size=264, st_atime=1297230295,
    #    st_mtime=1297230027, st_ctime=1297230027)
    #statinfo.st_size
    print ("End TEST_02_04")
#endfunction

#------------------------------------------
# main():
#------------------------------------------
def main():
#beginfunction
    #TEST_02_01 ('D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY')
    TEST_02_02 ("D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY")
    #TEST_02_03 ("D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY")
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
#----------------------------------------------------------------------------
