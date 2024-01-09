from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
import csv
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 440)
        MainWindow.setFixedSize(698, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 701, 283))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_period = QtWidgets.QWidget()
        self.tab_period.setObjectName("tab_period")
        self.calendarWidget_start_time = QtWidgets.QCalendarWidget(self.tab_period)
        self.calendarWidget_start_time.setGeometry(QtCore.QRect(10, 0, 321, 201))
        self.calendarWidget_start_time.setObjectName("calendarWidget_start_time")
        self.calendarWidget_end_time = QtWidgets.QCalendarWidget(self.tab_period)
        self.calendarWidget_end_time.setGeometry(QtCore.QRect(370, 0, 321, 201))
        self.calendarWidget_end_time.setObjectName("calendarWidget_end_time")
        self.label = QtWidgets.QLabel(self.tab_period)
        self.label.setGeometry(QtCore.QRect(10, 200, 141, 31))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_period)
        self.label_2.setGeometry(QtCore.QRect(370, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3_start = QtWidgets.QLabel(self.tab_period)
        self.label_3_start.setGeometry(QtCore.QRect(170, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3_start.setFont(font)
        self.label_3_start.setText("")
        self.label_3_start.setObjectName("label_3_start")
        self.label_4_end = QtWidgets.QLabel(self.tab_period)
        self.label_4_end.setGeometry(QtCore.QRect(560, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4_end.setFont(font)
        self.label_4_end.setText("")
        self.label_4_end.setObjectName("label_4_end")
        self.tabWidget.addTab(self.tab_period, "")
        self.tab_3_day = QtWidgets.QWidget()
        self.tab_3_day.setObjectName("tab_3_day")
        self.calendarWidget_get_day = QtWidgets.QCalendarWidget(self.tab_3_day)
        self.calendarWidget_get_day.setGeometry(QtCore.QRect(160, 20, 361, 211))
        self.calendarWidget_get_day.setObjectName("calendarWidget_get_day")
        self.tabWidget.addTab(self.tab_3_day, "")
        self.tab_2_month = QtWidgets.QWidget()
        self.tab_2_month.setObjectName("tab_2_month")
        self.pushButton_February = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_February.setGeometry(QtCore.QRect(0, 130, 175, 51))
        self.pushButton_February.setObjectName("pushButton_February")
        self.pushButton_March = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_March.setGeometry(QtCore.QRect(0, 180, 175, 51))
        self.pushButton_March.setObjectName("pushButton_March")
        self.pushButton_January = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_January.setGeometry(QtCore.QRect(0, 80, 175, 51))
        self.pushButton_January.setObjectName("pushButton_January")
        self.pushButton_June = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_June.setGeometry(QtCore.QRect(170, 180, 175, 51))
        self.pushButton_June.setObjectName("pushButton_June")
        self.pushButton_April = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_April.setGeometry(QtCore.QRect(170, 80, 175, 51))
        self.pushButton_April.setObjectName("pushButton_April")
        self.pushButton_May = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_May.setGeometry(QtCore.QRect(170, 130, 175, 51))
        self.pushButton_May.setObjectName("pushButton_May")
        self.pushButton_September = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_September.setGeometry(QtCore.QRect(340, 180, 175, 51))
        self.pushButton_September.setObjectName("pushButton_September")
        self.pushButton_July = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_July.setGeometry(QtCore.QRect(340, 80, 175, 51))
        self.pushButton_July.setObjectName("pushButton_July")
        self.pushButton_August = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_August.setGeometry(QtCore.QRect(340, 130, 175, 51))
        self.pushButton_August.setObjectName("pushButton_August")
        self.pushButton_December = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_December.setGeometry(QtCore.QRect(510, 180, 175, 51))
        self.pushButton_December.setObjectName("pushButton_December")
        self.pushButton_Orcober = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_Orcober.setGeometry(QtCore.QRect(510, 80, 175, 51))
        self.pushButton_Orcober.setObjectName("pushButton_Orcober")
        self.pushButton_November = QtWidgets.QPushButton(self.tab_2_month)
        self.pushButton_November.setGeometry(QtCore.QRect(510, 130, 175, 51))
        self.pushButton_November.setObjectName("pushButton_November")
        self.label_5_show_month = QtWidgets.QLabel(self.tab_2_month)
        self.label_5_show_month.setGeometry(QtCore.QRect(140, 10, 411, 31))
        self.label_5_show_month.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.label_5_show_month.setTextFormat(QtCore.Qt.PlainText)
        self.label_5_show_month.setObjectName("label_5_show_month")
        self.dateEdit_month = QtWidgets.QDateEdit(self.tab_2_month)
        self.dateEdit_month.setGeometry(QtCore.QRect(270, 40, 141, 31))
        self.dateEdit_month.setObjectName("dateEdit_month")
        self.tabWidget.addTab(self.tab_2_month, "")
        self.tab_year = QtWidgets.QWidget()
        self.tab_year.setObjectName("tab_year")
        self.dateEdit_year = QtWidgets.QDateEdit(self.tab_year)
        self.dateEdit_year.setGeometry(QtCore.QRect(240, 60, 201, 61))
        self.dateEdit_year.setObjectName("dateEdit_year")
        self.tabWidget.addTab(self.tab_year, "")
        self.tab_4_quarter = QtWidgets.QWidget()
        self.tab_4_quarter.setObjectName("tab_4_quarter")
        self.dateEdit_quarter = QtWidgets.QDateEdit(self.tab_4_quarter)
        self.dateEdit_quarter.setGeometry(QtCore.QRect(260, 110, 141, 31))
        self.dateEdit_quarter.setObjectName("dateEdit_quarter")
        self.radioButton_1quarter = QtWidgets.QRadioButton(self.tab_4_quarter)
        self.radioButton_1quarter.setGeometry(QtCore.QRect(100, 180, 82, 17))
        self.radioButton_1quarter.setObjectName("radioButton_1quarter")
        self.radioButton_2quarter = QtWidgets.QRadioButton(self.tab_4_quarter)
        self.radioButton_2quarter.setGeometry(QtCore.QRect(230, 180, 82, 17))
        self.radioButton_2quarter.setObjectName("radioButton_2quarter")
        self.radioButton_3quarter = QtWidgets.QRadioButton(self.tab_4_quarter)
        self.radioButton_3quarter.setGeometry(QtCore.QRect(350, 180, 82, 17))
        self.radioButton_3quarter.setObjectName("radioButton_3quarter")
        self.radioButton_4quarter = QtWidgets.QRadioButton(self.tab_4_quarter)
        self.radioButton_4quarter.setGeometry(QtCore.QRect(470, 180, 82, 17))
        self.radioButton_4quarter.setObjectName("radioButton_4quarter")
        self.tabWidget.addTab(self.tab_4_quarter, "")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(0, 260, 701, 91))
        self.pushButton_start.setStyleSheet("background-color: #00a0e4;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "font: 14pt \"MS Reference Sans Serif\";")
        self.pushButton_start.setObjectName("pushButton_start")
        self.checkBox_Diadok = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Diadok.setGeometry(QtCore.QRect(90, 360, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Diadok.sizePolicy().hasHeightForWidth())
        self.checkBox_Diadok.setSizePolicy(sizePolicy)
        self.checkBox_Diadok.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Diadok.setFont(font)
        self.checkBox_Diadok.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Diadok.setChecked(True)
        self.checkBox_Diadok.setObjectName("checkBox_Diadok")
        self.checkBox_local_folder = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_local_folder.setGeometry(QtCore.QRect(430, 360, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.checkBox_local_folder.setFont(font)
        self.checkBox_local_folder.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_local_folder.setChecked(True)
        self.checkBox_local_folder.setObjectName("checkBox_local_folder")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        self.radioButton_1quarter.setChecked(True)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.calendarWidget_get_day.setMaximumDate(datetime.now())
        self.calendarWidget_start_time.setMaximumDate(datetime.now())
        self.calendarWidget_end_time.setMaximumDate(datetime.now())
        self.dateEdit_year.setDate(datetime.now())
        self.dateEdit_year.setMaximumDate(datetime.now())
        self.dateEdit_month.setDate(datetime.now())
        self.dateEdit_month.setMaximumDate(datetime.now())
        self.dateEdit_quarter.setDate(datetime.now())
        self.dateEdit_quarter.setMaximumDate(datetime.now())
        self.tabWidget.setCurrentWidget(self.tab_period)

        self.pushButton_start.setStyleSheet("background-color: #00a0e4;")
        self.functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Начало периода"))
        self.label_2.setText(_translate("MainWindow", "Окончание периода"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_period), _translate("MainWindow", "Период"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3_day), _translate("MainWindow", "День"))
        self.pushButton_February.setText(_translate("MainWindow", "Февраль"))
        self.pushButton_March.setText(_translate("MainWindow", "Март"))
        self.pushButton_January.setText(_translate("MainWindow", "Январь"))
        self.pushButton_June.setText(_translate("MainWindow", "Июнь"))
        self.pushButton_April.setText(_translate("MainWindow", "Апрель"))
        self.pushButton_May.setText(_translate("MainWindow", "Май"))
        self.pushButton_September.setText(_translate("MainWindow", "Сентябрь"))
        self.pushButton_July.setText(_translate("MainWindow", "Июль"))
        self.pushButton_August.setText(_translate("MainWindow", "Август"))
        self.pushButton_December.setText(_translate("MainWindow", "Декабрь"))
        self.pushButton_Orcober.setText(_translate("MainWindow", "Октябрь"))
        self.pushButton_November.setText(_translate("MainWindow", "Ноябрь"))
        self.label_5_show_month.setText(_translate("MainWindow", "Укажите месяц"))
        self.dateEdit_month.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2_month), _translate("MainWindow", "Месяц"))
        self.dateEdit_year.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_year), _translate("MainWindow", "Год"))
        self.dateEdit_quarter.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.radioButton_1quarter.setText(_translate("MainWindow", "1 квартал"))
        self.radioButton_2quarter.setText(_translate("MainWindow", "2 квартал"))
        self.radioButton_3quarter.setText(_translate("MainWindow", "3 квартал"))
        self.radioButton_4quarter.setText(_translate("MainWindow", "4 квартал"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4_quarter), _translate("MainWindow", "Квартал"))
        self.pushButton_start.setText(_translate("MainWindow", "Запуск"))
        self.checkBox_Diadok.setText(_translate("MainWindow", "Контур диадок"))
        self.checkBox_local_folder.setText(_translate("MainWindow", "Локальная папка"))

    def tab_change(self):
        tab_index = self.tabWidget.currentIndex()
        return tab_index

    def functions(self):
        self.pushButton_start.clicked.connect(lambda: self.get_result(self.tab_change()))
        self.calendarWidget_start_time.clicked.connect(self.get_label_value_period)
        self.calendarWidget_end_time.clicked.connect(self.get_label_value_period)
        self.calendarWidget_get_day.clicked.connect(self.get_day_value)
        self.radioButton_1quarter.clicked.connect(self.get_quarter_vaue)
        self.radioButton_2quarter.clicked.connect(self.get_quarter_vaue)
        self.radioButton_3quarter.clicked.connect(self.get_quarter_vaue)
        self.radioButton_4quarter.clicked.connect(self.get_quarter_vaue)
        self.pushButton_January.clicked.connect(lambda: self.get_month_value(self.pushButton_January.text()))
        self.pushButton_February.clicked.connect(lambda: self.get_month_value(self.pushButton_February.text()))
        self.pushButton_March.clicked.connect(lambda: self.get_month_value(self.pushButton_March.text()))
        self.pushButton_April.clicked.connect(lambda: self.get_month_value(self.pushButton_April.text()))
        self.pushButton_May.clicked.connect(lambda: self.get_month_value(self.pushButton_May.text()))
        self.pushButton_June.clicked.connect(lambda: self.get_month_value(self.pushButton_June.text()))
        self.pushButton_July.clicked.connect(lambda: self.get_month_value(self.pushButton_July.text()))
        self.pushButton_August.clicked.connect(lambda: self.get_month_value(self.pushButton_August.text()))
        self.pushButton_September.clicked.connect(lambda: self.get_month_value(self.pushButton_September.text()))
        self.pushButton_Orcober.clicked.connect(lambda: self.get_month_value(self.pushButton_Orcober.text()))
        self.pushButton_November.clicked.connect(lambda: self.get_month_value(self.pushButton_November.text()))
        self.pushButton_December.clicked.connect(lambda: self.get_month_value(self.pushButton_December.text()))

    def checkbox(self):
        checkbox = []
        if self.checkBox_Diadok.isChecked():
            checkbox.append("D")
        if self.checkBox_local_folder.isChecked():
            checkbox.append("L")
        return checkbox

    def get_quarter_vaue(self):
        select = 0
        cb = self.checkbox()
        get_year = self.dateEdit_quarter.date().toString("yyyy")
        if self.radioButton_1quarter.isChecked():
            select = 1
        elif self.radioButton_2quarter.isChecked():
            select = 2
        elif self.radioButton_3quarter.isChecked():
            select = 3
        elif self.radioButton_2quarter.isChecked():
            select = 4
        result = [[f"Запрос от: {datetime.now()}"], ["quarter"], [select], [get_year], cb]
        self.checkbox()
        return result

    def get_year_value(self):
        cb = self.checkbox()
        get_year = self.dateEdit_year.date().toString("yyyy")
        print(get_year)
        result = [[f"Запрос от: {datetime.now()}"], ["year"], [get_year], [""], cb]
        return result

    def get_day_value(self):
        cb = self.checkbox()
        get_day = self.calendarWidget_get_day.selectedDate()
        result = [[f"Запрос от: {datetime.now()}"],
                  ["day"], [get_day.toString("dd.MM.yyyy")], [""], cb]
        print(result)
        return result

    def get_month_value(self, month_label):
        cb = self.checkbox()
        mul = {"Январь": 1, "Февраль": 2, "Март": 3,
               "Апрель": 4, "Май": 5, "Июнь": 6,
               "Июль": 7, "Август": 8, "Сентябрь": 9,
               "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12}
        get_month_year = self.dateEdit_month.date().toString("yyyy")
        self.label_5_show_month.setText(month_label)
        print(get_month_year, month_label)
        result = [[f"Запрос от: {datetime.now()}"], ["month"], [get_month_year], [mul[month_label]], cb]
        print(result)
        with open("log.csv", "w") as f:
            writer = csv.writer(f, lineterminator=" \r")
            for j in result:
                writer.writerow(j)


    def get_label_value_period(self):
        cb = self.checkbox()
        date_start = self.calendarWidget_start_time.selectedDate()
        date_end = self.calendarWidget_end_time.selectedDate()
        self.label_3_start.setText(date_start.toString("dd.MM.yyyy"))
        self.label_4_end.setText(date_end.toString("dd.MM.yyyy"))

        if date_start > date_end:
            print(123)
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Недопустимое значение периода")
            error.setIcon(QMessageBox.Warning)
            error.exec_()

        result = [[f"Запрос от: {datetime.now()}"],
                  ["period"], [date_start.toString("dd.MM.yyyy")],
                  [date_end.toString("dd.MM.yyyy")], cb]
        return result

    def get_result(self, i):
        if i == 0:
            data = self.get_label_value_period()
        elif i == 1:
            data = self.get_day_value()
        elif i == 2:
            sys.exit()
        elif i == 3:
            data =self.get_year_value()
        elif i == 4:
            data = self.get_quarter_vaue()
        with open("log.csv", "w") as f:
            writer = csv.writer(f, lineterminator=" \r")
            for j in data:
                writer.writerow(j)
        sys.exit()

    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Название окна")
        msg.setText("Описание")
        msg.setIcon(QMessageBox.Warning)

        msg.exec_()


        # sys.exit()


def start():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.get_label_value_period()
    MainWindow.show()
    sys.exit(app.exec_())


start()
