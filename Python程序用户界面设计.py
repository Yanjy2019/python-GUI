#python用户图形界面编程实现
import sys  #简单用户图形界面实现
from PyQt5.QtWidgets import  QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon
import sys

app=QApplication(sys.argv)   #sys.argv是一组命令行参数的列表
w=QWidget()              #QWidget控件是一个用户界面的基本控件，这里是一个窗口（window）
w.resize(500,800)        #窗口的大小设置，宽和高
w.move(900,300)    #修改控件位置的方法
w.setWindowTitle("大数据与数据挖掘")     #窗口添加标题
w.setWindowIcon(QIcon("rose-1.jpg"))      #设置标题图标
w.show()
sys.exit(app.exec())  #关闭界面窗口
