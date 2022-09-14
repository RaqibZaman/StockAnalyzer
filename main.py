
import sys
# from UI.gen import mainwindow
from UI.win.mainwindow import MainWindow


print("this is outside of main")

if __name__ == '__main__':
    print("this is inside of main")
    MainWindow()
    print("after calling MainWindow")
    sys.exit(0)
