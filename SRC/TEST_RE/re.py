"""HelloWorld.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2025
 Author:
     Lisitsin Y.R.
 Project:
     HelloWorld
     Python (PROJECTS_PY)
 Module:
     HelloWorld.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import re

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU
#------------------------------------------
import lyrpy.LUos as LUos
import lyrpy.LULog as LULog
import lyrpy.LUConst as LUConst
from lyrpy.LUDoc import *

#------------------------------------------
# EXAMPLE_01
#------------------------------------------
def EXAMPLE_01 ():
    """EXAMPLE_01"""
#beginfunction
    PrintInfoObject('---------EXAMPLE_01----------')
    PrintInfoObject(EXAMPLE_01)
    pattern = re.compile('^([0-2]{1}[0-3]{0,1}:[0-5][0-9]{0,1}:[0-5][0-9]{0,1},{0,1})+$')

    # print(pattern.search('0:0:0'))
    # print(pattern.search('00:00:00'))
    # print(pattern.search('000000:0:0'))
    # print(pattern.search('111:2:0'))
    # print(pattern.search('23:0:0'))

    # print(pattern.match('0:0:0'))
    # print(pattern.match('00:00:00,00:00:00'))
    # print(pattern.match('000000:0:0'))
    # print(pattern.match('111:2:0'))
    # print(pattern.match('23:0:0'))

    __FMIN_re = re.compile (
        '^'

        '('
        '('
        '('
        '([0-5]?[0-9]|60)'

        '(-'
        '([0-5]?[0-9]|60)'
        '){0,1}?)|\*)'

        '(,'
        '([0-5]?[0-9]|60)'
        '((-'
        '([0-5]?[0-9]|60)'
        '){0,1}?))*?)'

        '$'
    )
    s = '0'
    print('MIN',__FMIN_re.match(s))
    s = '0,10,20,30,40,50'
    print('MIN',__FMIN_re.match(s))
    s = '0-10,10-20,30-40,40-50,50-60'
    print(s)
    print('MIN',__FMIN_re.match(s))
    s = '60'
    print('MIN',__FMIN_re.match(s))
    s = ''
    print('MIN',__FMIN_re.match(s))
    __FHH_re = re.compile (
        '^(((([0-1]?[0-9]|2[0-4])(-([0-1]?[0-9]|2[0-4])){0,1}?)|\*)(,([0-1]?[0-9]|2[0-4])((-([0-1]?[0-9]|2[0-4])){0,1}?))*?)$')
    s = '0'
    print('HH',__FHH_re.match(s))
    s = '0,1,2,3,4,5,23'
    print('HH',__FHH_re.match(s))
    s = '0-1,1-2,3-4,4-5,5-6'
    print('HH',__FHH_re.match(s))
    s = '23'
    print('HH',__FHH_re.match(s))
    s = ''
    print('HH',__FHH_re.match(s))

    __FDD_re = re.compile (
        '^((('
        '([0-2]?[1-9]|3[0-1])'
        '(-([0-2]?[1-9]|3[0-1])){0,1}?)|\*)(,([0-2]?[1-9]|3[0-1])((-([0-2]?[1-9]|3[0-1])){0,1}?))*?)'
        '$'
    )
    s = '1'
    print('DD',__FDD_re.match(s))
    s = '1,2,3,4,5,23,0'
    print('DD',__FDD_re.match(s))
    s = '1-2,3-4,4-5,5-6,0'
    print('DD',__FDD_re.match(s))
    s = '31'
    print('DD',__FDD_re.match(s))
    s = ''
    print('DD',__FDD_re.match(s))
    s = '0'
    print('DD',__FDD_re.match(s))

    __FDN_re = re.compile (
        '^'
        '('
        '('
        '('
        '([1]?[1-7])'
        '(-'
        '([1]?[1-7])'
        '){0,1}?)|\*)'
        '(,'
        '([1]?[1-7])'
        '('
        '(-'
        '([1]?[1-7])'
        '){0,1}?))*?)'
        '$')
    s = '1'
    print('DN',__FDN_re.match(s))
    s = '1,2,3,4,5,6,7'
    print('DN',__FDN_re.match(s))
    s = '1-2,3-4,4-5,5-6'
    print('DN',__FDN_re.match(s))
    s = '*'
    print('DN',__FDN_re.match(s))
    s = ''
    print('DN',__FDN_re.match(s))
    s = '0'
    print('DN',__FDN_re.match(s))

    __FMM_re = re.compile (
        '^(((([1]?[1-9]|1[0-2])(-([0]?[0-9]|1[0-2])){0,1}?)|\*)(,([0]?[0-9]|1[0-2])((-([0]?[0-9]|1[0-2])){0,1}?))*?)$')
    s = '1'
    print('MM',__FMM_re.match(s))
    s = '1,2,3,4,5,6,7,8,9,10,11,12'
    print('MM',__FMM_re.match(s))
    s = '1-2,3-4,4-5,5-6,1-12'
    print('MM',__FMM_re.match(s))
    s = '12'
    print('MM',__FMM_re.match(s))
    s = '*'
    print('MM',__FMM_re.match(s))
    s = ''
    print('MM',__FMM_re.match(s))
    s = '0'
    print('MM',__FMM_re.match(s))

#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    EXAMPLE_01 ()
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    print(LUos.cHOME)
    main()
#endif

#endmodule
