import sys
import requests
from datetime import datetime, date
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

import style
from model import Invoice, Item
import mainwindow
from style import *

# from PyQt5.QtWidgets import QApplication, QMainWindow

type_holder_list = [
    "Оберіть тип кріплення",
    "Amada-promecam",
    "Trumpf-Wila",
    "Bystronic"
]

item_list_amada = [
    "Оберіть виріб",
    "Пуансон",
    "Матриця одноручова",
    "Пуансон плющення",
    "Матриця плющення",
    "Матриця багаторучова",
    "Тримач пуансона",
    "Прижимні планки",
    "Тримач матриці"
]

item_list_trumpf_wila = [
    "Оберіть виріб",
    "Пуансон",
    "Матриця",
    "Пуансон плющення",
    "Матриця плющення",
    "Кнопка",
    "Штифт"
]


category = {
    type_holder_list[0]: type_holder_list[0],
    type_holder_list[1]: item_list_amada,
    type_holder_list[2]: item_list_trumpf_wila,
    type_holder_list[3]: item_list_trumpf_wila[0:5],
}


week_day = {
    1: "понеділок",
    2: "вівторок",
    3: "середа",
    4: "четвер",
    5: "п'ятниця",
    6: "субота",
    7: "неділя"
}

#створюємо список з датою
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

#Отримуємо курс валюти з сайта мінфіна по міжбанку
def get_rate() -> str:
    rate = ""
    url = "https://minfin.com.ua/currency/mb/"
    request = requests.get(url)
    if request.status_code == 200:
        print(request.status_code)
    soup = BeautifulSoup(request.text, "html.parser")
    td_list = soup.find_all("td", "sc-1x32wa2-8 tWvco")
    rate_full_string = None
    for item in td_list:
        rate_full_string = item.find("div", {"class": "sc-1x32wa2-9 bKmKjX"}).text
    rate = rate_full_string[0:6]
    return rate



def get_recommended_rate_for_euro_value(new_rate: str) -> str:
    rate = new_rate.replace(",", ".")
    result = str(round(float(rate) * 1.01, 2))
    return result


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        uic.loadUi("BendingPriceCalc.ui", self)
        self.setGeometry(50, 50, 820, 880)
        self.setFixedSize(820, 880)
        self.m_w = None
        for item_connection in type_holder_list:
            self.type_value.addItem(item_connection)
        self.type_value.activated.connect(self.get_items)
        self.type_value.setStyleSheet(style.type_value_style)

        self.add_item_button.clicked.connect(self.add_item_function)

        self.item_value.addItem("Оберіть тип кріплення")
        self.number_value.addItem("?")
        self.length_value.addItem("Оберіть номер виробу")

        # Блок роботи з валютою
        time_info = get_list_moment()
        rate = get_rate()
        self.euro_value.setText(rate)
        self.EURO_value.setText(get_recommended_rate_for_euro_value(rate))
        self.date_value.setText(time_info[0])
        self.time_label.setText(time_info[1])
        self.day.setText(time_info[2])

        self.refresh_rate_button.clicked.connect(self.refresh_rate)
        self.search_button.clicked.connect(self.search_item)

        #Створюємо invoice, у якому будуть лежати вироби (item)
        my_invoice = Invoice()

        #встановлюємо курс евро
        my_invoice.set_rate(self.EURO_value.text())
        print(my_invoice.get_rate())
        self.show()


    #Додаємо виріб до таблиці
    def add_item_function(self):
        self.table.setData()
        pass

    def get_items(self) -> None:
        if category[self.type_value.currentText()] == type_holder_list[0]:
            self.item_value.clear()
            self.item_value.addItem(type_holder_list[0])
        else:
            self.item_value.clear()
            for item in category[self.type_value.currentText()]:
                self.item_value.addItem(item)


    def get_numbers(self) -> None:
        #20.210
        pass

    #Оновлення дати та курса
    def refresh_rate(self) -> None:
        time_info = get_list_moment()
        self.window.date_value.setText(time_info[0])
        self.window.time_label.setText(time_info[1])
        self.window.day.setText(time_info[2])
        self.window.euro_value.setText(get_rate())

    #Створення пошукового вікна
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
