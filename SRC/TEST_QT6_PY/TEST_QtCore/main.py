# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PySide6.QtCore

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test_qt6():
    # Prints PySide6 version
    print (PySide6.__version__)

    # Prints the Qt version used to compile PySide6
    print (PySide6.QtCore.__version__)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')

    test_qt6()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




