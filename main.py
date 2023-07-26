import sys
from datetime import datetime, date

from PyQt5 import QtWidgets, uic

# from PyQt5.QtWidgets import QApplication, QMainWindow

type_item_list = [
    "Оберіть тип кріплення",
    "Amada",
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
        for item_connection in type_item_list:
            self.type_value.addItem(item_connection)

        self.item_value.addItem("Оберіть тип кріплення")
        self.number_value.addItem("?")
        self.length_value.addItem("Оберіть номер виробу")

        date_list = get_list_moment()

        # self.date_euro_layout.date_value.setText(date_list[0])
    	self.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()

app.exec_()
