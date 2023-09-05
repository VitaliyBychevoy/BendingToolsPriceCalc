import sys
import requests
from datetime import datetime, date
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import os
import shutil

import db_handler
import style
from vectortool_customers.customers_db import *
from model import Invoice, Item, Pre_commercial_offer
from db_handler import *
import mainwindow
from style import *

# from PyQt5.QtWidgets import QApplication, QMainWindow

acceptable_character = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "."]


def check_valid_symbols(number: str) -> bool:
    for letter in number:
        if letter not in acceptable_character:
            return False
    return True

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


# створюємо список з датою
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


# Отримуємо курс валюти з сайта мінфіна по міжбанку
def get_rate() -> str:
    rate = ""
    url = "https://minfin.com.ua/currency/mb/"
    try:
        request = requests.get(url)
        if request.status_code == 200:
            print(request.status_code)
            soup = BeautifulSoup(request.text, "html.parser")
            td_list = soup.find_all("td", "sc-1x32wa2-8 tWvco")
            rate_full_string = None
            for item in td_list:
                rate_full_string = item.find("div", {"class": "sc-1x32wa2-9 bKmKjX"}).text
            rate = rate_full_string[0:5]
            print("rate ok")
            return rate
        else:
            return "00.00"
    except requests.exceptions.ConnectionError:
        return "00.000"

def get_recommended_rate_for_euro_value(new_rate: str) -> str:
    rate = new_rate.replace(",", ".")
    result = str(round(float(rate) * 1.01, 2))
    print("recommended rate ok")
    rate_with_comma = result.replace(".", ",")
    return rate_with_comma


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        uic.loadUi("BendingPriceCalc.ui", self)

        self.setWindowIcon(QtGui.QIcon('data/logo_4.png'))
        self.setGeometry(50, 50, 820, 920)
        self.setFixedSize(820, 920)
        self.m_w = None
        self.table.setColumnWidth(0, 20)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 500)

        company_list: list = get_short_name_list()

        #Заповнюємо компанії
        for company in company_list:
            self.company_value.addItem(company)

        # Заповнюємо тип кріплення
        for item_connection in type_holder_list:
            self.type_holder.addItem(item_connection)

        self.item_value.addItem("?")

        self.code_value.addItem("?")

        self.length_value.addItem("?")

        # Обираємо тип кріплення
        self.type_holder.activated.connect(self.get_items)


        # Обираємо виріб
        self.item_value.activated.connect(self.get_code_items)

        # Oбираємо розмір
        self.code_value.activated.connect(self.get_item_length)

        #Кнопка. Додаємо новий виріб
        self.add_item_button.clicked.connect(self.add_item_function)

        #Кнопка. Скидаємо попередні поля та кількість
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

        # Створюємо invoice, у якому будуть лежати вироби (item)
        self.my_invoice = Invoice()

        # встановлюємо курс евро
        self.my_invoice.set_rate(self.EURO_value.text())

        # Максимальна довжина, см
        self.max_length = 0.0

        # Оформлення таблиці
        font_table = QtGui.QFont()
        #font_table.setFamily("Comic Sans MS")
        font_table.setFamily("Arial Narrow")
        font_table.setPointSize(12)
        self.table.setFont(font_table)

        #Шрифт для опису вироба
        self.font_table_1 = QtGui.QFont()
        #self.font_table_1.setFamily("Comic Sans MS")
        self.font_table_1.setFamily("Arial Narrow")
        self.font_table_1.setPointSize(12)

        self.font_table_2 = QtGui.QFont()
        #self.font_table_2.setFamily("Comic Sans MS")
        self.font_table_2.setFamily("Arial Narrow")
        self.font_table_2.setPointSize(16)


        #Поле для встановлення курсу
        self.EURO_value.textChanged.connect(self.check_number_EURO)

        #Додаємо один до кількості обраного елемента
        self.add_amount_button.clicked.connect(self.add_one_item)

        #Зменьшуємо на один кількость обраного елемента
        self.remove_amount_button.clicked.connect(self.remove_one_item)

        #Видаляємо обраний елемент
        self.remove_element.clicked.connect(self.remove_row)

        self.update_row.clicked.connect(self.update_item)

        #Видаляемо усе з таблиці
        self.clear_table_button.clicked.connect(self.clear_table)

        #Отримати рекомендований курс валюти
        self.recommended_rate_button.clicked.connect(self.recommended_rate)

        #Поле для вартості
        self.packing_value.textChanged.connect(self.check_packing_number)

        #Поле для вартості доставки
        self.delivery_value.textChanged.connect(self.check_delivery_number)

        #Кнопка Створити xlsx
        self.pre_commercial_offer_button.clicked.connect(self.create_pre_commercial_offer)


        self.show()

    def set_typical_style(self) -> None:
        #Списки та spinbox для редагування
        self.company_value.setStyleSheet(style.typically_style_QComboBox)
        self.company_value.setEnabled(True)
        self.type_holder.setStyleSheet(style.typically_style_QComboBox)
        self.item_value.setStyleSheet(style.typically_style_QComboBox)
        self.code_value.setStyleSheet(style.typically_style_QComboBox)
        self.length_value.setStyleSheet(style.typically_style_QComboBox)
        self.quantity_value.setStyleSheet(style.typically_style_QSpinBox)

        #Кнопки
        self.company_button.setStyleSheet(style.typically_style_company_button)
        self.company_button.setEnabled(True)
        self.reset_button.setStyleSheet(style.typically_style_button_reset_fields)
        self.reset_button.setEnabled(True)
        self.remove_element.setStyleSheet(style.typically_remove_element_button)
        self.remove_element.setEnabled(True)
        self.update_row.setStyleSheet(style.typically_update_row_button)
        self.update_row.setEnabled(True)
        self.db_button.setStyleSheet(style.typically_db_button)
        self.db_button.setEnabled(True)
        self.refresh_rate_button.setStyleSheet(style.typically_refresh_rate_button)
        self.refresh_rate_button.setEnabled(True)
        self.recommended_rate_button.setStyleSheet(style.typically_recommended_rate_button)
        self.refresh_rate_button.setEnabled(True)
        self.search_button.setStyleSheet(style.typically_search_button)
        self.search_button.setEnabled(True)
        self.add_amount_button.setStyleSheet(style.typically_update_row_button)
        self.add_amount_button.setEnabled(True)
        self.remove_amount_button.setStyleSheet(style.typically_update_row_button)
        self.remove_amount_button.setEnabled(True)
        self.clear_table_button.setStyleSheet(style.typically_style_button_reset_fields)
        self.clear_table_button.setEnabled(True)
        self.pre_commercial_offer_button.setStyleSheet(style.typically_xlsx_button)
        self.pre_commercial_offer_button.setEnabled(True)
        self.commercial_offer_button.setStyleSheet(style.typically_xlsx_button)
        self.commercial_offer_button.setEnabled(True)

        #таблиця
        self.table.setStyleSheet(style.typically_table)

        # загальний фон
        self.setStyleSheet(style.typically_style_background)

        # Поля
        self.EURO_value.setEnabled(True)
        self.EURO_value.setStyleSheet(style.typically_style_editline)
        self.packing_value.setEnabled(True)
        self.packing_value.setStyleSheet(style.typically_style_editline)
        self.delivery_value.setEnabled(True)
        self.delivery_value.setStyleSheet(style.typically_style_editline)

        #SpinBox
        self.persentage_spinBox.setStyleSheet(style.typically_persentage_spinBox)
        self.persentage_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.discount_spinBox.setStyleSheet(style.typically_persentage_spinBox)
        self.discount_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.discount_customer_spinBox.setStyleSheet(style.typically_persentage_spinBox)
        self.discount_customer_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.persentage_spinBox.setReadOnly(False)
        self.discount_spinBox.setReadOnly(False)
        self.discount_customer_spinBox.setReadOnly(False)

        #Курс валют
        self.date_euro_layout.setStyleSheet(style.typically_date_euro_layout)
        self.title.setStyleSheet(style.typically_title)
        self.date_value.setStyleSheet(style.typically_title)
        self.time_label.setStyleSheet(style.typically_title)
        self.day.setStyleSheet(style.typically_title)
        self.euro_value.setStyleSheet(style.typically_title)
        self.euro_label.setStyleSheet(style.typically_title)
        self.uah_label.setStyleSheet(style.typically_title)

        #для xls
        self.weight_label.setStyleSheet(style.typically_weight_label)
        self.weight_value.setStyleSheet(style.typically_weight_label)
        self.lenght_label.setStyleSheet(style.typically_weight_label)
        self.lenght_value.setStyleSheet(style.typically_weight_label)
        self.packing_label.setStyleSheet(style.typically_weight_label)
        self.packing_euro_label.setStyleSheet(style.typically_weight_label)
        self.comission_label.setStyleSheet(style.typically_weight_label)
        self.discount_customer_label.setStyleSheet(style.typically_weight_label)
        self.percent_label.setStyleSheet(style.typically_weight_label)
        self.percent_discount_customer_label.setStyleSheet(style.typically_weight_label)
        self.delivery_label.setStyleSheet(style.typically_weight_label)
        self.delivery_euro_label.setStyleSheet(style.typically_weight_label)
        self.discount_label.setStyleSheet(style.typically_weight_label)
        self.percent_discount_label.setStyleSheet(style.typically_weight_label)

    def set_update_style(self) -> None:
        #Списки та spinbox для редагування
        self.company_value.setStyleSheet(style.typically_style_QComboBox)
        self.company_value.setEnabled(False)
        self.type_holder.setStyleSheet(style.update_style_QComboBox)
        self.item_value.setStyleSheet(style.update_style_QComboBox)
        self.code_value.setStyleSheet(style.update_style_QComboBox)
        self.length_value.setStyleSheet(style.update_style_QComboBox)
        self.quantity_value.setStyleSheet(style.update_style_QSpinBox)

        #Кнопки
        self.company_button.setStyleSheet(style.update_style_company_button)
        self.company_button.setEnabled(False)
        self.reset_button.setStyleSheet(style.update_style_button)
        self.reset_button.setEnabled(False)
        self.remove_element.setStyleSheet(style.update_remove_element_button)
        self.remove_element.setEnabled(False)
        self.update_row.setStyleSheet(style.update_update_row_button)
        self.update_row.setEnabled(False)
        self.db_button.setStyleSheet(style.update_db_button)
        self.db_button.setEnabled(False)
        self.refresh_rate_button.setStyleSheet(style.update_refresh_rate_button)
        self.refresh_rate_button.setEnabled(False)
        self.recommended_rate_button.setStyleSheet(style.update_recommended_rate_button)
        self.refresh_rate_button.setEnabled(False)
        self.search_button.setStyleSheet(style.update_search_button)
        self.search_button.setEnabled(False)
        self.add_amount_button.setStyleSheet(style.update_update_row_button)
        self.add_amount_button.setEnabled(False)
        self.remove_amount_button.setStyleSheet(style.update_update_row_button)
        self.remove_amount_button.setEnabled(False)
        self.clear_table_button.setStyleSheet(style.update_style_button)
        self.clear_table_button.setEnabled(False)
        self.pre_commercial_offer_button.setStyleSheet(style.update_xlsx_button)
        self.pre_commercial_offer_button.setEnabled(False)
        self.commercial_offer_button.setStyleSheet(style.update_xlsx_button)
        self.commercial_offer_button.setEnabled(False)

        #таблиця
        self.table.setStyleSheet(style.update_table)

        #загальний фон
        self.setStyleSheet(style.update_style_background)

        #Поля
        self.EURO_value.setEnabled(False)
        self.EURO_value.setStyleSheet(style.update_style_editline)
        self.packing_value.setEnabled(False)
        self.packing_value.setStyleSheet(style.update_style_editline)
        self.delivery_value.setEnabled(False)
        self.delivery_value.setStyleSheet(style.update_style_editline)


        #SpinBox
        self.persentage_spinBox.setStyleSheet(style.update_persentage_spinBox)
        self.persentage_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.discount_spinBox.setStyleSheet(style.update_persentage_spinBox)
        self.discount_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.discount_customer_spinBox.setStyleSheet(style.update_persentage_spinBox)
        self.discount_customer_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.persentage_spinBox.setReadOnly(True)
        self.discount_spinBox.setReadOnly(True)
        self.discount_customer_spinBox.setReadOnly(True)

        #Курс валют
        self.date_euro_layout.setStyleSheet(style.update_date_euro_layout)
        self.title.setStyleSheet(style.update_title)
        self.date_value.setStyleSheet(style.update_title)
        self.time_label.setStyleSheet(style.update_title)
        self.day.setStyleSheet(style.update_title)
        self.euro_value.setStyleSheet(style.update_title)
        self.euro_label.setStyleSheet(style.update_title)
        self.uah_label.setStyleSheet(style.update_title)

        #для xls
        self.weight_label.setStyleSheet(style.update_weight_label)
        self.weight_value.setStyleSheet(style.update_weight_label)
        self.lenght_label.setStyleSheet(style.update_weight_label)
        self.lenght_value.setStyleSheet(style.update_weight_label)
        self.packing_label.setStyleSheet(style.update_weight_label)
        self.packing_euro_label.setStyleSheet(style.update_weight_label)
        self.comission_label.setStyleSheet(style.update_weight_label)
        self.discount_customer_label.setStyleSheet(style.update_weight_label)
        self.percent_label.setStyleSheet(style.update_weight_label)
        self.percent_discount_customer_label.setStyleSheet(style.update_weight_label)
        self.delivery_label.setStyleSheet(style.update_weight_label)
        self.delivery_euro_label.setStyleSheet(style.update_weight_label)
        self.discount_label.setStyleSheet(style.update_weight_label)
        self.percent_discount_label.setStyleSheet(style.update_weight_label)

    #Додаємо одиницю до кількості екземплярів виробу
    def add_one_item(self) -> None:
        row_index = self.table.currentRow()
        if row_index > -1:
            selected_code = self.table.model().index(row_index, 1).data()
            for item in self.my_invoice.get_list_item():
                if item.get_code_item() == selected_code:
                    item.set_amount_item(item.get_amount_item() + 1)
                    break
            self.load_data()
        else:
            self.load_data()

    #Зменьшуємо на одиницю кількість екземплярів виробу
    def remove_one_item(self) -> None:
        row_index = self.table.currentRow()

        if row_index > -1:
            selected_code = self.table.model().index(row_index, 1).data()
            for item in self.my_invoice.get_list_item():
                if item.get_code_item() == selected_code:
                    if item.get_amount_item() == 1:
                        self.my_invoice.remove_item_from_list(selected_code)
                    else:
                        item.set_amount_item(item.get_amount_item() - 1)
                    break
            self.load_data()
        else:
            pass

    #Видаляємо позицію вироба зі списка та з таблиці
    def remove_row(self) -> None:
        row_index = self.table.currentRow()
        if len(self.my_invoice.get_list_item()) == 1:
            self.clear_table()
        else:
            if row_index > -1:
                if len(self.my_invoice.get_list_item()) == 1:
                    self.clear_table()
                selected_code = self.table.model().index(row_index, 1).data()
                self.my_invoice.remove_item_from_list(selected_code)
                self.load_data()
            else:
                pass

    # Додаємо виріб до таблиці
    def add_item_function(self):

        # self.set_typical_style()
        # self.new_item = Item()

        if self.type_holder.currentText() == "Оберіть тип кріплення" or \
            self.item_value.currentText() in ["Оберіть виріб", " ", "","Оберіть тип кріплення"] or \
            self.code_value.currentText() in [" ", "?"] or \
            self.length_value.currentText() in [" ", "?"] or \
            self.quantity_value.value() == 0:

            error_message = ""
            if self.type_holder.currentText() == "Оберіть тип кріплення":
                error_message += "Оберіть тип кріплення\n"
            if self.item_value.currentText() in ["Оберіть виріб", " ", "","Оберіть тип кріплення","?"]:
                error_message += "Оберіть виріб\n"
            if self.code_value.currentText() in [" ", "?"]:
                error_message += "Оберіть код виробу\n"
            if self.length_value.currentText() in [" ", "?"]:
                error_message += "Оберіть довжину виробу\n"
            if self.quantity_value.value() == 0:
                error_message += "Оберіть кількість виробу"

            error = MessageError()
            error.setText(error_message)
            error.exec_()
        else:
            self.set_typical_style()
            self.new_item = Item()

            if self.type_holder.currentText() != "Оберіть тип кріплення" and \
                    self.item_value.currentText() == "Оберіть виріб" and \
                    self.code_value.currentText() not in [" ", "?"] and \
                    self.length_value.currentText() not in [" ", "?"]:

                print("Hello! I`m bug")
                self.load_data()

            if self.type_holder.currentText() != "Оберіть тип кріплення" and \
                    self.item_value.currentText() not in [" ", "Оберіть тип кріплення", "Оберіть виріб"] and \
                    self.code_value.currentText() not in [" ", "?"] and \
                    self.length_value.currentText() not in [" ", "?"] and \
                    self.quantity_value.value() != 0:

                data_list = [self.type_holder.currentText(),
                             self.item_value.currentText(),
                             self.code_value.currentText(),
                             self.length_value.currentText()]

                code: str = My_db.get_full_code_item(data_list)
                data_list.append(code)
                dict_item = My_db.get_info_item(data_list)

                print("############")
                self.new_item.set_type_holder(dict_item["type_holder"])
                self.new_item.set_type_item(dict_item["item"])
                self.new_item.set_code_item(dict_item["code_item"])
                self.new_item.set_en_name_item(dict_item["en_name_item"])
                self.new_item.set_ua_name_item(dict_item["ua_name_item"])
                self.new_item.set_length_item(dict_item["length_item"])
                self.new_item.set_image_path(dict_item["image_path"])
                length_str = My_db.get_length(dict_item["length_item"])

                self.new_item.set_length_item_mm(length_str)
                self.new_item.set_weight_item(dict_item["weight"])
                self.new_item.set_price_item(dict_item["price_item"])
                self.new_item.set_discount_item(self.discount_spinBox.value())
                self.new_item.set_amount_item(self.quantity_value.value())
                print(self.new_item.get_type_holder())
                print(self.new_item.get_type_item())
                print(self.new_item.get_code_item())
                print(f"Довжина {self.new_item.get_length_item_mm()} мм")
                print(f"Кількість: {self.new_item.get_amount_item()} шт")
                print("%%%%%%%%%%%%%%%")

                if not self.my_invoice.get_list_item():
                    print("Список порожній")
                    self.my_invoice.add_item_to_list(self.new_item)

                else:

                    if self.new_item.get_code_item() in self.my_invoice.get_list_code():
                        print("Вже існує")
                        for i in range(0, len(self.my_invoice.get_list_item())):
                            if self.my_invoice.get_list_item()[i].get_code_item() == self.new_item.get_code_item():
                                amount: int = int(self.new_item.get_amount_item()) + \
                                              int(self.my_invoice.get_list_item()[i].get_amount_item())
                                self.my_invoice.get_list_item()[i].set_amount_item(amount)
                                self.my_invoice.set_total_weight()
                                break
                    else:
                        print("Додаємо новий виріб")
                        self.my_invoice.add_item_to_list(self.new_item)
                self.my_invoice.show_list()
                self.my_invoice.set_total_weight()
                self.my_invoice.set_max_length()
                self.weight_value.setText(str(self.my_invoice.get_total_weight()) + " кг")
                self.lenght_value.setText(str(self.my_invoice.get_max_length()) + " см")

            else:
                print("Помилка")
            self.load_data()

    #Редагуємо обрану позицію
    def update_item(self) -> None:
        print("Update")
        row_index = self.table.currentRow()
        if row_index > -1:
            print(f"row index: {row_index}")
            print(f"Items: {len(self.my_invoice.get_list_item())}")
            selected_code = self.table.model().index(row_index, 1).data()
            print(selected_code)
            if len(self.my_invoice.get_list_item()) == 1:
                self.type_holder.setCurrentText(self.my_invoice.get_list_item()[0].get_type_holder())
                self.item_value.setCurrentText(self.my_invoice.get_list_item()[0].get_type_item())
                self.code_value.setCurrentText(self.my_invoice.get_list_item()[0].get_code_item())
                self.length_value.setCurrentText(self.my_invoice.get_list_item()[0].get_length_item())
                self.quantity_value.setValue(self.my_invoice.get_list_item()[0].get_amount_item())
                self.my_invoice.set_list_item([])
            else:
                for index_item in range(0, len(self.my_invoice.get_list_item())):
                    if self.my_invoice.get_list_item()[index_item].get_code_item() == selected_code:
                        self.type_holder.setCurrentText(self.my_invoice.get_list_item()[index_item].get_type_holder())
                        self.item_value.setCurrentText(self.my_invoice.get_list_item()[index_item].get_type_item())
                        self.code_value.setCurrentText(self.my_invoice.get_list_item()[index_item].get_code_item())
                        self.length_value.setCurrentText(self.my_invoice.get_list_item()[index_item].get_length_item())
                        self.quantity_value.setValue(self.my_invoice.get_list_item()[index_item].get_amount_item())
                        self.remove_row()
                        break
            self.set_update_style()
        else:
            pass

    # Скидаємо попередні параметри
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

    # Завантаження списка виробів для пувного типа тримача
    def get_items(self) -> None:
        self.quantity_value.setValue(0)

        if category[self.type_holder.currentText()] == type_holder_list[0]:
            self.item_value.clear()
            self.item_value.addItem(type_holder_list[0])
            self.code_value.clear()
            self.code_value.addItem("?")
            self.length_value.clear()
            self.length_value.addItem("?")
        else:
            self.item_value.clear()
            for item in category[self.type_holder.currentText()]:
                self.item_value.addItem(item)

    # Завантажуємо данні з об'єкта до у таблицю
    def load_data(self) -> None:
        if self.my_invoice is not None:
            print(len(self.my_invoice.get_list_item()))
            self.table.setRowCount(len(self.my_invoice.get_list_item()))
            for i in range(0, len(self.my_invoice.get_list_item())):
                self.table.setRowHeight(i, 50)

                self.table.setItem(i, 0, QTableWidgetItem(str(i + 1)))

                self.table.item(i, 0).setTextAlignment(QtCore.Qt.AlignCenter)

                self.table.item(i, 0).setFlags(self.table.item(i, 0, ).flags() & ~ QtCore.Qt.ItemIsEditable)

                self.table.setItem(i, 1, QTableWidgetItem(self.my_invoice.get_list_item()[i].get_code_item()))

                self.table.item(i, 1).setTextAlignment(QtCore.Qt.AlignCenter)

                self.table.item(i, 1).setFlags(self.table.item(i, 1, ).flags() & ~ QtCore.Qt.ItemIsEditable)

                # self.table.setItem(i, 2, QTableWidgetItem(self.my_invoice.get_list_item()[i].get_ua_name_item()))
                self.table.setItem(i, 2, QTableWidgetItem(self.my_invoice.get_list_item()[i].get_name_for_table()))

                self.table.item(i, 2).setFlags(self.table.item(i, 2, ).flags() & ~ QtCore.Qt.ItemIsEditable)
                self.table.item(i, 2).setFont(self.font_table_1)
                self.table.setItem(i, 3, QTableWidgetItem(str(self.my_invoice.get_list_item()[i].get_amount_item())))

                self.table.item(i, 3).setTextAlignment(QtCore.Qt.AlignCenter)

                self.table.item(i, 3).setFlags(self.table.item(i, 3, ).flags() & ~ QtCore.Qt.ItemIsEditable)
                self.table.item(i, 3).setFont(self.font_table_2)
        else:
            pass
        self.my_invoice.set_total_weight()
        self.my_invoice.set_max_length()
        self.weight_value.setText(str(self.my_invoice.get_total_weight()) + " кг")
        self.lenght_value.setText(str(self.my_invoice.get_max_length()) + " см")

    # Отримання повного кода виробу з урахуванням довжини
    def get_full_code(self):
        all_parameters: list = []
        all_parameters[0] = self.type_holder.currentText()
        all_parameters[1] = self.item_value.currentText()
        all_parameters[2] = self.code_value.currentText()
        all_parameters[3] = self.length_value.currentText()
        self.full_code = My_db.get_full_code_item(all_parameters)
        del(all_parameters)

    # Завантаження списку кодів виробу без урахування довжини
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

        elif self.type_holder.currentText() != "Оберіть тип кріплення" and self.item_value.currentText() == "Оберіть тип кріплення":
            self.code_value.clear()
            self.code_value.addItem("?")
            self.length_value.clear()
            self.length_value.addItem("?")
        else:
            self.code_value.clear()
            self.code_value.addItem("?")
            self.length_value.clear()
            self.length_value.addItem("?")

    # Завантаження списку довжин для певного кода виробу
    def get_item_length(self) -> None:
        self.quantity_value.setValue(0)
        if self.code_value.currentText() not in [" ", "?"]:
            length_list: list = \
                db_handler.My_db().get_length_item([self.type_holder.currentText(),
                                                    self.item_value.currentText(),
                                                    self.code_value.currentText()])
            self.length_value.clear()
            for length_item in length_list:
                self.length_value.addItem(str(length_item))
        else:
            self.length_value.clear()
            self.length_value.addItem("?")

    # Оновлення дати запита та курса
    def refresh_rate(self) -> None:
        time_info = get_list_moment()
        self.date_value.setText(time_info[0])
        self.time_label.setText(time_info[1])
        self.day.setText(time_info[2])
        self.euro_value.setText(get_rate())

    def clear_table(self) -> None:
        self.table.setRowCount(0)
        self.my_invoice.set_list_item([])
        self.my_invoice.set_total_weight()
        self.my_invoice.set_max_length()
        self.weight_value.setText(str(self.my_invoice.get_total_weight()))
        self.lenght_value.setText(str(self.my_invoice.get_max_length()))

    def recommended_rate(self) -> None:
        rate: str = self.euro_value.text().replace(",", ".")
        self.EURO_value.setText(str(round(float(rate) * 1.01, 2)))

    @staticmethod
    def new_check_number(new_number: str) -> str:
        result: str = ""

        count_comma: int = new_number.count(",")

        if check_valid_symbols(new_number):
            current_number = new_number.replace(".", ",")
            if count_comma > 0:
                for number in current_number:
                    if number == "," and "," in result:
                        continue
                    result += number
                return result
            else:
                return new_number.replace(".", ",")
        else:
            for number in new_number:
                if number not in acceptable_character:
                    continue
                else:
                    result += number
            return result

    def check_number_EURO(self) -> None:
        self.EURO_value.setText(self.new_check_number(self.EURO_value.text()))

    def check_packing_number(self) -> None:
        self.packing_value.setText(self.new_check_number(self.packing_value.text()))

    def check_delivery_number(self) -> None:
        self.delivery_value.setText(self.new_check_number(self.delivery_value.text()))

    # Кнопка створення пошукового вікна
    def search_item(self) -> None:
        self.m_w = Search()
        self.m_w.show()

    # Кнопка створення попередньої таблиці
    def create_pre_commercial_offer(self) -> None:
        print("Pre commercial offer")
        #if self.company_name.text() in ["", " "] or \
        if self.company_value.currentText() == "Оберіть компанію" or\
                self.EURO_value.text() in ["", " ", "00,000", "0,0", "0"] or \
                self.table.rowCount() < 1 or \
                self.packing_value.text() in ["", " ", "00,000", "0,0", "0"] or \
                self.delivery_value.text() in ["", " ", "00,000", "0,0", "0"]:
            error = MessageError()
            error_message: str = ""
           # if self.company_name.text() in ["", " "]:
            if self.company_value.currentText() == "Оберіть компанію":
                error_message += "Вкажіть назву компанії клієтна.\n"
            if self.EURO_value.text() in ["", " ", "00,000", "0,0", "0"]:
                error_message += "Вкажіть курс EURO.\n"
            if self.table.rowCount() < 1:
                error_message += "Додайте хочаб один виріб.\n"
            if self.packing_value.text() in ["", " ", "00,000", "0,0", "0"]:
                error_message += "Зазначте вартість пакування.\n"
            if self.delivery_value.text() in ["", " ", "00,000", "0,0", "0"]:
                error_message += "Зазначте вартість доставки."
            error.setText(error_message)
            error.exec_()
        else:
            print("Let`s create pre commercial offer")

            self.pco = Pre_commercial_offer()
            #self.pco.set_company_name(self.company_name.text())
            self.pco.set_company_name(self.company_value.currentText())
            self.pco.set_rate(new_rate=self.EURO_value.text())
            self.pco.set_discount(self.discount_spinBox.value())
            #self.pco.set_path_temp(f"data/ТКП {self.pco.get_company_name()} I{self.time_label.text().replace(':', '_')}I {self.date_value.text().replace(':', '_')}.xlsx")
            self.pco.set_path_temp(
                f"data/ТКП {self.pco.get_company_name()} I{self.time_label.text().replace(':', '_')}I {self.date_value.text().replace(':', '_')}.xlsx")
            # Копиюєм попередній порожній зразок комерційної пропозиції
            shutil.copy("data/Зразок ТКП.xlsx", self.pco.get_path_temp())



            #Заповнюємо новий файл
            self.pco.fill_xlsx(self.my_invoice)
            #

class MessageError(QMessageBox):
    font_message = QtGui.QFont()
    font_message.setFamily("Arial Narrow")
    font_message.setPointSize(14)
    def __init__(self):
        super(MessageError, self).__init__()
        self.setWindowIcon(QtGui.QIcon('data/logo_4.png'))
        self.setStyleSheet(typically_style_background)
        self.setWindowTitle("Помилка")
        self.setFont(self.font_message)
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Ok)
        self.button(QMessageBox.Ok).setVisible(False)


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
