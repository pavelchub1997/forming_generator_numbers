import sys, class_main_window
from PyQt5 import QtWidgets

def main():

    app = QtWidgets.QApplication(sys.argv)
    window = class_main_window.Main_Window()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()