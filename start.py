from PyQt5 import QtCore, QtGui, QtWidgets
from customer import  Ui_customers
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(820, 920)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("BendingPriceCalc")
        MainWindow.setStyleSheet("/*background-color: qlineargradient(spread:pad, x1:0.011, y1:0.852455, x2:0.96, y2:0.085, stop:0 rgba(112, 2, 117, 255), stop:1 rgba(128, 16, 255, 255));*/\n"
"/*background-color:rgb(30, 0, 65);*/\n"
"/*background-color: rgb(156, 149, 255);*/\n"
"background-color: #7393ad;")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #MainWindow.setIconSize(QtCore.QSize(256, 256))
        #MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.bending_price_calc_window = QtWidgets.QWidget(MainWindow)
        self.bending_price_calc_window.setStyleSheet("")
        self.bending_price_calc_window.setObjectName("bending_price_calc_window")
        self.company_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.company_label.setGeometry(QtCore.QRect(20, 20, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.company_label.setFont(font)
        self.company_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.company_label.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.company_label.setAlignment(QtCore.Qt.AlignCenter)
        self.company_label.setObjectName("company_label")
        self.type_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.type_label.setGeometry(QtCore.QRect(20, 60, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.type_label.setFont(font)
        self.type_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.type_label.setObjectName("type_label")
        self.type_holder = QtWidgets.QComboBox(self.bending_price_calc_window)
        self.type_holder.setGeometry(QtCore.QRect(130, 60, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.type_holder.setFont(font)
        self.type_holder.setStyleSheet("QComboBox{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QComboBox:focus {\n"
"\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.type_holder.setObjectName("type_holder")
        self.item_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.item_label.setGeometry(QtCore.QRect(20, 100, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.item_label.setFont(font)
        self.item_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.item_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label.setObjectName("item_label")
        self.item_value = QtWidgets.QComboBox(self.bending_price_calc_window)
        self.item_value.setGeometry(QtCore.QRect(130, 100, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.item_value.setFont(font)
        self.item_value.setStyleSheet("QComboBox{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QComboBox:focus {\n"
"\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.item_value.setObjectName("item_value")
        self.code_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.code_label.setGeometry(QtCore.QRect(20, 140, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.code_label.setFont(font)
        self.code_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.code_label.setAlignment(QtCore.Qt.AlignCenter)
        self.code_label.setObjectName("code_label")
        self.code_value = QtWidgets.QComboBox(self.bending_price_calc_window)
        self.code_value.setGeometry(QtCore.QRect(130, 140, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.code_value.sizePolicy().hasHeightForWidth())
        self.code_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.code_value.setFont(font)
        self.code_value.setStyleSheet("QComboBox{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.code_value.setObjectName("code_value")
        self.length_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.length_label.setGeometry(QtCore.QRect(20, 180, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.length_label.setFont(font)
        self.length_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.length_label.setAlignment(QtCore.Qt.AlignCenter)
        self.length_label.setObjectName("length_label")
        self.length_value = QtWidgets.QComboBox(self.bending_price_calc_window)
        self.length_value.setGeometry(QtCore.QRect(130, 180, 430, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        self.length_value.setFont(font)
        self.length_value.setStyleSheet("QComboBox{\n"
"    background-color:#8BE8E5;\n"
"    color:  rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QComboBox:focus {\n"
"\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.length_value.setObjectName("length_value")
        self.quantity_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.quantity_label.setGeometry(QtCore.QRect(20, 220, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.quantity_label.setFont(font)
        self.quantity_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.quantity_label.setObjectName("quantity_label")
        self.quantity_value = QtWidgets.QSpinBox(self.bending_price_calc_window)
        self.quantity_value.setGeometry(QtCore.QRect(130, 220, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.quantity_value.setFont(font)
        self.quantity_value.setStyleSheet("QSpinBox{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"border-radius: 5px;\n"
"}\n"
"QSpinBox:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QSpinBox:focus {\n"
"\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}\n"
"QSpinBox::up-arrow {\n"
"color : blue;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"color : red;\n"
"}\n"
"\n"
"")
        self.quantity_value.setAlignment(QtCore.Qt.AlignCenter)
        self.quantity_value.setObjectName("quantity_value")
        self.add_item_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.add_item_button.setGeometry(QtCore.QRect(10, 260, 230, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.add_item_button.setFont(font)
        self.add_item_button.setStyleSheet("QPushButton {\n"
"color:white;\n"
"/*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 158, 255, 255), stop:0.55 rgba(71, 61, 235, 255), stop:0.98 rgba(27, 2, 212, 255), stop:1 rgba(0, 0, 0, 0)); */\n"
"/*background-color: rgb(102, 161, 255);*/\n"
"background-color: #4A3CE5;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.add_item_button.setObjectName("add_item_button")
        self.reset_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.reset_button.setEnabled(True)
        self.reset_button.setGeometry(QtCore.QRect(330, 260, 230, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.reset_button.setFont(font)
        self.reset_button.setStyleSheet("QPushButton {\n"
"/*background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 102, 102, 255), stop:0.5625 rgba(194, 80, 21, 255), stop:0.98 rgba(196, 4, 56, 255), stop:1 rgba(0, 0, 0, 0));*/\n"
"background-color: #312E63;\n"
"color:white;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.reset_button.setObjectName("reset_button")
        self.table = QtWidgets.QTableWidget(self.bending_price_calc_window)
        self.table.setEnabled(True)
        self.table.setGeometry(QtCore.QRect(10, 370, 800, 250))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.table.setFont(font)
        self.table.setStyleSheet("background:#D5FFE4;\n"
"color: rgb(199, 55, 255);\n"
"")
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setShowGrid(True)
        self.table.setGridStyle(QtCore.Qt.DotLine)
        self.table.setWordWrap(True)
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setKerning(False)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(3, item)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(90)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.horizontalHeader().setMinimumSectionSize(50)
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(20)
        self.table.verticalHeader().setHighlightSections(False)
        self.table.verticalHeader().setMinimumSectionSize(20)
        self.table.verticalHeader().setSortIndicatorShown(True)
        self.table.verticalHeader().setStretchLastSection(False)
        self.weight_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.weight_label.setGeometry(QtCore.QRect(10, 620, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.weight_label.setFont(font)
        self.weight_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.weight_label.setObjectName("weight_label")
        self.weight_value = QtWidgets.QLabel(self.bending_price_calc_window)
        self.weight_value.setGeometry(QtCore.QRect(130, 620, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.weight_value.setFont(font)
        self.weight_value.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 255, 255)\n"
";")
        self.weight_value.setObjectName("weight_value")
        self.lenght_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.lenght_label.setGeometry(QtCore.QRect(10, 650, 320, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.lenght_label.setFont(font)
        self.lenght_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.lenght_label.setObjectName("lenght_label")
        self.lenght_value = QtWidgets.QLabel(self.bending_price_calc_window)
        self.lenght_value.setGeometry(QtCore.QRect(340, 650, 95, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.lenght_value.setFont(font)
        self.lenght_value.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.lenght_value.setObjectName("lenght_value")
        self.pre_commercial_offer_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.pre_commercial_offer_button.setGeometry(QtCore.QRect(10, 875, 230, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        self.pre_commercial_offer_button.setFont(font)
        self.pre_commercial_offer_button.setStyleSheet("QPushButton {\n"
"background-color: #7168E3;\n"
"color:white;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.pre_commercial_offer_button.setObjectName("pre_commercial_offer_button")
        self.clear_table_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.clear_table_button.setGeometry(QtCore.QRect(580, 875, 230, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        self.clear_table_button.setFont(font)
        self.clear_table_button.setStyleSheet("QPushButton {\n"
"background-color: #312E63;\n"
"color:white;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.clear_table_button.setObjectName("clear_table_button")
        self.date_euro_layout = QtWidgets.QWidget(self.bending_price_calc_window)
        self.date_euro_layout.setEnabled(False)
        self.date_euro_layout.setGeometry(QtCore.QRect(570, 20, 240, 171))
        self.date_euro_layout.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 1, 255, 255), stop:0.55 rgba(34, 54, 133, 255), stop:0.98 rgba(2, 34, 212, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border-radius: 10px;")
        self.date_euro_layout.setObjectName("date_euro_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.date_euro_layout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.date_euro_layout)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setToolTipDuration(18)
        self.title.setStyleSheet("QLabel {\n"
"    color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.date_value = QtWidgets.QLabel(self.date_euro_layout)
        self.date_value.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.date_value.setFont(font)
        self.date_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date_value.setStyleSheet("QLabel {\n"
"    color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.date_value.setAlignment(QtCore.Qt.AlignCenter)
        self.date_value.setObjectName("date_value")
        self.verticalLayout.addWidget(self.date_value)
        self.time_label = QtWidgets.QLabel(self.date_euro_layout)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.verticalLayout.addWidget(self.time_label)
        self.day = QtWidgets.QLabel(self.date_euro_layout)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.day.setFont(font)
        self.day.setStyleSheet("QLabel {\n"
"    color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.day.setAlignment(QtCore.Qt.AlignCenter)
        self.day.setObjectName("day")
        self.verticalLayout.addWidget(self.day)
        self.euro_layout = QtWidgets.QHBoxLayout()
        self.euro_layout.setObjectName("euro_layout")
        self.euro_label = QtWidgets.QLabel(self.date_euro_layout)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.euro_label.setFont(font)
        self.euro_label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.euro_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.euro_label.setObjectName("euro_label")
        self.euro_layout.addWidget(self.euro_label)
        self.euro_value = QtWidgets.QLabel(self.date_euro_layout)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.euro_value.setFont(font)
        self.euro_value.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.euro_value.setAlignment(QtCore.Qt.AlignCenter)
        self.euro_value.setObjectName("euro_value")
        self.euro_layout.addWidget(self.euro_value)
        self.uah_label = QtWidgets.QLabel(self.date_euro_layout)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.uah_label.setFont(font)
        self.uah_label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.uah_label.setObjectName("uah_label")
        self.euro_layout.addWidget(self.uah_label)
        self.verticalLayout.addLayout(self.euro_layout)
        self.recommended_rate_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.recommended_rate_button.setEnabled(True)
        self.recommended_rate_button.setGeometry(QtCore.QRect(570, 280, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.recommended_rate_button.setFont(font)
        self.recommended_rate_button.setStyleSheet("QPushButton {\n"
"background-color: #6F61C0;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.recommended_rate_button.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.recommended_rate_button.setShortcut("")
        self.recommended_rate_button.setObjectName("recommended_rate_button")
        self.EURO_value = QtWidgets.QLineEdit(self.bending_price_calc_window)
        self.EURO_value.setGeometry(QtCore.QRect(570, 240, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.EURO_value.setFont(font)
        self.EURO_value.setStyleSheet("QLineEdit{\n"
"\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(202, 8, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.EURO_value.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.EURO_value.setAlignment(QtCore.Qt.AlignCenter)
        self.EURO_value.setObjectName("EURO_value")
        self.refresh_rate_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.refresh_rate_button.setEnabled(True)
        self.refresh_rate_button.setGeometry(QtCore.QRect(570, 200, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.refresh_rate_button.setFont(font)
        self.refresh_rate_button.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"background-color: rgb(0, 38, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.refresh_rate_button.setObjectName("refresh_rate_button")
        self.comission_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.comission_label.setGeometry(QtCore.QRect(350, 680, 80, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.comission_label.setFont(font)
        self.comission_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.comission_label.setObjectName("comission_label")
        self.persentage_spinBox = QtWidgets.QSpinBox(self.bending_price_calc_window)
        self.persentage_spinBox.setGeometry(QtCore.QRect(495, 680, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.persentage_spinBox.setFont(font)
        self.persentage_spinBox.setStyleSheet("QSpinBox{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"border-radius: 5px;\n"
"}\n"
"QSpinBox:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QSpinBox:focus {\n"
"\n"
"    border: 3px solid rgb(225, 255, 249);\n"
"}\n"
"QSpinBox::up-arrow {\n"
"color : blue;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"color : red;\n"
"}\n"
"")
        self.persentage_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.persentage_spinBox.setProperty("value", 15)
        self.persentage_spinBox.setObjectName("persentage_spinBox")
        self.percent_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.percent_label.setGeometry(QtCore.QRect(550, 680, 20, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        self.percent_label.setFont(font)
        self.percent_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.percent_label.setObjectName("percent_label")
        self.search_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.search_button.setGeometry(QtCore.QRect(10, 320, 800, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet("/*QPushButton {\n"
"background-color:#3559FC;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}*/\n"
"QPushButton {\n"
"color:white;\n"
"/*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 158, 255, 255), stop:0.55 rgba(71, 61, 235, 255), stop:0.98 rgba(27, 2, 212, 255), stop:1 rgba(0, 0, 0, 0)); */\n"
"/*background-color: rgb(102, 161, 255);*/\n"
"background-color: #4A3CE5;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.search_button.setObjectName("search_button")
        self.packing_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.packing_label.setGeometry(QtCore.QRect(10, 680, 180, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.packing_label.setFont(font)
        self.packing_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.packing_label.setObjectName("packing_label")
        self.delivery_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.delivery_label.setGeometry(QtCore.QRect(10, 720, 180, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.delivery_label.setFont(font)
        self.delivery_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.delivery_label.setObjectName("delivery_label")
        self.packing_value = QtWidgets.QLineEdit(self.bending_price_calc_window)
        self.packing_value.setGeometry(QtCore.QRect(200, 680, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.packing_value.setFont(font)
        self.packing_value.setStyleSheet("QLineEdit{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.packing_value.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.packing_value.setAlignment(QtCore.Qt.AlignCenter)
        self.packing_value.setObjectName("packing_value")
        self.delivery_value = QtWidgets.QLineEdit(self.bending_price_calc_window)
        self.delivery_value.setGeometry(QtCore.QRect(200, 720, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.delivery_value.setFont(font)
        self.delivery_value.setStyleSheet("QLineEdit{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.delivery_value.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.delivery_value.setAlignment(QtCore.Qt.AlignCenter)
        self.delivery_value.setObjectName("delivery_value")
        self.packing_euro_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.packing_euro_label.setGeometry(QtCore.QRect(290, 680, 60, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.packing_euro_label.setFont(font)
        self.packing_euro_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.packing_euro_label.setObjectName("packing_euro_label")
        self.delivery_euro_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.delivery_euro_label.setGeometry(QtCore.QRect(290, 720, 60, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.delivery_euro_label.setFont(font)
        self.delivery_euro_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.delivery_euro_label.setObjectName("delivery_euro_label")
        self.provider_discount_spinBox = QtWidgets.QSpinBox(self.bending_price_calc_window)
        self.provider_discount_spinBox.setGeometry(QtCore.QRect(495, 760, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.provider_discount_spinBox.setFont(font)
        self.provider_discount_spinBox.setStyleSheet("QSpinBox{\n"
"    background-color:#8BE8E5;\n"
"    color:  rgb(199, 55, 255);\n"
"border-radius: 5px;\n"
"}\n"
"QSpinBox:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QSpinBox:focus {\n"
"\n"
"    border: 3px solid rgb(225, 255, 249);\n"
"}\n"
"QSpinBox::up-arrow {\n"
"color : blue;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"color : red;\n"
"}\n"
"")
        self.provider_discount_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.provider_discount_spinBox.setProperty("value", 35)
        self.provider_discount_spinBox.setObjectName("provider_discount_spinBox")
        self.discount_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.discount_label.setGeometry(QtCore.QRect(350, 760, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        self.discount_label.setFont(font)
        self.discount_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 253, 240);")
        self.discount_label.setObjectName("discount_label")
        self.percent_discount_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.percent_discount_label.setGeometry(QtCore.QRect(550, 760, 20, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.percent_discount_label.setFont(font)
        self.percent_discount_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 253, 240);")
        self.percent_discount_label.setObjectName("percent_discount_label")
        self.add_amount_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.add_amount_button.setGeometry(QtCore.QRect(580, 630, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.add_amount_button.setFont(font)
        self.add_amount_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_amount_button.setStyleSheet("\n"
"QPushButton {\n"
"background-color: #6F61C0;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.add_amount_button.setObjectName("add_amount_button")
        self.remove_amount_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.remove_amount_button.setGeometry(QtCore.QRect(700, 630, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.remove_amount_button.setFont(font)
        self.remove_amount_button.setStyleSheet("\n"
"QPushButton{\n"
"background-color: #6F61C0;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.remove_amount_button.setObjectName("remove_amount_button")
        self.update_row = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.update_row.setGeometry(QtCore.QRect(580, 670, 230, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.update_row.setFont(font)
        self.update_row.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.update_row.setStyleSheet("\n"
"QPushButton {\n"
"background: #6F61C0;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.update_row.setObjectName("update_row")
        self.db_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.db_button.setGeometry(QtCore.QRect(580, 750, 230, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.db_button.setFont(font)
        self.db_button.setStyleSheet("QPushButton {\n"
"color:white;\n"
"background-color: #3559FC;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.db_button.setObjectName("db_button")
        self.remove_element = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.remove_element.setGeometry(QtCore.QRect(580, 710, 230, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.remove_element.setFont(font)
        self.remove_element.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remove_element.setStyleSheet("\n"
"QPushButton {\n"
"background: #312E63;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.remove_element.setObjectName("remove_element")
        self.company_button = QtWidgets.QPushButton(self.bending_price_calc_window)
        self.company_button.setEnabled(True)
        self.company_button.setGeometry(QtCore.QRect(440, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.company_button.setFont(font)
        self.company_button.setStyleSheet("QPushButton {\n"
"background-color: #6F61C0;\n"
"color:white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgb(48, 221, 255);\n"
"}")
        self.company_button.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.company_button.setShortcut("")
        self.company_button.setObjectName("company_button")
        self.company_value = QtWidgets.QComboBox(self.bending_price_calc_window)
        self.company_value.setGeometry(QtCore.QRect(130, 20, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.company_value.setFont(font)
        self.company_value.setStyleSheet("QComboBox{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QComboBox:focus {\n"
"\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.company_value.setObjectName("company_value")
        self.discount_customer_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.discount_customer_label.setGeometry(QtCore.QRect(350, 720, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.discount_customer_label.setFont(font)
        self.discount_customer_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 253, 240);")
        self.discount_customer_label.setObjectName("discount_customer_label")
        self.discount_customer_spinBox = QtWidgets.QSpinBox(self.bending_price_calc_window)
        self.discount_customer_spinBox.setGeometry(QtCore.QRect(495, 720, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.discount_customer_spinBox.setFont(font)
        self.discount_customer_spinBox.setStyleSheet("QSpinBox{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"border-radius: 5px;\n"
"}\n"
"QSpinBox:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QSpinBox:focus {\n"
"\n"
"    border: 3px solid rgb(225, 255, 249);\n"
"}\n"
"QSpinBox::up-arrow {\n"
"color : blue;\n"
"}\n"
"QSpinBox::down-arrow {\n"
"color : red;\n"
"}\n"
"")
        self.discount_customer_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.discount_customer_spinBox.setProperty("value", 0)
        self.discount_customer_spinBox.setObjectName("discount_customer_spinBox")
        self.percent_discount_customer_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.percent_discount_customer_label.setGeometry(QtCore.QRect(550, 720, 20, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        self.percent_discount_customer_label.setFont(font)
        self.percent_discount_customer_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.percent_discount_customer_label.setObjectName("percent_discount_customer_label")
        self.delivery_document_euro_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.delivery_document_euro_label.setGeometry(QtCore.QRect(290, 760, 60, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.delivery_document_euro_label.setFont(font)
        self.delivery_document_euro_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.delivery_document_euro_label.setObjectName("delivery_document_euro_label")
        self.delivery_document_value = QtWidgets.QLineEdit(self.bending_price_calc_window)
        self.delivery_document_value.setGeometry(QtCore.QRect(200, 760, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.delivery_document_value.setFont(font)
        self.delivery_document_value.setStyleSheet("QLineEdit{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.delivery_document_value.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.delivery_document_value.setAlignment(QtCore.Qt.AlignCenter)
        self.delivery_document_value.setObjectName("delivery_document_value")
        self.delivery_document_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.delivery_document_label.setGeometry(QtCore.QRect(10, 760, 180, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.delivery_document_label.setFont(font)
        self.delivery_document_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.delivery_document_label.setObjectName("delivery_document_label")
        self.bank_tax_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.bank_tax_label.setGeometry(QtCore.QRect(350, 800, 130, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.bank_tax_label.setFont(font)
        self.bank_tax_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.bank_tax_label.setObjectName("bank_tax_label")
        self.bank_tax_value = QtWidgets.QLineEdit(self.bending_price_calc_window)
        self.bank_tax_value.setGeometry(QtCore.QRect(480, 800, 65, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.bank_tax_value.setFont(font)
        self.bank_tax_value.setStyleSheet("QLineEdit{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.bank_tax_value.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.bank_tax_value.setAlignment(QtCore.Qt.AlignCenter)
        self.bank_tax_value.setObjectName("bank_tax_value")
        self.percent_bank_tax_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.percent_bank_tax_label.setGeometry(QtCore.QRect(550, 800, 20, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.percent_bank_tax_label.setFont(font)
        self.percent_bank_tax_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 253, 240);")
        self.percent_bank_tax_label.setObjectName("percent_bank_tax_label")
        self.transaction_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.transaction_label.setGeometry(QtCore.QRect(10, 800, 160, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.transaction_label.setFont(font)
        self.transaction_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.transaction_label.setObjectName("transaction_label")
        self.transaction_value = QtWidgets.QLineEdit(self.bending_price_calc_window)
        self.transaction_value.setGeometry(QtCore.QRect(200, 800, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.transaction_value.setFont(font)
        self.transaction_value.setStyleSheet("QLineEdit{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.transaction_value.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.transaction_value.setAlignment(QtCore.Qt.AlignCenter)
        self.transaction_value.setObjectName("transaction_value")
        self.transaction_uah_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.transaction_uah_label.setGeometry(QtCore.QRect(290, 800, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.transaction_uah_label.setFont(font)
        self.transaction_uah_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.transaction_uah_label.setObjectName("transaction_uah_label")
        self.brokerage_services_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.brokerage_services_label.setGeometry(QtCore.QRect(10, 840, 160, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.brokerage_services_label.setFont(font)
        self.brokerage_services_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.brokerage_services_label.setObjectName("brokerage_services_label")
        self.brokerage_services_value = QtWidgets.QLineEdit(self.bending_price_calc_window)
        self.brokerage_services_value.setGeometry(QtCore.QRect(200, 840, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        self.brokerage_services_value.setFont(font)
        self.brokerage_services_value.setStyleSheet("QLineEdit{\n"
"    background-color:#8BE8E5;\n"
"    color: rgb(199, 55, 255);\n"
"    border: 1px  rgb(237, 255, 152);\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 3px solid rgb(2, 35, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 3px solid rgb(0, 255, 162);\n"
"}")
        self.brokerage_services_value.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.brokerage_services_value.setAlignment(QtCore.Qt.AlignCenter)
        self.brokerage_services_value.setObjectName("brokerage_services_value")
        self.brokerage_services_uah_label = QtWidgets.QLabel(self.bending_price_calc_window)
        self.brokerage_services_uah_label.setGeometry(QtCore.QRect(290, 840, 40, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.brokerage_services_uah_label.setFont(font)
        self.brokerage_services_uah_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgb(255, 255, 255);")
        self.brokerage_services_uah_label.setObjectName("brokerage_services_uah_label")
        #MainWindow.setCentralWidget(self.bending_price_calc_window)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.company_label.setText(_translate("MainWindow", "Компанія"))
        self.type_label.setText(_translate("MainWindow", "Tип"))
        self.item_label.setText(_translate("MainWindow", "Виріб"))
        self.item_value.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>QComboBox{</p><p>    background-color: rgb(237, 255, 152);</p><p>    color: rgb(202, 8, 255);</p><p>}</p><p>QComboBoxt:hover {</p><p>    border: 3px solid rgb(2, 35, 255);</p><p>}</p><p>QComboBox:focus {</p><p><br/></p><p>    border: 3px solid rgb(225, 255, 249);</p><p>}</p></body></html>"))
        self.code_label.setText(_translate("MainWindow", "Номер"))
        self.length_label.setText(_translate("MainWindow", "Довжина"))
        self.quantity_label.setText(_translate("MainWindow", "Кількість"))
        self.add_item_button.setText(_translate("MainWindow", "Додати виріб"))
        self.reset_button.setText(_translate("MainWindow", "Все з початку"))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Код"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Назва"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Кількість"))
        self.weight_label.setText(_translate("MainWindow", "Вага складає"))
        self.weight_value.setText(_translate("MainWindow", "0.00 кг"))
        self.lenght_label.setText(_translate("MainWindow", "Максимальна довжина одного виробу"))
        self.lenght_value.setText(_translate("MainWindow", "0.0 см"))
        self.pre_commercial_offer_button.setText(_translate("MainWindow", "Створити xlsx"))
        self.clear_table_button.setText(_translate("MainWindow", "Скинути таблицю"))
        self.title.setText(_translate("MainWindow", "Курс по міжбанку станом на"))
        self.date_value.setText(_translate("MainWindow", "26.07.2023"))
        self.time_label.setText(_translate("MainWindow", "11:22"))
        self.day.setText(_translate("MainWindow", "Середа"))
        self.euro_label.setText(_translate("MainWindow", "EUR"))
        self.euro_value.setText(_translate("MainWindow", "00,0000"))
        self.uah_label.setText(_translate("MainWindow", "ГРН"))
        self.recommended_rate_button.setText(_translate("MainWindow", "Рекомендований курс"))
        self.refresh_rate_button.setText(_translate("MainWindow", "Оновити"))
        self.comission_label.setText(_translate("MainWindow", "Комісія"))
        self.percent_label.setText(_translate("MainWindow", "%"))
        self.search_button.setText(_translate("MainWindow", "Підібрати пуансон або матрицю"))
        self.packing_label.setText(_translate("MainWindow", "Вартість пакування"))
        self.delivery_label.setText(_translate("MainWindow", "Вартість доставки"))
        self.packing_euro_label.setText(_translate("MainWindow", "EURO"))
        self.delivery_euro_label.setText(_translate("MainWindow", "EURO"))
        self.discount_label.setText(_translate("MainWindow", "Знижка постачальника"))
        self.percent_discount_label.setText(_translate("MainWindow", "%"))
        self.add_amount_button.setText(_translate("MainWindow", "+1"))
        self.remove_amount_button.setText(_translate("MainWindow", "-1"))
        self.update_row.setText(_translate("MainWindow", "Корегувати"))
        self.db_button.setText(_translate("MainWindow", "База"))
        self.remove_element.setText(_translate("MainWindow", "Видалити"))
        self.company_button.setText(_translate("MainWindow", " Наші клієнти"))
        self.company_value.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>QComboBox{</p><p>    background-color: rgb(237, 255, 152);</p><p>    color: rgb(202, 8, 255);</p><p>}</p><p>QComboBoxt:hover {</p><p>    border: 3px solid rgb(2, 35, 255);</p><p>}</p><p>QComboBox:focus {</p><p><br/></p><p>    border: 3px solid rgb(225, 255, 249);</p><p>}</p></body></html>"))
        self.discount_customer_label.setText(_translate("MainWindow", "Знижка клієнту"))
        self.percent_discount_customer_label.setText(_translate("MainWindow", "%"))
        self.delivery_document_euro_label.setText(_translate("MainWindow", "EURO"))
        self.delivery_document_label.setText(_translate("MainWindow", "Вартість EX-1/ EURO-1"))
        self.bank_tax_label.setText(_translate("MainWindow", "Податок банка"))
        self.bank_tax_value.setText(_translate("MainWindow", "0,2"))
        self.percent_bank_tax_label.setText(_translate("MainWindow", "%"))
        self.transaction_label.setText(_translate("MainWindow", "Вартість переказу"))
        self.transaction_value.setText(_translate("MainWindow", "1097,6"))
        self.transaction_uah_label.setText(_translate("MainWindow", "ГРН"))
        self.brokerage_services_label.setText(_translate("MainWindow", "Брокерскі послуги"))
        self.brokerage_services_value.setText(_translate("MainWindow", "2500"))
        self.brokerage_services_uah_label.setText(_translate("MainWindow", "ГРН"))

class Customers(QtWidgets.QWidget,  Ui_customers):
    def __init__(self, parent=None):
        super(Customers, self).__init__(parent)
        self.setupUi(self)


class Main(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.company_button.clicked.connect(self.open_customer_window)

    def open_customer_window(self):
        self.win = Customers()
        self.win.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    w = Main()
    w.show()

    sys.exit(app.exec_())