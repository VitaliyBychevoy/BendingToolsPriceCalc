import sys
import requests
from datetime import datetime, date
from bs4 import BeautifulSoup
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
    rate = rate_full_string[0:7]
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
        for item_connection in type_item_list:
            self.type_value.addItem(item_connection)

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

        self.show()

    #Оновлення дати та курса
    def refresh_rate(self) -> None:
        time_info = get_list_moment()
        self.date_value.setText(time_info[0])
        self.time_label.setText(time_info[1])
        self.day.setText(time_info[2])
        self.euro_value.setText(get_rate())

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
