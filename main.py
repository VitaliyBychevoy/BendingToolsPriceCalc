import sys
import requests
from datetime import datetime, date
from bs4  import BeautifulSoup
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import PIL


#import db_handler
import style

from db_handler import *
from BendingPreCommercialOffer import *
from style import *
from db_handler import *



acceptable_character = \
    ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", ".")

zero_spinBox = ("", " ", "00,000", "00,00", "0,0", "0")

empty_value = (" ", "?")


def check_valid_symbols(number: str) -> bool:
    """Функція отримує строку та первіряє кожен символ
    чи є він валідний. Вертає False у разі якщо символ не сприйнятний.
    Якщо усі символи сприйнятні вертає True."""
    for letter in number:
        if letter not in acceptable_character:
            return False
    return True

type_holder_list = (
    "Оберіть тип кріплення",
    "Amada-promecam",
    "Trumpf-Wila",
    "Bystronic",
    "Universal"
)

item_list_amada = (
    "Оберіть виріб",
    "Пуансон",
    "Матриця одноручова",
    "Пуансон плющення",
    "Матриця плющення",
    "Матриця багаторучова",
    "Тримач радіусних вставок",
    "Тримач поліуретанової вставки",
    #"Тримач пуансона",
    #"Прижимні планки",
    #"Тримач матриці",
    #"Радіусна вставка",
)

item_list_trumpf_wila = (
    "Оберіть виріб",
    "Пуансон",
    "Матриця одноручова",
    "Пуансон плющення",
    "Матриця плющення",
    "Кнопка",
    "Штіфт",
    "Тримач поліуретанової вставки"
)


item_list_bystronic = (
    "Пуансон",
    "Матриця одноручова",
)

item_list_universal = (
    "Оберіть виріб",
    "Радіусна вставка",
    "Уретанова вставка матриці",
    "Прямокутна вставка пуансона",
)

category = {
    type_holder_list[0]: type_holder_list[0],
    type_holder_list[1]: item_list_amada,
    type_holder_list[2]: item_list_trumpf_wila,
    type_holder_list[3]: item_list_trumpf_wila[0:5],
    type_holder_list[4]: item_list_universal
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


# створюємо кортеж з датою
def get_list_moment() -> tuple:
    """Функція повертає кортеж у вигляді
    (поточна дата, поточний час, день тижня)"""

    request_moment_1 = datetime.now()
    moment = str(request_moment_1)
    day = date.today().isoweekday()
    moment_list = moment.split(" ")
    date_list = moment_list[0].split("-")
    date_str = ":".join(date_list[::-1])
    time_list = moment_list[1].split(":")
    time_string = time_list[0] + ":" + time_list[1]
    list_result = [date_str, time_string, week_day[day]]
    return tuple(list_result)


# Отримуємо курс валюти з сайта мінфіна по міжбанку
def get_rate() -> str:
    """Функція парсить сайт minfin отримує вартість покупки euro
    та вертає  її як строку """

    rate = ""
    url = "https://minfin.com.ua/currency/mb/"
    try:
        request = requests.get(url)
        if request.status_code == 200:
            soup = BeautifulSoup(request.text, "html.parser")
            td_list = soup.find_all("td", "sc-1x32wa2-8 tWvco")
            rate_full_string = None
            for item in td_list:
                rate_full_string = item.find("div", {"class": "sc-1x32wa2-9 bKmKjX"}).text
            rate = rate_full_string[0:5]
            return rate
        else:
            return "00.00"
    except requests.exceptions.ConnectionError:
        return "00.000"


def get_recommended_rate_for_euro_value(new_rate: str) -> str:
    """Функція  отримує строку яка містить вартість покупки euro
    та вертає збільшену вартість на один відсоток у вигяді строки"""
    rate = new_rate.replace(",", ".")
    result = str(round(float(rate) * 1.01, 2))
    rate_with_comma = result.replace(".", ",")
    return rate_with_comma


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        #uic.loadUi("data/BendingPriceCalc.ui", self)
        uic.loadUi("BendingPriceCalc.ui", self)
        self.setWindowIcon(QtGui.QIcon('data/logo_4.png'))
        self.setGeometry(50, 50, 1500, 960)
        self.setFixedSize(1500, 960)

        #self.m_w = None  # Вікно пошуку
        # self.customers = None  # Вікно для створення клієнтів
        # self.mdi = QMdiArea()
        self.table.setColumnWidth(0, 20)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 500)

        self.book = MyDb.open_book("data/DB_bending.xlsx")



        # Приховуємо результати
        self.hide_result()

        # Заповнюємо компанії
        company_list: list = get_short_name_list()

        for company in company_list:
            self.company_value.addItem(company)

        # Заповнюємо тип кріплення
        for item_connection in type_holder_list:
            self.type_holder.addItem(item_connection)

        # Заповнюємо тип кріплення для пошуку пуансона та матриці
        self.type_punch_value.addItem("")
        self.type_die_value.addItem("")
        for holder in (
                "Amada-promecam",
                "Trumpf-Wila",
                "Bystronic",
        ):
            self.type_punch_value.addItem(holder)
            self.type_die_value.addItem(holder)

        self.item_value.addItem("?")

        self.code_value.addItem("?")

        self.length_value.addItem("?")

        # Обираємо тип кріплення
        self.type_holder.activated.connect(self.get_items)

        # Обираємо виріб
        self.item_value.activated.connect(self.get_code_items)

        # Oбираємо розмір
        self.code_value.activated.connect(self.get_item_length)

        # Кнопка. Додаємо новий виріб
        self.add_item_button.clicked.connect(self.add_item_function)

        # Кнопка. Скидаємо попередні поля та кількість
        self.reset_button.clicked.connect(self.reset_function)

        # Блок роботи з валютою
        time_info = get_list_moment()
        rate = get_rate()
        self.euro_value.setText(rate)
        self.EURO_value.setText(
            get_recommended_rate_for_euro_value(rate)
        )
        self.date_value.setText(time_info[0])
        self.time_label.setText(time_info[1])
        self.day.setText(time_info[2])

        self.holder_item: list = []
        self.refresh_rate_button.clicked.connect(self.refresh_rate)

        # Створюємо invoice, у якому будуть лежати вироби (item)
        self.my_invoice = Invoice()

        # Максимальна довжина, см
        self.max_length = 0.0

        # Оформлення таблиці
        font_table = QtGui.QFont()

        font_table.setFamily("Arial Narrow")
        font_table.setPointSize(12)
        self.table.setFont(font_table)

        # Шрифт для опису вироба
        self.font_table_1 = QtGui.QFont()

        self.font_table_1.setFamily("Arial Narrow")
        self.font_table_1.setPointSize(12)

        self.font_table_2 = QtGui.QFont()

        self.font_table_2.setFamily("Arial Narrow")
        self.font_table_2.setPointSize(16)

        # Поле для встановлення курсу
        self.EURO_value.textChanged.connect(self.check_number_EURO)

        # Додаємо один до кількості обраного елемента
        self.add_amount_button.clicked.connect(self.add_one_item)

        # Зменьшуємо на один кількость обраного елемента
        self.remove_amount_button.clicked.connect(self.remove_one_item)

        # Видаляємо обраний елемент
        self.remove_element.clicked.connect(self.remove_row)

        #Кнопка корегування позиції
        self.update_row.clicked.connect(self.update_item)

        # Видаляемо усе з таблиці
        self.clear_table_button.clicked.connect(self.clear_table)

        # Отримати рекомендований курс валюти
        self.recommended_rate_button.clicked.connect(self.recommended_rate)

        # Поле для вартості пакування
        self.packing_value.textChanged.connect(self.check_packing_number)

        # Поле для вартості доставки
        self.delivery_value.textChanged.connect(self.check_delivery_number)

        # Кнопка Створити xlsx
        self.pre_commercial_offer_button.clicked.connect(self.create_pre_commercial_offer)

        # Кнопка Розрахувати вартість
        self.result_button.clicked.connect(self.show_result)

        # Вартість переводу
        self.transaction_value.textChanged.connect(self.check_transaction_value)

        # Податок банка
        self.bank_tax_value.textChanged.connect(self.check_bank_tax_value)

        # Брокерські послуги
        self.brokerage_services_value.textChanged.connect(self.check_brokerage_services_value)

        # Вартість оформлення документів
        self.delivery_document_value.textChanged.connect(self.check_delivery_document_value)

        # Вартість оформлення документів EURO-1
        self.delivery_document_EURO_1_value_.textChanged.connect(
            self.check_delivery_document_EURO_1_value_
        )

        # РОБОТА З КЛІЄНТАМИ

        # Кнопка отримання повної назви клієнта
        self.get_full_name_Button.clicked.connect(self.get_full_name_customer)

        # Кнопка скидання короткої назви
        self.reset_short_name_Button.clicked.connect(self.reset_short_name)

        # Кнопка скидання повної назви
        self.reset_full_name_Button.clicked.connect(self.reset_full_name)

        # Кнопка отримання усіх коротких назв клієнтів
        self.all_customers_Button.clicked.connect(self.show_all_short_name)

        # Обираємо позицію у списку коротких назв
        self.list_customer_comboBox.activated.connect(self.get_itemBox_info)

        # Змінюємо запис клієнта у базі
        self.update_customer_Button.clicked.connect(self.update_client)

        #Додаємо нову компанію
        self.add_customer_Button.clicked.connect(self.add_client)

        #Видалення з бази
        self.delete_customer_Button.clicked.connect(self.delete_client)

        # ПОШУК
        #Пуансон

        #Робимо зображення порожнім
        self.set_empty_punch_image()

        #Обробка результатів списка пошуку пуансонів
        self.result_punch_value.activated.connect(self.get_one_punch_info)

        #Зміна стану поля "Тип"
        self.type_punch_value.activated.connect(self.change_type_punch)

        #Кнопка пошуку пуансона
        self.find_punch_button.clicked.connect(self.find_punch)

        #Порожня інформація пуансона
        self.punch_info.setText("")

        #Прожня інформація довжин пуансонів
        self.length_info_punch_label.setText("")

        #Пошук матриці

        #Зміна стану поля "Тип"
        self.type_die_value.activated.connect(self.change_type_die)

        #Порожнє зображення матриці
        self.set_empty_die_image()

        #Обробка кнопки Підібрати матрицю
        self.find_die_button.clicked.connect(self.find_die)

        #Обробка результата списка пошуку матриці
        self.result_die_value.activated.connect(self.get_one_die_info)

    #  self.show()

    #def customers_db(self):
    #    self.customers = CustomerWindow()
    #    self.customers.show()

    def set_typical_style(self) -> None:
        # Списки та spinbox для редагування
        self.company_value.setStyleSheet(style.typically_style_QComboBox)
        self.company_value.setEnabled(True)
        self.type_holder.setStyleSheet(style.typically_style_QComboBox)
        self.item_value.setStyleSheet(style.typically_style_QComboBox)
        self.code_value.setStyleSheet(style.typically_style_QComboBox)
        self.length_value.setStyleSheet(style.typically_style_QComboBox)
        self.quantity_value.setStyleSheet(style.typically_style_QSpinBox)

        # Кнопки
        self.reset_button.setStyleSheet(style.typically_style_button_reset_fields)
        self.reset_button.setEnabled(True)
        self.remove_element.setStyleSheet(style.typically_remove_element_button)
        self.remove_element.setEnabled(True)
        self.update_row.setStyleSheet(style.typically_update_row_button)
        self.update_row.setEnabled(True)
        self.refresh_rate_button.setStyleSheet(style.typically_refresh_rate_button)
        self.refresh_rate_button.setEnabled(True)
        self.recommended_rate_button.setStyleSheet(style.typically_recommended_rate_button)
        self.refresh_rate_button.setEnabled(True)
        self.add_amount_button.setStyleSheet(style.typically_update_row_button)
        self.add_amount_button.setEnabled(True)
        self.remove_amount_button.setStyleSheet(style.typically_update_row_button)
        self.remove_amount_button.setEnabled(True)
        self.clear_table_button.setStyleSheet(style.typically_style_button_reset_fields)
        self.clear_table_button.setEnabled(True)
        self.pre_commercial_offer_button.setStyleSheet(style.typically_xlsx_button)
        self.pre_commercial_offer_button.setEnabled(True)

        # таблиця
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
        self.brokerage_services_value.setEnabled(True)
        self.brokerage_services_value.setStyleSheet(style.typically_style_editline)
        self.brokerage_services_value.setEnabled(True)
        self.brokerage_services_value.setStyleSheet(style.typically_style_editline)

        self.delivery_document_value.setEnabled(True)
        self.delivery_document_value.setStyleSheet(style.typically_style_editline)

        self.delivery_document_EURO_1_value_.setEnabled(True)
        self.delivery_document_EURO_1_value_.setStyleSheet(style.typically_style_editline)

        self.transaction_value.setEnabled(True)
        self.transaction_value.setStyleSheet(style.typically_style_editline)
        self.bank_tax_value.setEnabled(True)
        self.bank_tax_value.setStyleSheet(style.typically_style_editline)

        # SpinBox
        self.persentage_spinBox.setStyleSheet(style.typically_persentage_spinBox)
        self.persentage_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.provider_discount_spinBox.setStyleSheet(style.typically_persentage_spinBox)
        self.provider_discount_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.discount_customer_spinBox.setStyleSheet(style.typically_persentage_spinBox)
        self.discount_customer_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.persentage_spinBox.setReadOnly(False)
        self.provider_discount_spinBox.setReadOnly(False)
        self.discount_customer_spinBox.setReadOnly(False)

        # Курс валют
        self.date_euro_layout.setStyleSheet(style.typically_date_euro_layout)
        self.title.setStyleSheet(style.typically_title)
        self.date_value.setStyleSheet(style.typically_title)
        self.time_label.setStyleSheet(style.typically_title)
        self.day.setStyleSheet(style.typically_title)
        self.euro_value.setStyleSheet(style.typically_title)
        self.euro_label.setStyleSheet(style.typically_title)
        self.uah_label.setStyleSheet(style.typically_title)

        # для xls
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

        self.delivery_document_label.setStyleSheet(style.typically_weight_label)
        self.delivery_document_label_2.setStyleSheet(style.typically_weight_label)

        self.delivery_euro_label.setStyleSheet(style.typically_weight_label)
        self.delivery_document_euro_1_label.setStyleSheet(style.typically_weight_label)
        self.discount_label.setStyleSheet(style.typically_weight_label)
        self.bank_tax_label.setStyleSheet(style.typically_weight_label)
        self.delivery_document_euro_label.setStyleSheet(style.typically_weight_label)
        self.brokerage_services_uah_label.setStyleSheet(style.typically_weight_label)
        self.transaction_label.setStyleSheet(style.typically_weight_label)
        self.brokerage_services_label.setStyleSheet(style.typically_weight_label)
        self.transaction_uah_label.setStyleSheet(style.typically_weight_label)
        self.discount_label.setStyleSheet(style.typically_weight_label)
        self.percent_bank_tax_label.setStyleSheet(style.typically_weight_label)
        self.percent_discount_label.setStyleSheet(style.typically_weight_label)

    #Функція оформлення під час корегування
    def set_update_style(self) -> None:
        # Списки та spinbox для редагування
        self.company_value.setStyleSheet(style.typically_style_QComboBox)
        self.company_value.setEnabled(False)
        self.type_holder.setStyleSheet(style.update_style_QComboBox)
        self.item_value.setStyleSheet(style.update_style_QComboBox)
        self.code_value.setStyleSheet(style.update_style_QComboBox)
        self.length_value.setStyleSheet(style.update_style_QComboBox)
        self.quantity_value.setStyleSheet(style.update_style_QSpinBox)

        # Кнопки
        self.reset_button.setStyleSheet(style.update_style_button)
        self.reset_button.setEnabled(False)
        self.remove_element.setStyleSheet(style.update_remove_element_button)
        self.remove_element.setEnabled(False)
        self.update_row.setStyleSheet(style.update_update_row_button)
        self.update_row.setEnabled(False)
        self.refresh_rate_button.setStyleSheet(style.update_refresh_rate_button)
        self.refresh_rate_button.setEnabled(False)
        self.recommended_rate_button.setStyleSheet(style.update_recommended_rate_button)
        self.refresh_rate_button.setEnabled(False)
        self.add_amount_button.setStyleSheet(style.update_update_row_button)
        self.add_amount_button.setEnabled(False)
        self.remove_amount_button.setStyleSheet(style.update_update_row_button)
        self.remove_amount_button.setEnabled(False)
        self.clear_table_button.setStyleSheet(style.update_style_button)
        self.clear_table_button.setEnabled(False)
        self.pre_commercial_offer_button.setStyleSheet(style.update_xlsx_button)
        self.pre_commercial_offer_button.setEnabled(False)

        # таблиця
        self.table.setStyleSheet(style.update_table)

        # загальний фон
        self.setStyleSheet(style.update_style_background)

        # Поля
        self.EURO_value.setEnabled(False)
        self.EURO_value.setStyleSheet(style.update_style_editline)
        self.packing_value.setEnabled(False)
        self.packing_value.setStyleSheet(style.update_style_editline)
        self.delivery_value.setEnabled(False)
        self.delivery_value.setStyleSheet(style.update_style_editline)
        self.delivery_document_value.setEnabled(False)
        self.delivery_document_value.setStyleSheet(style.update_style_editline)
        self.brokerage_services_value.setEnabled(False)
        self.brokerage_services_value.setStyleSheet(style.update_style_editline)
        self.bank_tax_value.setEnabled(False)
        self.bank_tax_value.setStyleSheet(style.update_style_editline)
        self.transaction_value.setEnabled(False)
        self.transaction_value.setStyleSheet(style.update_style_editline)
        self.delivery_document_value.setEnabled(False)
        self.delivery_document_value.setStyleSheet(style.update_style_editline)
        self.delivery_document_EURO_1_value_.setEnabled(False)
        self.delivery_document_EURO_1_value_.setStyleSheet(style.update_style_editline)

        # SpinBox
        self.persentage_spinBox.setStyleSheet(style.update_persentage_spinBox)
        self.persentage_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.provider_discount_spinBox.setStyleSheet(style.update_persentage_spinBox)
        self.provider_discount_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.discount_customer_spinBox.setStyleSheet(style.update_persentage_spinBox)
        self.discount_customer_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.persentage_spinBox.setReadOnly(True)
        self.provider_discount_spinBox.setReadOnly(True)
        self.discount_customer_spinBox.setReadOnly(True)

        # Курс валют
        self.date_euro_layout.setStyleSheet(style.update_date_euro_layout)
        self.title.setStyleSheet(style.update_title)
        self.date_value.setStyleSheet(style.update_title)
        self.time_label.setStyleSheet(style.update_title)
        self.day.setStyleSheet(style.update_title)
        self.euro_value.setStyleSheet(style.update_title)
        self.euro_label.setStyleSheet(style.update_title)
        self.uah_label.setStyleSheet(style.update_title)

        # для xls
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

        # self.delivery_label.setStyleSheet(style.update_weight_label)
        self.delivery_document_label.setStyleSheet(style.update_weight_label)
        self.delivery_document_label_2.setStyleSheet(style.update_weight_label)

        self.delivery_euro_label.setStyleSheet(style.update_weight_label)
        self.delivery_document_euro_1_label.setStyleSheet(style.update_weight_label)
        self.transaction_uah_label.setStyleSheet(style.update_weight_label)
        self.delivery_document_euro_label.setStyleSheet(style.update_weight_label)
        self.brokerage_services_uah_label.setStyleSheet(style.update_weight_label)
        self.bank_tax_label.setStyleSheet(style.update_weight_label)
        self.transaction_label.setStyleSheet(style.update_weight_label)
        self.brokerage_services_label.setStyleSheet(style.update_weight_label)
        self.discount_label.setStyleSheet(style.update_weight_label)
        self.percent_discount_label.setStyleSheet(style.update_weight_label)
        self.percent_bank_tax_label.setStyleSheet(style.update_weight_label)

    # Додаємо одиницю до кількості екземплярів виробу
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

    # Зменьшуємо на одиницю кількість екземплярів виробу
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

    # Видаляємо позицію вироба зі списка та з таблиці
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

        if self.type_holder.currentText() == "Оберіть тип кріплення" or \
                self.item_value.currentText() in ["Оберіть виріб", " ", "", "Оберіть тип кріплення"] or \
                self.code_value.currentText() in empty_value or \
                self.length_value.currentText() in empty_value or \
                self.quantity_value.value() == 0:
            error_message = ""
            if self.type_holder.currentText() == "Оберіть тип кріплення":
                error_message += "Оберіть тип кріплення\n"
            if self.item_value.currentText() in ["Оберіть виріб", " ", "", "Оберіть тип кріплення", "?"]:
                error_message += "Оберіть виріб\n"
            if self.code_value.currentText() in empty_value:
                error_message += "Оберіть код виробу\n"
            if self.length_value.currentText() in empty_value:
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
                    self.code_value.currentText() not in empty_value and \
                    self.length_value.currentText() not in empty_value:

                self.load_data()

            if self.type_holder.currentText() != "Оберіть тип кріплення" and \
                    self.item_value.currentText() not in [" ", "Оберіть тип кріплення", "Оберіть виріб"] and \
                    self.code_value.currentText() not in empty_value and \
                    self.length_value.currentText() not in empty_value and \
                    self.quantity_value.value() != 0:

                data_list = [self.type_holder.currentText(),
                             self.item_value.currentText(),
                             self.code_value.currentText(),
                             self.length_value.currentText()]

                code: str = MyDb.get_full_code_item(data_list)
                data_list.append(code)
                dict_item = MyDb.get_info_item(data_list)


                self.new_item.set_type_holder(dict_item["type_holder"])
                self.new_item.set_type_item(dict_item["item"])
                self.new_item.set_code_item(dict_item["code_item"])
                self.new_item.set_en_name_item(dict_item["en_name_item"])
                self.new_item.set_ua_name_item(dict_item["ua_name_item"])
                self.new_item.set_length_item(dict_item["length_item"])
                self.new_item.set_image_path(dict_item["image_path"])
                length_str = MyDb.get_length(dict_item["length_item"])

                self.new_item.set_length_item_mm(length_str)
                self.new_item.set_weight_item(dict_item["weight"])
                self.new_item.set_price_item(dict_item["price_item"])
                self.new_item.set_discount_item(self.provider_discount_spinBox.value())
                self.new_item.set_amount_item(self.quantity_value.value())

                if not self.my_invoice.get_list_item():
                    self.my_invoice.add_item_to_list(self.new_item)

                else:

                    if self.new_item.get_code_item() in self.my_invoice.get_list_code():
                        for i in range(0, len(self.my_invoice.get_list_item())):
                            if self.my_invoice.get_list_item()[i].get_code_item() == self.new_item.get_code_item():
                                amount: int = int(self.new_item.get_amount_item()) + \
                                              int(self.my_invoice.get_list_item()[i].get_amount_item())
                                self.my_invoice.get_list_item()[i].set_amount_item(amount)
                                self.my_invoice.set_total_weight()
                                break
                    else:

                        self.my_invoice.add_item_to_list(self.new_item)

                self.my_invoice.set_total_weight()
                self.my_invoice.set_max_length()
                self.weight_value.setText(str(self.my_invoice.get_total_weight()) + " кг")
                self.lenght_value.setText(str(self.my_invoice.get_max_length()) + " см")
            self.load_data()

    # Редагуємо обрану позицію
    def update_item(self) -> None:
        #print("Update")
        row_index = self.table.currentRow()
        if row_index > -1:
            #print(f"row index: {row_index}")
            #print(f"Items: {len(self.my_invoice.get_list_item())}")
            selected_code = self.table.model().index(row_index, 1).data()
            #print(selected_code)
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
        """Функція  заповнює item_value переліком типів виробу"""

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
            #print(len(self.my_invoice.get_list_item()))
            self.table.setRowCount(len(self.my_invoice.get_list_item()))
            for i in range(0, len(self.my_invoice.get_list_item())):
                self.table.setRowHeight(i, 50)

                self.table.setItem(i, 0, QTableWidgetItem(str(i + 1)))

                self.table.item(i, 0).setTextAlignment(QtCore.Qt.AlignCenter)

                self.table.item(i, 0).setFlags(self.table.item(i, 0, ).flags() & ~ QtCore.Qt.ItemIsEditable)

                self.table.setItem(i, 1, QTableWidgetItem(self.my_invoice.get_list_item()[i].get_code_item()))

                self.table.item(i, 1).setTextAlignment(QtCore.Qt.AlignCenter)

                self.table.item(i, 1).setFlags(self.table.item(i, 1, ).flags() & ~ QtCore.Qt.ItemIsEditable)

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

        all_parameters = (
            self.type_holder.currentText(),
            self.item_value.currentText(),
            self.code_value.currentText(),
            self.length_value.currentText()
        )
        self.full_code = MyDb.get_full_code_item(all_parameters)
        del (all_parameters)

    # Завантаження списку кодів виробу без урахування довжини
    def get_code_items(self):
        """Функція заповнює code_value перелік кодів виробів
        певного типу тримача"""
        self.quantity_value.setValue(0)

        if self.item_value.currentText() not in ["Оберіть виріб", "Оберіть тип кріплення", "?", " "]:
            self.length_value.clear()
            self.length_value.addItem("?")
            code_list: tuple = MyDb.get_code_list(
                (self.type_holder.currentText(),
                 self.item_value.currentText())
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
        self.length_value.clear()
        if self.code_value.currentText() not in empty_value:
            length_tuple: tuple = \
                MyDb.get_length_item(
                    (self.type_holder.currentText(),
                     self.item_value.currentText(),
                     self.code_value.currentText())
                )

            for length_item in length_tuple:
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
        self.EURO_value.setText(
            self.new_check_number(self.EURO_value.text())
        )

    def check_packing_number(self) -> None:
        self.packing_value.setText(self.new_check_number(self.packing_value.text()))

    def check_delivery_number(self) -> None:
        self.delivery_value.setText(self.new_check_number(self.delivery_value.text()))

    def check_transaction_value(self) -> None:
        self.transaction_value.setText(self.new_check_number(self.transaction_value.text()))

    def check_bank_tax_value(self) -> None:
        self.bank_tax_value.setText(self.new_check_number(self.bank_tax_value.text()))

    def check_brokerage_services_value(self) -> None:
        self.brokerage_services_value.setText(self.new_check_number(self.brokerage_services_value.text()))

    def check_delivery_document_value(self) -> None:
        self.delivery_document_value.setText(self.new_check_number(self.delivery_document_value.text()))

    def check_delivery_document_EURO_1_value_(self) -> None:
        self.delivery_document_EURO_1_value_.setText(
            self.new_check_number(
                self.delivery_document_EURO_1_value_.text()
            )
        )

    # Кнопка створення пошукового вікна
    # def search_item(self) -> None:
    #     self.m_w = Search()
    #     self.m_w.show()

    # Кнопка створення КП
    def create_pre_commercial_offer(self) -> None:
        # встановлюємо курс евро
        self.my_invoice.set_rate(float(self.EURO_value.text().replace(",", ".")))

        # перевіряємо чи усі потрібні дані були надані користувачем
        if not self.check_data_for_pre_commercial():
            return

        # Додаємо у інвойс ім'я клієнта-компаніі
        self.my_invoice.set_customer_name(
            self.company_value.currentText()
        )

        # Додаємо packing
        self.my_invoice.set_packing_price(self.packing_value.text())

        # Додаємо калькуляцію у інвойс
        self.my_invoice.set_commission_percentage(
            self.persentage_spinBox.text()
        )

        # Додаємо у інвойс розмір знижки для клієнта-компаніі
        self.my_invoice.set_customer_discount(
            self.discount_customer_spinBox.text()
        )

        # Додаємо у інвойс розмір знижки від постачальника
        self.my_invoice.set_provider_discount(
            self.provider_discount_spinBox.text()
        )

        # Додаємо у інвойс вартість доставки
        self.my_invoice.set_delivery_price(
            self.delivery_value.text()
        )

        # Додаємо у інвойс вартість  документів
        self.my_invoice.set_price_document(
            self.delivery_document_value.text()
        )

        # Додаємо відсоток для банка
        self.my_invoice.set_bank_tax(
            self.bank_tax_value.text()
        )

        # Додаємо у інвойс вартість переказу
        self.my_invoice.set_transaction_price(
            self.transaction_value.text()
        )

        # Додаємо у інвойс брокерські послуги
        self.my_invoice.set_brokerage_price(
            self.brokerage_services_value.text()
        )

        # Формуємо ім'я мойбутньго файла
        pre_commercial_offer_name = \
            (name_offer(self.my_invoice.get_customer_name()))

        #self.my_invoice.invoice_input_toString()

        # Створюємо новий файл xlsx
        wb = Workbook()

        # Активуємо лист
        sheet = wb.active

        row_style(sheet)

        # Обороблюємо  колонки
        column_style(sheet)

        # Поєднуємо комірки  до таблиці
        merge_cells_before_table(sheet)

        #Додаємо картинку  у комірку А1
        img_top = openpyxl.drawing.image.Image(f"data/top.png")
        img_top.height = 150
        img_top.width = 920
        img_top.anchor ="A1"
        sheet.add_image(img_top)


        # Информація про компанію
        fill_company_info(sheet)

        # Заповнюємо дату до таблиці
        fill_today_before_table(sheet)

        # Заповнюємо назву компанії
        fill_customer_name(
            sheet,
            self.my_invoice.get_customer_name()
        )

        # Заповнюємо назву таблиці
        fill_title_table(sheet)

        # Заповнюємо назву таблиці
        fill_table_head(sheet)

        # Заповнюємо номера колонок
        fill_number_string(sheet)

        current_row = 16
        empty_string(sheet, current_row)
        current_row += 1

        # Вставновлюємо ціну виробника
        self.my_invoice.calculate_sum_item_price()

        # Ціна для розрахунку
        self.my_invoice.calculate_total_price_ua()

        # Заповнюємо таблицю з позиціями
        current_row = items_in_row(sheet, self.my_invoice, current_row)

        # Порожній рядок
        empty_string(sheet, current_row)

        # Вага
        total_weight(sheet, current_row)
        current_row += 1

        # Строка Разом
        fill_total_bill(sheet, current_row)
        current_row += 1

        # ПДВ
        tax_row_total(sheet, current_row)
        current_row += 1

        # Разом з ПДВ
        total_bill_with_tax(sheet, current_row)
        current_row += 1

        if self.my_invoice.get_customer_discount() != "0":
            # Знижка для клієнта
            fill_discount_customer_value(
                sheet,
                current_row,
                self.my_invoice.get_customer_name(),
                self.my_invoice.get_customer_discount()
            )
            current_row += 1
            # Вартість після знижки
            fill_total_tax_discount(sheet, current_row)
            current_row += 1

        # Вартість доставки
        self.my_invoice.calculate_total_delivery_price_ua()
        fill_delivery_value(sheet, current_row, self.my_invoice)
        current_row += 1

        # Загальна вартість
        fill_total_price(sheet, current_row)

        # 1C для всіх
        fill_1C_all(sheet, self.my_invoice, current_row)

        # Порожни колонки
        empty_columns(sheet, current_row, self.my_invoice)
        current_row += 1

        # Строки після таблиці
        after_table(sheet, current_row, self.my_invoice)
        current_row += 25

        #Приховуємо стовчики
        sheet.column_dimensions['D'].hidden = True
        sheet.column_dimensions['E'].hidden = True
        sheet.column_dimensions['I'].hidden = True
        sheet.column_dimensions['J'].hidden = True
        sheet.column_dimensions['L'].hidden = True
        sheet.column_dimensions['M'].hidden = True
        sheet.column_dimensions['N'].hidden = True
        sheet.column_dimensions['S'].hidden = True
        sheet.column_dimensions['T'].hidden = True

        sheet.print_area = f"A1:U{current_row}"

        qf = QFileDialog()

        path = ""
        path = qf.getSaveFileName(
            None,
            None,
            f"./{pre_commercial_offer_name}",
            '*.xlsx;;*.xls'
        )[0]

        if path == "":
            return
        else:
            # Збереження файла
            wb.save(path)
            wb.close()

    # Перевіряємо наявність усіх даних для прорахунку
    def check_data_for_pre_commercial(self) -> bool:

        if self.company_value.currentText() == "Оберіть компанію" or \
                self.EURO_value.text() in zero_spinBox or \
                self.table.rowCount() < 1 or \
                self.delivery_document_value.text() in zero_spinBox or \
                self.packing_value.text() in zero_spinBox or \
                self.delivery_document_EURO_1_value_.text() in zero_spinBox or \
                self.delivery_value.text() in zero_spinBox:
            error = MessageError()
            error_message: str = ""
            if self.company_value.currentText() == "Оберіть компанію":
                error_message += "Вкажіть назву компанії клієтна.\n"
            if self.EURO_value.text() in zero_spinBox:
                error_message += "Вкажіть курс EURO.\n"
            if self.delivery_document_value.text() in zero_spinBox:
                error_message += "Вкажіть вартість документу\n"
            if self.delivery_document_EURO_1_value_.text() in zero_spinBox:
                error_message += "Вкажіть вартість накладної EURO-1\n"
            if self.table.rowCount() < 1:
                error_message += "Додайте хочаб один виріб.\n"
            if self.packing_value.text() in zero_spinBox:
                error_message += "Зазначте вартість пакування.\n"
            if self.delivery_value.text() in zero_spinBox:
                error_message += "Зазначте вартість доставки."
            error.setText(error_message)
            error.exec_()
            return False
        else:
            return True

    # Приховуємо результати
    def hide_result(self):
        # Приховуємо вартість доставки
        self.result_delivery_label.setHidden(True)

        # Приховуємо  загальну вартість
        self.result_price_label.setHidden(True)

    # Показуємо результат
    def show_result(self) -> None:
        error_in_field: tuple = ('', '.', ',', "0")
        if self.EURO_value.text() in error_in_field \
                or self.packing_value.text() in error_in_field \
                or self.delivery_value.text() in error_in_field \
                or self.delivery_document_value.text() in error_in_field \
                or self.delivery_document_EURO_1_value_.text() in error_in_field \
                or self.transaction_value.text() in error_in_field \
                or self.brokerage_services_value.text() in error_in_field \
                or self.bank_tax_value.text() in error_in_field:
            error = MessageError()
            if self.EURO_value.text() in error_in_field:
                message = "Порожній курс валюти.\nВведіть курс валют.\n"

            if self.packing_value.text() in error_in_field:
                message = "Порожня вартість пакування.\nВведіть вартість пакування.\n"

            if self.delivery_value.text() in error_in_field:
                message = "Порожня вартість доставки.\nВведіть вартість доставки.\n"
            error.setText(message)
            error.exec_()
            return

        rate: float = round(float(self.EURO_value.text().replace(",", ".")), 2)
        price_delivery: float = 0.0
        price_result: float = 0.0


        provider_discount = \
            (100 - float(self.provider_discount_spinBox.text().replace(",", "."))) / 100

        price_result = sum([item.get_price_item() * item.get_amount_item() * provider_discount for item in
                            self.my_invoice.get_list_item()])
        price_result = round(price_result, 2)

        price_result += float(self.packing_value.text())


        price_order = price_result

        price_result = round(price_result * (1 + (float(self.bank_tax_value.text().replace(",", "."))) / 100), 2)



        percent = (100 - (float(self.persentage_spinBox.text().replace(",", ".")))) / 100

        price_result = round(price_result / percent, 2)

        price_result *= rate
        price_result = round(price_result, 2)

        price_result += float(self.transaction_value.text().replace(",", "."))
        price_result += float(self.brokerage_services_value.text().replace(",", "."))


        price_result *= 1.2
        price_result = round(price_result, 2)


        # Показуємо вартість доставки
        self.result_delivery_label.setHidden(False)

        if price_order > 5999.99:
            price_delivery = \
                float(self.delivery_value.text().replace(",", ".")) + \
                float(self.delivery_document_value.text().replace(",", ".")) + \
                float(self.delivery_document_EURO_1_value_.text().replace(",", "."))
        else:
            a = float(self.delivery_value.text().replace(",", "."))
            b = float(self.delivery_document_value.text().replace(",", "."))
            price_delivery = a + b

        price_delivery *= rate
        price_delivery *= 1.2
        price_delivery = round(price_delivery, 2)


        if self.discount_customer_spinBox.text() not in ("", " ", "0"):
            discount: float = round(
                float(self.discount_customer_spinBox.text().replace(",", ".")) / 100,
                2
            )

            discount_value: float = price_result * discount


            price_result = price_result - discount_value
            price_result = round(price_result, 2)


        price_result = price_result + price_delivery
        price_result = round(price_result, 2)

        # Показуємо  загальну вартість
        self.result_price_label.setText(
            f"Загальна вартість: {round(price_result / rate, 2)} "
            f"EURO {price_result} грн."
        )
        self.result_price_label.setHidden(False)
        self.result_delivery_label.setText(
            f"Вартість доставки: {round(price_delivery / rate, 2)} "
            f"EURO {price_delivery} грн."
        )

    # КЛІЄНТИ
    # Кнопка отримання повної назви клієнтів
    def get_full_name_customer(self) -> None:
        short_name: str = self.customer_short_name_value.text()
        if short_name == "":
            error = MessageError()
            message = "Порожній запит\nВведіть коротку назву."
            error.setText(message)
            error.exec_()
            self.customer_full_name_value.setText("")
            return
        if short_name not in get_short_name_list():
            error = MessageError()
            message = f"Коротка назва компанії {short_name} відсутня у базі."
            error.setText(message)
            error.exec_()
            self.customer_full_name_value.setText("")
            return
        else:
            full_name: str = get_full_name_company(short_name)
            self.customer_full_name_value.setText(full_name)

    # Кнопка скидання короткої назви
    def reset_short_name(self) -> None:
        self.customer_short_name_value.setText("")

    # Кнопка скидання повної назви
    def reset_full_name(self) -> None:
        self.customer_full_name_value.setText("")

    # Кнопка отримання усіх коротких назв
    def show_all_short_name(self) -> None:
        for item in get_short_name_list():
            self.list_customer_comboBox.addItem(item)

    # Отримуемо одного клієнта зі списка
    def get_itemBox_info(self) -> None:
        if self.list_customer_comboBox.currentText() != "":
            self.customer_short_name_value.setText(
                self.list_customer_comboBox.currentText()
            )
            self.get_full_name_customer()

    # Кнопка для зміни клієнта
    def update_client(self) -> None:
        if self.customer_short_name_value.text() == "":
            error = MessageError()
            message = (f'Порожня коротка назва.\nВведіть коротку назву\n'
                       f'та знов натисніть кнопку"Змінити"')
            error.setText(message)
            error.exec_()
            return
        if self.customer_full_name_value.text() == "":
            error = MessageError()
            message = (f'Порожня повна назва.\nВведіть повна назву\n'
                       f'та знов натисніть кнопку"Змінити"')
            error.setText(message)
            error.exec_()
            return

        if (
                (self.customer_short_name_value.text() in get_short_name_list())
                and (self.customer_full_name_value.text() not in get_full_name_list())
        ):
            up_date_full_name_company(
                self.customer_short_name_value.text(),
                self.customer_full_name_value.text()
            )
        elif (
                (self.customer_full_name_value.text() in
                get_full_name_list())
                and (self.customer_short_name_value.text() not in
                get_short_name_list())
        ):
            up_date_short_name(
                self.customer_full_name_value.text(),
                self.customer_short_name_value.text()
            )
        self.company_value.clear()
        self.customer_full_name_value.setText("")
        self.customer_short_name_value.setText("")
        self.list_customer_comboBox.clear()
        company_list: list = get_short_name_list()
        # Заповнюємо компанії
        for company in company_list:
            self.company_value.addItem(company)
            self.list_customer_comboBox.addItem(company)

    def add_client(self) -> None:
        """
        Додаємо нового клієєнта
        :return:
        """
        if self.customer_short_name_value.text() == "":
            error = MessageError()
            message = (f'Порожня коротка назва.\nВведіть коротку назву\n'
                       f'та знов натисніть кнопку"Змінити"')
            error.setText(message)
            error.exec_()
            return
        if self.customer_full_name_value.text() == "":
            error = MessageError()
            message = (f'Порожня повна назва.\nВведіть повна назву\n'
                       f'та знов натисніть кнопку"Змінити"')
            error.setText(message)
            error.exec_()
            return

        if self.customer_short_name_value.text() in get_short_name_list():
            full_name = get_full_name_company(self.customer_short_name_value.text())
            if full_name == self.customer_full_name_value.text():
                error = MessageError()
                message = (f'Компанія вже існує в базі.')
                error.setText(message)
                error.exec_()
                return

        add_new_company(
            self.customer_short_name_value.text(),
            self.customer_full_name_value.text()
        )

        self.company_value.clear()
        self.customer_full_name_value.setText("")
        self.customer_short_name_value.setText("")
        self.list_customer_comboBox.clear()
        company_list: list = get_short_name_list()
        # Заповнюємо компанії
        for company in company_list:
            self.company_value.addItem(company)
            self.list_customer_comboBox.addItem(company)

    #Видалення кліента з бази
    def delete_client(self) -> None:
        """
        Функція видаляє кліента з бази
        :return:
        """
        customers_list = get_short_name_list()
        if self.customer_short_name_value.text() in ("", " "):
            error = MessageError()
            message = (f'Введить коротку назву клієнта')
            error.setText(message)
            error.exec_()
            return

        if self.customer_short_name_value.text() not in customers_list:
            error = MessageError()
            message = (f'Клієнт {self.customer_short_name_value.text() }'
                       f'в базі відсутній')
            error.setText(message)
            error.exec_()
            return

        delete_customer(self.customer_short_name_value.text())
        self.customer_full_name_value.setText("")
        self.customer_short_name_value.setText("")
        self.company_value.clear()
        self.list_customer_comboBox.clear()
        company_list: list = get_short_name_list()
        # Заповнюємо компанії
        for company in company_list:
            self.company_value.addItem(company)
            self.list_customer_comboBox.addItem(company)


        # ПОШУК ПУАНСОНА
    #ПОШУК
    def find_punch(self) -> None:
        """
        Метод обробляє кнопку find_die_button,
        та викликає повдомлення  про помилку
        або  відповдний до заданих параметрів метод
        :return: None
        """
        self.length_info_punch_label.setText("")
        self.punch_info.setText("")
        self.set_empty_punch_image()
        holder: str = self.type_punch_value.currentText()
        if holder == "":
            message = MessageError()
            message.setText("Оберіть тип кріплення пуансона")
            message.exec_()
        else:
            #Обран лише тримач
            self.result_punch_value.clear()
            if (self.punch_angle_value.currentText() == ""
                    and self.punch_height_value.currentText() == ""
                    and self.punch_radius_value.currentText() == ""):
                self.result_punch_value.clear()
                for item in MyDb.get_punch_by_holder(
                        book=self.book,
                        holder=holder
                ):
                    self.result_punch_value.addItem(item)
            #Обрані тримач та кут
            elif (self.punch_angle_value.currentText() != ""
                  and self.punch_height_value.currentText() == ""
                  and self.punch_radius_value.currentText() == ""):
                self.result_punch_value.clear()
                punch_holder_angle = MyDb.get_punch_by_holder_angle(
                        book=self.book,
                        type_holder=holder,
                        angle=self.punch_angle_value.currentText()
                )
                for item in punch_holder_angle:
                    self.result_punch_value.addItem(item)
                del punch_holder_angle

            #Обран тримач та виста
            if (self.punch_angle_value.currentText() == ""
                    and self.punch_height_value.currentText() != ""
                    and self.punch_radius_value.currentText() == ""):
                self.result_punch_value.clear()
                punch_holder_height = MyDb.get_punch_by_holder_height(
                    book=self.book,
                    type_holder=holder,
                    height=self.punch_height_value.currentText()
                )
                for item in punch_holder_height:
                    self.result_punch_value.addItem(item)
                del punch_holder_height

                #Обран тримач та радіус
            if (self.punch_angle_value.currentText() == ""
                    and self.punch_height_value.currentText() == ""
                    and self.punch_radius_value.currentText() != ""):
                self.result_punch_value.clear()
                punch_holder_radius = MyDb.get_punch_by_holder_radius(
                    book=self.book,
                    type_holder=holder,
                    radius=self.punch_radius_value.currentText()
                )
                for item in punch_holder_radius:
                    self.result_punch_value.addItem(item)
                del punch_holder_radius

            #Обрані тримач, кут та висота
            elif (self.punch_angle_value.currentText() != ""
                  and self.punch_height_value.currentText() != ""
                  and self.punch_radius_value.currentText() == ""):
                self.result_punch_value.clear()
                punch_holder_angle_height \
                    = MyDb.get_punch_by_holder_angle_height(
                        book=self.book,
                        type_holder=holder,
                        angle=self.punch_angle_value.currentText(),
                        height=self.punch_height_value.currentText()
                )
                for item in punch_holder_angle_height:
                    self.result_punch_value.addItem(item)
                del punch_holder_angle_height

            #Обрані тримач, кут та радіус
            elif (self.punch_angle_value.currentText() != ""
                  and self.punch_height_value.currentText() == ""
                  and self.punch_radius_value.currentText() != ""):
                self.result_punch_value.clear()
                punch_holder_angle_radius \
                    = MyDb.get_punch_by_holder_angle_radius(
                        book=self.book,
                        type_holder=holder,
                        angle=self.punch_angle_value.currentText(),
                        radius=self.punch_radius_value.currentText()
                )
                for item in punch_holder_angle_radius:
                    self.result_punch_value.addItem(item)
                del punch_holder_angle_radius

            #Обрані тримач, висота та радіус
            elif (self.punch_angle_value.currentText() == ""
                  and self.punch_height_value.currentText() != ""
                  and self.punch_radius_value.currentText() != ""):
                self.result_punch_value.clear()
                punch_holder_height_radius \
                    = MyDb.get_punch_by_holder_height_radius(
                        book=self.book,
                        type_holder=holder,
                        height=self.punch_height_value.currentText(),
                        radius=self.punch_radius_value.currentText()
                )
                for item in punch_holder_height_radius:
                    self.result_punch_value.addItem(item)
                del punch_holder_height_radius

            # Обрані тримач,кут, висота та радіус
            elif (
                    self.punch_angle_value.currentText() != ""
                    and self.punch_height_value.currentText() != ""
                    and self.punch_radius_value.currentText() != ""
            ):
                self.result_punch_value.clear()
                punch_holder_angle_height_radius \
                    = MyDb.get_punch_by_holder_angle_height_radius(
                        book=self.book,
                        type_holder=holder,
                        angle=self.punch_angle_value.currentText(),
                        height=self.punch_height_value.currentText(),
                        radius=self.punch_radius_value.currentText()
                )
                for item in punch_holder_angle_height_radius:
                    self.result_punch_value.addItem(item)
                del punch_holder_angle_height_radius

    def change_type_punch(self) -> None:
        sheet = self.book["Пуансон"]
        rows = sheet.max_row
        """
                "Amada-promecam",
                "Trumpf-Wila",
                "Bystronic",
        :return: 
        """
        self.result_punch_value.clear()
        self.punch_angle_value.clear()
        self.punch_angle_value.addItem("")
        self.punch_height_value.clear()
        self.punch_height_value.addItem("")
        self.punch_radius_value.clear()
        self.punch_radius_value.addItem("")
        self.set_empty_punch_image()
        self.punch_info.setText("")
        self.length_info_punch_label.setText("")

        if self.type_punch_value.currentText() != "":
            self.result_punch_value.clear()
            self.punch_angle_value.clear()
            self.punch_angle_value.addItem("")
            self.punch_height_value.clear()
            self.punch_height_value.addItem("")
            self.punch_radius_value.clear()
            self.punch_radius_value.addItem("")
            my_holder = self.type_punch_value.currentText()

            set_angel = set()
            set_height = set()
            set_radius = set()
            counter = 0
            for index in range(2, rows):
                if (sheet["B" + str(index-1)].value == my_holder and
                        sheet["B" + str(index)].value != my_holder):
                    break
                if sheet["B" + str(index)].value == my_holder:
                    counter += 1
                    set_angel.add(sheet["J" + str(index)].value)
                    set_height.add(sheet["K" + str(index)].value)
                    set_radius.add(sheet["L" + str(index)].value)
            #print(f"COUNTER: {counter}")
            tuple_angle = tuple(sorted(set_angel))
            tuple_height = tuple(sorted(set_height))
            tuple_radius = tuple(sorted(set_radius))
            len_tuple = (
                len(tuple_angle),
                len(tuple_height),
                len(tuple_radius)
            )

            for index in range(max(len_tuple)):
                if len(tuple_angle) != max(len_tuple):
                    if len(tuple_angle) >= index+1:
                        self.punch_angle_value.addItem(
                            str(tuple_angle[index]).replace(".",",")
                        )
                else:
                    self.punch_angle_value.addItem(
                        str(tuple_angle[index]).replace(".",",")
                    )
                if len(tuple_height) != max(len_tuple):
                    if len(tuple_height) >= index+1:
                        self.punch_height_value.addItem(
                            str(tuple_height[index]).replace(".",",")
                        )
                else:
                    self.punch_height_value.addItem(
                        str(tuple_height[index]).replace(".",",")
                    )
                if len(tuple_radius) != max(len_tuple):
                    if len(tuple_radius) >= index + 1:
                        self.punch_radius_value.addItem(
                            str(tuple_radius[index]).replace(".",",")
                        )
                else:
                    self.punch_radius_value.addItem(
                        str(tuple_radius[index]).replace(".",",")
                    )

    def get_one_punch_info(self) -> None:
        """
        Функція заповнює  punch_image зображенням та
         додає параметри пуансона у length_info_punch_label та
         у punch_info
        """

        if self.result_punch_value.currentText() not in ("", " "):
            code = self.result_punch_value.currentText()
            image_code = MyDb.get_punch_code_image(
                self.book,
                code
            )
            self.pixmap = QPixmap(f"data\{image_code}")
            im = PIL.Image.open(f"data\{image_code}").size
            if im[0] < im[1]:
                origin_width = im[0]
                origin_height = im[1]
                div_h_w = origin_height / origin_width
                scale = im[1] / 320

                #width height
                origin_height /= scale
                origin_width = origin_height/div_h_w
                p = self.pixmap.scaled(int(origin_width), int(origin_height))
            elif im[0] > im[1]:
                origin_width = im[0]
                origin_height = im[1]
                div_h_w = origin_height / origin_width
                scale = im[0] / 310
                #width heigh
                origin_width /= scale
                origin_height = div_h_w * origin_width
                p = self.pixmap.scaled(int(origin_width), int(origin_height))
            self.punch_image.setPixmap(p)

            sheet_punch = self.book["Пуансон"]
            length_tuple = MyDb.get_length_tuple(sheet_punch, code)
            self.length_info_punch_label.setText(", ".join(length_tuple))

            self.punch_info.setText(
                MyDb.get_punch_info(sheet_punch, code)
            )
        else:
            self.set_empty_punch_image()
            self.length_info_punch_label.setText("")
            self.punch_info.setText("")

    def set_empty_punch_image(self) -> None:
        """
        Функція заповняє порожнім зображенням punch_image
        """
        self.pixmap = QPixmap("data\empty.jpg")
        self.punch_image.setPixmap(self.pixmap)

        # ПОШУК МАТРИЦІ
    def change_type_die(self) -> None:
        """
        Функція заповнює порожніми полями та зображенням
        після  зміни стану type_die_value
        :return:None
        """
        self.result_die_value.clear()
        self.die_angle_value.clear()
        self.die_angle_value.addItem("")
        self.die_height_value.clear()
        self.die_height_value.addItem("")
        self.die_distance_value.clear()
        self.die_distance_value.addItem("")
        self.length_info_die_label.setText("")
        self.die_info.setText("")
        self.set_empty_die_image()

        if self.type_die_value.currentText() != "":
            self.result_die_value.clear()
            self.die_angle_value.clear()
            self.die_angle_value.addItem("")
            self.die_height_value.clear()
            self.die_height_value.addItem("")
            self.die_distance_value.clear()
            self.die_distance_value.addItem("")

            die_parameters = MyDb.get_all_die_parameters(
                self.book,
                self.type_die_value.currentText()
            )


            max_len = max(len(die_parameters[0]), len(die_parameters[1]), len(die_parameters[2]))

            for index in range(max_len):
                if len(die_parameters[0]) != max_len:
                    if len(die_parameters[0]) >= index +1:
                        self.die_angle_value.addItem(
                            str(die_parameters[0][index]).replace(".",",")
                        )
                else:
                    self.die_angle_value.addItem(
                        str(die_parameters[0][index]).replace(
                            ".",","
                        )
                    )
                if len(die_parameters[1]) != max_len:
                    if len(die_parameters[1]) >= index +1:
                        self.die_height_value.addItem(
                            str(die_parameters[1][index]).replace(
                                ".", ","
                            )
                        )
                else:
                    self.die_height_value.addItem(
                        str(die_parameters[1][index]).replace(
                            ".", ","
                        )
                    )
                if len(die_parameters[2]) != max_len:
                    if len(die_parameters[2]) >= index +1:
                        self.die_distance_value.addItem(
                            str(die_parameters[2][index]).replace(
                                ".", ","
                            )
                        )
                else:
                    self.die_distance_value.addItem(
                        str(die_parameters[2][index]).replace(
                            ".", ","
                        )
                    )
        elif self.type_die_value.currentText() == "":
            return

    def set_empty_die_image(self) -> None:
        """
        Функція заповняє порожнім зображенням die_image
        """
        self.pixmap_die = QPixmap("data\empty.jpg")
        self.die_image.setPixmap(self.pixmap_die)

    def find_die(self) -> None:
        """
        Метод обробляє кнопку find_die_button
        та викликає повдомлення  про помилку
        або  відповдний до заданих параметрів метод
        :return: None
        """
        self.length_info_die_label.setText("")
        self.die_info.setText("")
        self.set_empty_die_image()
        holder_die: str = self.type_die_value.currentText()
        if holder_die == "":
            message = MessageError()
            message.setText("Оберіть тип кріплення матриці")
            message.exec_()
        else:
            #Обран лише тримач
            self.result_die_value.clear()
            if (self.die_angle_value.currentText() == ""
                    and self.die_height_value.currentText() == ""
                    and self.die_distance_value.currentText() == ""):
                self.result_die_value.clear()
                for item in MyDb.get_die_by_holder(
                        book=self.book,
                        holder=holder_die
                ):
                    self.result_die_value.addItem(item)
            #Обрані тримач та кут
            if (self.die_angle_value.currentText() != ""
                    and self.die_height_value.currentText() == ""
                    and self.die_distance_value.currentText() == ""):
                self.result_die_value.clear()
                die_holder_angle = MyDb.get_die_by_holder_angle(
                    book=self.book,
                    type_holder=holder_die,
                    angle=self.die_angle_value.currentText()
                )
                for item in die_holder_angle:
                    self.result_die_value.addItem(item)

            #Обрані тримач та висота
            if (self.die_angle_value.currentText() == ""
                    and self.die_height_value.currentText() != ""
                    and self.die_distance_value.currentText() == ""):
                self.result_die_value.clear()
                die_holder_height = MyDb.get_die_by_holder_height(
                    book=self.book,
                    type_holder=holder_die,
                    height=self.die_height_value.currentText()
                )
                for item in die_holder_height:
                    self.result_die_value.addItem(item)
            #Обрані тримач та розкриття
            if (self.die_angle_value.currentText() == ""
                    and self.die_height_value.currentText() == ""
                    and self.die_distance_value.currentText() != ""):
                self.result_die_value.clear()
                die_holder_distance = MyDb.get_die_by_holder_distance(
                    book=self.book,
                    type_holder=holder_die,
                    distance=self.die_distance_value.currentText()
                )
                for item in die_holder_distance:
                    self.result_die_value.addItem(item)
            #Обрані тримач, кут та висота
            if (self.die_angle_value.currentText() != ""
                    and self.die_height_value.currentText() != ""
                    and self.die_distance_value.currentText() == ""):
                self.result_die_value.clear()
                die_holder_angle_height = MyDb.get_die_by_holder_angle_height(
                    book=self.book,
                    type_holder=holder_die,
                    angle=self.die_angle_value.currentText(),
                    height=self.die_height_value.currentText()
                )
                #print(die_holder_angle_height)
                for item in die_holder_angle_height:
                    self.result_die_value.addItem(item)
            #Обрані тримач, кут та розкриття
            if (self.die_angle_value.currentText() != ""
                    and self.die_height_value.currentText() == ""
                    and self.die_distance_value.currentText() != ""):
                self.result_die_value.clear()
                die_holder_angle_distance = MyDb.get_die_by_holder_angle_distance(
                    book=self.book,
                    type_holder=holder_die,
                    angle=self.die_angle_value.currentText(),
                    distance=self.die_distance_value.currentText()
                )
                #print(die_holder_angle_distance)
                for item in die_holder_angle_distance:
                    self.result_die_value.addItem(item)
            #Обрані тримач, висота та розкриття
            if (self.die_angle_value.currentText() == ""
                    and self.die_height_value.currentText() != ""
                    and self.die_distance_value.currentText() != ""):
                self.result_die_value.clear()
                die_holder_height_distance = MyDb.get_die_by_holder_height_distance(
                    book=self.book,
                    type_holder=holder_die,
                    height=self.die_height_value.currentText(),
                    distance=self.die_distance_value.currentText()
                )
                for item in die_holder_height_distance:
                    self.result_die_value.addItem(item)

            #Обрані тримач, кут висота та розкриття
            if (self.die_angle_value.currentText() != ""
                    and self.die_height_value.currentText() != ""
                    and self.die_distance_value.currentText() != ""):
                self.result_die_value.clear()

                die_holder_angle_height_distance = MyDb.get_die_by_holder_ang_hei_dist(
                    book=self.book,
                    type_holder=holder_die,
                    angle=self.die_angle_value.currentText(),
                    height=self.die_height_value.currentText(),
                    distance=self.die_distance_value.currentText()
                )
                for item in die_holder_angle_height_distance:
                    self.result_die_value.addItem(item)

    def get_one_die_info(self) -> None:
        """
        Фунція заповнює length_info_die_label, die_info та
        die_image  відповідно коду
        :return: None
        """

        #Зображення
        code_die = self.result_die_value.currentText()
        if code_die in ("", " "):
            self.length_info_die_label.setText("")
            self.die_info.setText("")
            self.set_empty_die_image()
        else:
            image_code = MyDb.get_die_code_image(
                self.book,
                code_die
            )
            self.pixmap = QPixmap(f"data\{image_code}")
            im = PIL.Image.open(f"data\{image_code}").size
            if im[0] < im[1]:
                origin_width = im[0]
                origin_height = im[1]
                div_h_w = origin_height / origin_width
                scale = im[1] / 320

                #width height
                origin_height /= scale
                origin_width = origin_height/div_h_w
                p = self.pixmap.scaled(int(origin_width), int(origin_height))
            elif im[0] > im[1]:
                origin_width = im[0]
                origin_height = im[1]
                div_h_w = origin_height / origin_width
                scale = im[0] / 310
                #width heigh
                origin_width /= scale
                origin_height = div_h_w * origin_width
                p = self.pixmap.scaled(int(origin_width), int(origin_height))
            self.die_image.setPixmap(p)

            # Довжини
            length_die_tuple = MyDb.get_length_die_tuple(
                self.book,
                code_die,
                self.type_die_value.currentText()
            )
            self.length_info_die_label.setText(
                ",".join(length_die_tuple)
            )

            #Інформація матриці
            self.die_info.setText(MyDb.get_die_info(self.book, code_die))


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


# class Search(QMdiSubWindow):
class Search(QWidget):
    def __init__(self):
        super(Search, self).__init__()
        self.setGeometry(870, 50, 820, 880)
        uic.loadUi("Search.ui", self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
