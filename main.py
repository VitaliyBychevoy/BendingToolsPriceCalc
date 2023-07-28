import sys
from datetime import datetime, date

from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

# from PyQt5.QtWidgets import QApplication, QMainWindow

type_item_list = [
    "Оберіть тип кріплення",
    "Amada-promecam",
    "Trumpf",
    "Wila",
    "Bystronic"
]

item_list = [
    "Пуансон",
    "Матриця",
    "Пуансон плющення",
    "Матриця плющення",
]
week_day = {
    1: "понеділок",
    2: "вівторок",
    3: "середа",
    4: "четверг",
    5: "п'ятниця",
    6: "субота",
    7: "неділя"
}


def get_list_moment() -> list:
    request_moment_1 = datetime.now()
    moment = str(request_moment_1)
    day = date.today().isoweekday()
    moment_list = moment.split(" ")
    date_list = moment_list[0].split("-")
    date_str = ":".join(date_list[::-1])
    time_list = moment_list[1].split(":")
    time_string = time_list[0] + ":" + time_list[1]
    list_result = [date_str, time_string, week_day[day]]
    return list_result


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("BendingPriceCalc.ui", self)
        self.setGeometry(50, 50, 820, 880)
        self.m_w = None
        for item_connection in type_item_list:
            self.type_value.addItem(item_connection)

        self.item_value.addItem("Оберіть тип кріплення")
        self.number_value.addItem("?")
        self.length_value.addItem("Оберіть номер виробу")

        # Блок роботи з валютою
        time_info = get_list_moment()
        self.EURO_value.setText(self.euro_value.text())

        self.date_value.setText(time_info[0])
        self.time_label.setText(time_info[1])
        self.day.setText(time_info[2])

        self.refresh_rate_button.clicked.connect(self.refresh_rate)
        self.search_button.clicked.connect(self.search_item)

        self.show()

    def refresh_rate(self) -> None:
        time_info = get_list_moment()
        print(time_info)
        self.date_value.setText(time_info[0])
        self.time_label.setText(time_info[1])
        self.day.setText(time_info[2])

    def search_item(self) -> None:
        self.m_w = Search()

        self.m_w.show()


class Search(QMdiSubWindow):
    def __init__(self):
        super(Search, self).__init__()
        self.setGeometry(870, 50, 820, 880)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        uic.loadUi("Search.ui", self)


app = QtWidgets.QApplication(sys.argv)
window = Ui()

app.exec_()
