# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fpga_displayui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PaintBoard import PaintBoard
from serial import Serial,PARITY_NONE,STOPBITS_ONE,SEVENBITS
import serial.tools.list_ports
from time import time


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 画板
        self.board = PaintBoard(self.centralwidget)
        self.board.setEnabled(True)
        self.board.setGeometry(QtCore.QRect(200, 10, 500, 360))

        self.board.setObjectName("widget")

        # UI初始化
        # 连接状态提示
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)

        # 缩放比例调整
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit.setObjectName("lineEdit")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(110, 110, 62, 22))
        self.doubleSpinBox.setMinimum(10.0)
        self.doubleSpinBox.setMaximum(90.0)
        self.doubleSpinBox.setProperty("value", 50.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.valueChanged.connect(self.changerate)

        # # 纵坐标调整
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(20, 90, 81, 21))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.label.setFont(font)
        # self.label.setObjectName("label")
        # self.lineEdit.setObjectName("lineEdit")
        # self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        # self.doubleSpinBox.setGeometry(QtCore.QRect(110, 90, 62, 22))
        # self.doubleSpinBox.setMinimum(16.0)
        # self.doubleSpinBox.setProperty("value", 32.0)
        # self.doubleSpinBox.setObjectName("doubleSpinBox")
        #
        # # 横坐标调整
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(20, 130, 81, 21))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.label_2.setFont(font)
        # self.label_2.setObjectName("label_2")
        # self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        # self.doubleSpinBox_2.setGeometry(QtCore.QRect(110, 130, 62, 22))
        # self.doubleSpinBox_2.setMinimum(50.0)
        # self.doubleSpinBox_2.setMaximum(99.0)
        # self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")

        # 峰峰值标签
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 200, 71, 16))
        self.label_4.setObjectName("label_4")

        # 频率标签
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 230, 71, 16))
        self.label_6.setObjectName("label_6")

        # 控制按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 300, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.running = False
        self.pushButton.clicked.connect(self.switch)

        # 菜单
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        # 二级菜单标签
        # 选择串口标签
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)

        # 选择串口
        self.actionCOM1 = QtWidgets.QAction(MainWindow)
        self.actionCOM1.setObjectName("actionCOM1")
        self.actionCOM1.triggered.connect(lambda: self.selectCOM(0))
        self.actionCOM2 = QtWidgets.QAction(MainWindow)
        self.actionCOM2.setObjectName("actionCOM2")
        self.actionCOM2.triggered.connect(lambda: self.selectCOM(1))
        self.actionCOM3 = QtWidgets.QAction(MainWindow)
        self.actionCOM3.setObjectName("actionCOM3")
        self.actionCOM3.triggered.connect(lambda: self.selectCOM(2))
        self.menu_2.addAction(self.actionCOM1)
        self.menu_2.addAction(self.actionCOM2)
        self.menu_2.addAction(self.actionCOM3)
        self.menu.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())



        # 定时器接收数据
        self.pretime = time()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.data_receive)

        self.retranslateUi(MainWindow)
        self.initdata()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        # 文字初始化
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FPGA_Display"))
        self.lineEdit.setText(_translate("MainWindow", "端口未选择"))
        self.label.setText(_translate("MainWindow", "缩放比例"))
        # self.label.setText(_translate("MainWindow", "纵坐标大小"))
        # self.label_2.setText(_translate("MainWindow", "横坐标大小"))
        self.label_3.setText(_translate("MainWindow", "峰峰值:"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "  频率:"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "选择端口"))
        self.actionCOM1.setText(_translate("MainWindow", "COM1"))
        self.actionCOM2.setText(_translate("MainWindow", "COM2"))
        self.actionCOM3.setText(_translate("MainWindow", "COM3"))

    def initdata(self):
        # 初始化串行端口
        # self.currentCOM=0
        # self.COMs=[serial.Serial("COM3",9600,timeout=0.5) for i in range(1,3)]
        # 获取可用的端口
        port_list = list(serial.tools.list_ports.comports())
        self.port_num = len(port_list)
        for i in port_list:
            print(i.device)
        self.currentCOM_index = -1
        self.currentCOM = None
        self.COMs = []

        if self.port_num == 0:
            print("没有可用端口")
            self.pushButton.setEnabled(False)
            self.actionCOM1.setEnabled(False)
            self.actionCOM2.setEnabled(False)
            self.actionCOM3.setEnabled(False)
        else:
            # 有可用的端口
            # 初始化缓存区,缓冲区定义为MAXBUFF字节
            self.MAXBUFF=100
            self.databuff = []
            self.buffremain = self.MAXBUFF

            # 初始化端口
            self.lineEdit.setText("端口COM1已打开")
            self.currentCOM_index = 0
            self.COMs = [Serial(port=seri.device, baudrate=9600,
                                       timeout=0.5,parity=PARITY_NONE,
                                       stopbits = STOPBITS_ONE,bytesize=SEVENBITS)
                         for seri in port_list]
            self.currentCOM = self.COMs[0]

            if self.port_num == 1:
                self.actionCOM2.setEnabled(False)
                self.actionCOM3.setEnabled(False)
            elif self.port_num == 2:
                self.actionCOM3.setEnabled(False)

    # 改变缩放比例
    def changerate(self):
        self.MAXBUFF = int(self.doubleSpinBox.value()*2)
        # self.buffremain = self.MAXBUFF
        # self.databuff = []

    # 打开串口
    def port_open(self):
        # self.currentCOM.port = self.s1__box_2.currentText()
        # self.currentCOM.baudrate = int(self.s1__box_3.currentText())
        # self.currentCOM.bytesize = int(self.s1__box_4.currentText())
        # self.currentCOM.stopbits = int(self.s1__box_6.currentText())
        # self.currentCOM.parity = self.s1__box_5.currentText()
        # self.currentCOM.baudrate=9600
        # self.currentCOM.bytesize=8
        # self.currentCOM.stopbits=1
        # self.currentCOM.parity="N"


        try:
            self.currentCOM.open()
        except (Exception, BaseException) as e:
            print(e)
            print( "Port Error", "此串口不能被打开！")

        # 打开串口接收定时器，周期为2ms
        self.timer.start(10)

        return self.currentCOM.isOpen()

    # 关闭串口
    def port_close(self):
        self.timer.stop()
        try:
            self.currentCOM.close()
        except:
            pass
        return not self.currentCOM.isOpen()

    # 在菜单中选择端口
    def selectCOM(self, n):
        self.currentCOM_index = n if (n < self.port_num) else 0
        self.currentCOM = self.COMs[n]
        self.lineEdit.setText("端口COM%d已打开" % (n + 1))
        print("OK", n)

    # 运行/停止运行按钮
    def switch(self):
        # 尝试进行切换
        result=False
        if self.running:
            result=self.port_close()
        else:
            result=self.port_open()

        # 根据切换结果进行设置
        if result:
            self.running = not self.running
            if self.running:
                self.pushButton.setText("暂停")
            else:
                self.pushButton.setText("开始")
        else:
            print("false")

    # 接收数据
    def data_receive(self):
        try:
            # 获取缓存区中的个数
            num = self.currentCOM.inWaiting()
            num = num if num < self.buffremain else self.buffremain
        except (Exception, BaseException) as e:
            print(e)
            exit(-1)
        if num > 0:
            data = self.currentCOM.read(num)
            num = len(data)
            print(data)


            # 统计接收字符的数量
            self.buffremain -= num
            # 添加数据到缓冲区中
            self.databuff.extend(data)
        else:
            pass

        if self.buffremain <= 0:
            self.refresh()

    # 缓冲区满，触发刷新
    def refresh(self):
        fre=0
        mid = (max(self.databuff)+min(self.databuff))/2
        now = time()
        perid = now-self.pretime
        self.pretime = time()

        # 计算频率
        for i in range(len(self.databuff)-2):
            if (self.databuff[i]-mid)*(self.databuff[i+2]-mid)<0:
                fre+=1

        # 计算峰峰值
        vvp=max(self.databuff)-min(self.databuff)
        self.label_4.setText(str(vvp))
        self.label_6.setText(str(round(fre/2/perid,2)))

        self.board.draw_wave(self.databuff)
        self.buffremain = self.MAXBUFF
        self.databuff = []
        print("=================refresh!!!!================")
