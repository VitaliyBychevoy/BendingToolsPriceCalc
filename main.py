import sys
import requests
from datetime import datetime, date
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

import db_handler
import style
from model import Invoice, Item
from db_handler import *
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
    # if request.status_code == 200:
    #     print(request.status_code)
    soup = BeautifulSoup(request.text, "html.parser")
    td_list = soup.find_all("td", "sc-1x32wa2-8 tWvco")
    rate_full_string = None
    for item in td_list:
        rate_full_string = item.find("div", {"class": "sc-1x32wa2-9 bKmKjX"}).text
    rate = rate_full_string[0:6]
    print("rate ok")
    return rate



def get_recommended_rate_for_euro_value(new_rate: str) -> str:
    rate = new_rate.replace(",", ".")
    result = str(round(float(rate) * 1.01, 2))
    print("recommended tare ok")
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

        #Заповнюємо тип кріплення
        for item_connection in type_holder_list:
            self.type_holder.addItem(item_connection)

        self.item_value.addItem("?")

        self.code_value.addItem("?")

        self.length_value.addItem("?")

        #Обираємо тип кріплення
        self.type_holder.activated.connect(self.get_items)
        self.type_holder.setStyleSheet(style.type_holder_style)

        #Обираємо виріб
        self.item_value.activated.connect(self.get_code_items)

        #Oбираємо розмір
        self.code_value.activated.connect(self.get_item_length)


        self.add_item_button.clicked.connect(self.add_item_function)

        self.reset_button.clicked.connect(self.reset_function)



        # Блок роботи з валютою
        time_info = get_list_moment()
        rate = get_rate()
        self.euro_value.setText(rate)
        self.EURO_value.setText(get_recommended_rate_for_euro_value(rate))
        self.date_value.setText(time_info[0])
        self.time_label.setText(time_info[1])
        self.day.setText(time_info[2])

        self.holder_item: list = []
        self.refresh_rate_button.clicked.connect(self.refresh_rate)
        self.search_button.clicked.connect(self.search_item)

        #Створюємо invoice, у якому будуть лежати вироби (item)
        my_invoice = Invoice()

        #встановлюємо курс евро
        my_invoice.set_rate(self.EURO_value.text())

        #Загальна вага кг
        self.total_weight = 0.0

        #Максимальна довжина, см
        self.max_length = 0.0


        self.show()


    #Додаємо виріб до таблиці
    def add_item_function(self):
        self.new_item = Item()

        if self.type_holder.currentText() != "Оберіть тип кріплення" and \
            self.item_value.currentText() not in [" ", "Оберіть тип кріплення"] and \
            self.code_value.currentText() not in [" ", "?"] and \
            self.length_value.currentText() not in [" ", "?"] and\
            self.quantity_value.value() != 0:

            self.new_item.set_discount_item(self.discount_spinBox.value()) #знижка від tecnostamp

            data_list = [self.type_holder.currentText(),
                 self.item_value.currentText(),
                 self.code_value.currentText(),
                 self.length_value.currentText()]

            # code: str = My_db.get_full_code_item(
            #     [self.type_holder.currentText(),
            #      self.item_value.currentText(),
            #      self.code_value.currentText(),
            #      self.length_value.currentText()]
            # )

            code: str = My_db.get_full_code_item(data_list)
            print(code)
            data_list.append(code)

            dict_item = My_db.get_info_item(data_list)
            for k, v in dict_item.items():
                print(k, " ", v)
            print("############")
            # en_description: str = My_db.get_en_description(data_list)
            # ua_description: str = My_db.get_ua_description(data_list)
            # self.new_item.set_code_item(code) # Код виробу
            # self.new_item.set_amount_item(self.quantity_value.value())
            # self.new_item.set_en_name_item(en_description)
            # self.new_item.set_ua_name_item(ua_description)
            # print(f"Код  {self.new_item.get_code_item()}")
            # print(f"Кількість {self.new_item.get_amount_item()}")
            # print(f"EN: {self.new_item.get_en_name_item()} ")
            # print(f"UA: {self.new_item.get_ua_name_item()} ")

    #Скидаємо попередні параметри
    def reset_function(self):

        self.quantity_value.setValue(0)

        self.length_value.clear()
        self.length_value.addItem("?")

        self.code_value.clear()
        self.code_value.addItem("?")

        self.item_value.clear()
        self.item_value.addItem(type_holder_list[0])

        self.type_holder.clear()
        for item_connection in type_holder_list:
            self.type_holder.addItem(item_connection)


    def get_items(self) -> None:
        self.quantity_value.setValue(0)
        if category[self.type_holder.currentText()] == type_holder_list[0]:
            self.item_value.clear()
            self.item_value.addItem(type_holder_list[0])
        else:
            self.item_value.clear()
            for item in category[self.type_holder.currentText()]:
                self.item_value.addItem(item)


    def get_full_code(self):
        all_parameters: list = []
        all_parameters[0] = self.type_holder.currentText()
        all_parameters[1] = self.item_value.currentText()
        all_parameters[2] = self.code_value.currentText()
        all_parameters[3] = self.length_value.currentText()
        self.full_code = My_db.get_full_code_item(all_parameters)


    def get_code_items(self):
        self.quantity_value.setValue(0)
        if self.item_value.currentText() not in ["Оберіть виріб", "Оберіть тип кріплення", "?", " "]:
            self.length_value.clear()
            self.length_value.addItem("?")
            code_list: list = db_handler.My_db().get_code_list(
                [self.type_holder.currentText(), self.item_value.currentText()]
            )
            self.code_value.clear()
            for code_item in code_list:
                self.code_value.addItem(code_item)
        else:
            self.code_value.clear()
            self.code_value.setText("?")
            self.length_value.clear()
            self.length_value.addItem("?")


    def get_item_length(self) -> None:
        self.quantity_value.setValue(0)
        if self.code_value.currentText() not in [" ", "?"]:
            length_list: list =\
                db_handler.My_db().get_length_item([self.type_holder.currentText(),
                                                    self.item_value.currentText(),
                                                    self.code_value.currentText()])
            self.length_value.clear()
            for length_item in length_list:
                self.length_value.addItem(str(length_item))
        else:
            self.length_value.clear()
            self.length_value.addItem("?")


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
