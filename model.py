import openpyxl
from openpyxl import *
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment
from openpyxl.styles.borders import Border, Side
import openpyxl.styles.numbers
from openpyxl.styles import Font, Fill #Стилі для текста
from openpyxl.styles import PatternFill #Cтили для ячеєк
from openpyxl.styles import colors #Kольори для текста и ячеєк
from vectortool_customers.customers_db import *
DB_FOLDER = "data/DB_bending.xlsx"


class Item:

    def __init__(
            self,
            db_path: str = None,
            type_holder: str = None,
            type_item: str = None,
            code_item: str = None,
            length_item: str = None,
            length_item_mm: str = None,
            weight: float = 0.0,
            price_item: float = 0.0,
            discount_item: float = 0.0,
            cross_section_param: dict = None,
            image_path: str = None,
            en_name_item: str = None,
            ua_name_item: str = None,
            amount_item: int = 0
    ) -> None:
        self.db = openpyxl.load_workbook(DB_FOLDER)
        self.db_path: str = db_path
        self.type_holder: str = type_holder
        self.type_item: str = type_item
        self.code_item: str = code_item
        self.length_item: str = length_item
        self.length_item_mm: str = length_item_mm
        self.weight: float = weight
        self.price_item: float = price_item
        self.discount_item: float = discount_item
        self.cross_section_param: dict = cross_section_param
        self.image_path: str = image_path
        self.en_name_item: str = en_name_item
        self.ua_name_item: str = ua_name_item
        self.amount_item: int = amount_item

    def set_db_path(self, new_path: str) -> None:
        self.db_path = new_path

    def get_db_path(self) -> str:
        return self.db_path

    def set_type_holder(self, new_type_holder: str) -> None:
        self.type_holder = new_type_holder

    def get_type_holder(self) -> str:
        return self.type_holder

    def set_type_item(self, new_type_item: str) -> None:
        self.type_item = new_type_item

    def get_type_item(self) -> str:
        return self.type_item

    def set_code_item(self, new_code_item: str) -> None:
        self.code_item = new_code_item

    def get_code_item(self) -> str:
        return self.code_item

    def set_length_item(self, new_length_item: str) -> None:
        self.length_item = new_length_item

    def get_length_item(self) -> str:
        return self.length_item

    def set_length_item_mm(self, new_length_item_mm: str) -> None:
        self.length_item_mm = new_length_item_mm

    def get_length_item_mm(self) -> str:
        return self.length_item_mm

    def set_weight_item(self, new_weight: float) -> None:
        self.weight = new_weight

    def get_weight_item(self) -> float:
        return self.weight

    def set_price_item(self, new_price_item: float) -> None:
        self.price_item = new_price_item

    def get_price_item(self) -> float:
        return self.price_item

    def set_discount_item(self, percent: float) -> None:
        self.discount_item = percent

    def get_discount_item(self) -> float:
        return self.discount_item

    def set_cross_section_param(self, new_dict: dict) -> None:
        self.cross_section_param = new_dict

    def get_cross_section_param(self) -> dict:
        return self.cross_section_param

    def set_image_path(self, new_img_path: str) -> None:
        self.image_path = new_img_path

    def get_image_path(self) -> str:
        return self.image_path

    def set_en_name_item(self, new_en_name: str) -> None:
        self.en_name_item = new_en_name

    def get_en_name_item(self) -> str:
        return self.en_name_item

    def set_ua_name_item(self, new_ua_name: int) -> None:
        self.ua_name_item = new_ua_name

    def get_ua_name_item(self) -> str:
        return self.ua_name_item

    def set_amount_item(self, new_amount_item: int) -> None:
        self.amount_item = new_amount_item

    def get_amount_item(self) -> int:
        return self.amount_item

    def get_name_for_table(self) -> str:
        result: str = ""
        list_1: list = self.get_ua_name_item().split(";")
        a = list_1[0]
        b = list_1[-1]
        result = a
        result += b
        return result

class Invoice:

    def __init__(
            self,
            rate: float = 0.0,
            list_item: list = None,
            packing_price: float = 0.0,
            delivery_price: float = 0.0,
            max_length: str = "0.0",
            total_weight: float = 0.0,
            commission_percentage: float = 0.0,
            tecnostamp_discount: float = 0.0,
    ) -> None:
        self.rate = rate
        self.list_item = list_item
        self.total_weight = total_weight
        self.max_length = max_length
        self.packing_price = packing_price
        self.delivery_price = delivery_price
        self.commission_percentage = commission_percentage
        self.tecnostamp_discount = tecnostamp_discount

    def set_rate(self, new_rate: float) -> None:
        self.rate = new_rate

    def get_rate(self) -> float:
        return self.rate

    def set_list_item(self, new_list_item: list[Item]) -> None:
        self.list_item = new_list_item

    def get_list_item(self) -> list[Item]:
        if self.list_item is None:
            return []
        else:
            return self.list_item

    def add_item_to_list(self, new_item: Item) -> None:
        my_list_item = self.get_list_item()

        my_list_item.append(new_item)
        self.set_list_item(my_list_item)
        self.set_total_weight()
        self.set_max_length()

    def remove_item_from_list(self, code: str) -> None:
        index_code = 0
        for i in range(0, len(self.get_list_item())):
            if self.get_list_item()[i].get_code_item() == code:
                index_code = i
                break
        temp_list = self.get_list_item()
        temp_list.pop(index_code)
        self.set_list_item(temp_list)

    def print_code_amount(self):
        for item in self.list_item:
            print(item.get_code_item(), " ", item.get_amount_item())

    #Загальна вага
    def set_total_weight(self) -> None:
        self.total_weight = 0.0
        if self.list_item is None:
            self.total_weight = 0.0
        else:
            for item in self.list_item:
                self.total_weight += (item.get_weight_item() * item.get_amount_item())
                self.total_weight = round(self.total_weight, 2)

    def get_total_weight(self) -> float:
        return self.total_weight

    #Максимальна довжина
    def set_max_length(self) -> None:
        if len(self.list_item) == 0:
            self.max_length = "0.0"
        elif len(self.list_item) == 1:
            self.max_length = self.list_item[0].get_length_item_mm()
            self.max_length = str(float(self.max_length) / 10)
        else:
            for i in range(0, len(self.list_item) - 1):
                if float(self.list_item[i].get_length_item_mm()) >= float(self.list_item[i + 1].get_length_item_mm()):
                    self.max_length = self.list_item[i].get_length_item_mm()
                    self.max_length = str(float(self.max_length)/10)
                else:
                    self.max_length = self.list_item[i + 1].get_length_item_mm()
                    self.max_length = str(float(self.max_length)/10) + " см"
    def get_max_length(self) -> str:
        return self.max_length


    def set_packing_price(self, new_packing_price: float) -> None:
        self.packing_price = new_packing_price

    def get_packing_price(self) -> float:
        return self.packing_price

    def set_delivery_price(self, new_delivery_price: float) -> None:
        self.delivery_price = new_delivery_price

    def get_delivery_price(self) -> float:
        return self.delivery_price

    def set_tecnostamp_discount(self, new_tecnostamp_discount: str) -> None:
        self.tecnostamp_discount = new_tecnostamp_discount

    def get_tecnostamp_discount(self) -> float:
        return self.tecnostamp_discount

    def show_list(self) -> None:
        print("START LIST")
        for item in self.get_list_item():
            print(f"{item.get_code_item()} - {item.get_amount_item()}")
        print("END LIST")

    def get_list_code(self) -> list:
        result_list = []
        for i in self.get_list_item():
            result_list.append(i.get_code_item())
        return result_list


class Pre_commercial_offer:

    def __init__(
            self,
            company_name: str = None,
            rate: str = None,
            discount: str = None,
            path_temp: str = None
    ):
        self.company_name: str = company_name
        self.rate: str = rate
        self.discount: str = discount
        self.path_temp: str = path_temp

    def set_company_name(self, new_company: str) -> None:
        self.company_name = new_company

    def get_company_name(self) -> str:
        return self.company_name

    def set_rate(self, new_rate: str) -> None:
        self.rate = new_rate

    def get_rate(self) -> str:
        return self.rate

    def set_discount(self, new_discount: str) -> None:
        self.discount = new_discount

    def get_discoiunt(self) -> str:
        return self.discount

    def set_path_temp(self, new_path: str) -> None:
        self.path_temp = new_path

    def get_path_temp(self) -> str:
        return self.path_temp

    #def fill_xlsx(self, new_invoice: Invoice, new_path: str) -> None:
    def fill_xlsx(self, new_invoice: Invoice) -> None:
        #Шрифти
        #Позиція
        position_font = Font(size=6, bold=True)
        position_font.name = "Times New Roman"

        #Назва
        name_font = Font(size=7, bold=False)
        name_font.name = "Times New Roman"


        #Рамка
        thin_border = Border(left=Side(style='thin'),
                             right=Side(style='thin'),
                             top=Side(style='thin'),
                             bottom=Side(style='thin'))

        #wb = load_workbook(new_path)
        wb = load_workbook(self.get_path_temp())
        ws = wb.active
        work_sheet = wb["Лист1"]

        #Назва компанії
        #work_sheet.merge_cells(start_row=10, start_column=13, end_row=10, end_column=16)



        start_row = 17



        work_sheet.insert_rows(len(new_invoice.get_list_item()))


        current_row = 0
        last_row = len(new_invoice.get_list_item()) + start_row


        img = None
        for index in range(0, len(new_invoice.get_list_item())):
            current_row = start_row + index
            work_sheet.row_dimensions[current_row].height = 90

            #Номер позиції

            work_sheet[f"B{str(current_row)}"].font = position_font
            work_sheet[f"B{str(current_row)}"].alignment = Alignment(horizontal="center", vertical='center')
            work_sheet[f"B{str(current_row)}"].value = index + 1
            work_sheet[f"B{str(current_row)}"].border = thin_border

            work_sheet[f"C{str(current_row)}"].border = thin_border

            #Англійська назва
            work_sheet[f"D{str(current_row)}"].fill = PatternFill(fill_type='solid', start_color='ffff00', end_color='ffff00')
            work_sheet[f"D{str(current_row)}"].value = new_invoice.get_list_item()[index].get_en_name_item()
            work_sheet[f"D{str(current_row)}"].font = name_font
            work_sheet[f"D{str(current_row)}"].alignment = Alignment(horizontal="left", vertical='center',wrapText=True)
            work_sheet[f"D{str(current_row)}"].border = thin_border

            work_sheet[f"E{str(current_row)}"].border = thin_border

            #Назва українською
            work_sheet[f"F{str(current_row)}"].value = new_invoice.get_list_item()[index].get_ua_name_item()
            work_sheet[f"F{str(current_row)}"].font = name_font
            work_sheet[f"F{str(current_row)}"].alignment = Alignment(horizontal="left", vertical='center',wrapText=True)
            work_sheet[f"F{str(current_row)}"].border = thin_border

            work_sheet[f"G{str(current_row)}"].border = thin_border
            print(new_invoice.get_list_item()[index].get_image_path())
            img = openpyxl.drawing.image.Image(f"data/{new_invoice.get_list_item()[index].get_image_path()}")
            img.height = 120
            img.width = 80
            print(type(img))
            img.anchor = f"H{str(current_row)}"
            ws[f"H{str(current_row)}"].alignment = Alignment(horizontal='center', vertical="center")
            ws.add_image(img)

            # wb.add_image(img, f"H{str(current_row)}")
            # work_sheet[f"H{str(current_row)}"].border = thin_border

            #Вага
            work_sheet[f"J{str(current_row)}"].value = new_invoice.get_list_item()[index].get_weight_item()
            work_sheet[f"J{str(current_row)}"].fill = PatternFill(fill_type='solid', start_color='ffff00', end_color='ffff00')
            work_sheet[f"J{str(current_row)}"].font = name_font
            work_sheet[f"J{str(current_row)}"].alignment = Alignment(horizontal="center", vertical='center')
            work_sheet[f"J{str(current_row)}"].fill = PatternFill(fill_type='solid', start_color='ffff00', end_color='ffff00')
            work_sheet[f"J{str(current_row)}"].border = thin_border

            #Кількість
            work_sheet[f"K{str(current_row)}"].value = new_invoice.get_list_item()[index].get_amount_item()
            work_sheet[f"K{str(current_row)}"].font = name_font
            work_sheet[f"K{str(current_row)}"].alignment = Alignment(horizontal="center", vertical='center')
            work_sheet[f"K{str(current_row)}"].border = thin_border

            #Вага помножена на кількість
            work_sheet[f"I{str(current_row)}"].value = f"=J{str(current_row)}*K{str(current_row)}"
            work_sheet[f"I{str(current_row)}"].alignment = Alignment(horizontal="center", vertical='center')
            work_sheet[f"I{str(current_row)}"].fill = PatternFill(fill_type='solid', start_color='ffff00', end_color='ffff00')
            work_sheet[f"I{str(current_row)}"].border = thin_border

            #Закупка з урахуванням знижки
            work_sheet[f"L{str(current_row)}"].value = f"={new_invoice.get_list_item()[index].get_price_item()}*((100-{self.get_discoiunt()})/100)"
            work_sheet[f"L{str(current_row)}"].font = name_font
            work_sheet[f"L{str(current_row)}"].alignment = Alignment(horizontal="center", vertical='center')
            work_sheet[f"L{str(current_row)}"].fill = PatternFill(fill_type='solid', start_color='ffff00', end_color='ffff00')
            work_sheet[f"L{str(current_row)}"].border = thin_border

            # Ціна за од ГРН
            work_sheet[f"O{str(current_row)}"].value = 0
            work_sheet[f"O{str(current_row)}"].font = name_font
            work_sheet[f"O{str(current_row)}"].alignment = Alignment(horizontal="center", vertical='center')
            work_sheet[f"O{str(current_row)}"].border = thin_border

            #Ціна за од EURO
            work_sheet[f"M{str(current_row)}"].value = f"=O{str(current_row)}/{float(self.get_rate().replace(',','.'))}"
            work_sheet[f"M{str(current_row)}"].font = name_font
            work_sheet[f"M{str(current_row)}"].alignment = Alignment(horizontal="center", vertical='center')
            work_sheet[f"M{str(current_row)}"].border = thin_border

            #Ціна разом EURO
            work_sheet[f"N{str(current_row)}"].value = f"=M{str(current_row)}*K{str(current_row)}"
            work_sheet[f"N{str(current_row)}"].font = name_font
            work_sheet[f"N{str(current_row)}"].alignment = Alignment(horizontal="center", vertical='center')
            work_sheet[f"N{str(current_row)}"].border = thin_border

            #Ціна разом ГРН
            work_sheet[f"P{str(current_row)}"].value = f"=O{str(current_row)}*K{str(current_row)}"
            #work_sheet[f"P{str(current_row)}"].value.number_format = openpyxl.styles.numbers.BUILTIN_FORMATS[2]
            work_sheet[f"P{str(current_row)}"].font = name_font
            work_sheet[f"P{str(current_row)}"].alignment = Alignment(horizontal="center", vertical='center')
            work_sheet[f"P{str(current_row)}"].border = thin_border

        img = None

        #last_row += 1
        work_sheet[f"B{str(last_row)}"].value = ""
        work_sheet[f"B{str(last_row)}"].border = thin_border
        work_sheet[f"C{str(last_row)}"].value = ""
        work_sheet[f"C{str(last_row)}"].border = thin_border
        work_sheet[f"D{str(last_row)}"].value = ""
        work_sheet[f"D{str(last_row)}"].fill = PatternFill(fill_type='solid', start_color='ffff00',
                                                              end_color='ffff00')
        work_sheet[f"D{str(last_row)}"].border = thin_border
        work_sheet[f"E{str(last_row)}"].fill = PatternFill(fill_type='solid', start_color='ffff00',
                                                              end_color='ffff00')
        work_sheet[f"E{str(last_row)}"].border = thin_border
        work_sheet[f"F{str(last_row)}"].value = ""
        work_sheet[f"F{str(last_row)}"].border = thin_border
        work_sheet[f"G{str(last_row)}"].value = ""
        work_sheet[f"G{str(last_row)}"].border = thin_border
        work_sheet[f"H{str(last_row)}"].value = ""
        work_sheet[f"H{str(last_row)}"].border = thin_border
        #work_sheet[f"I{str(last_row)}"].value = f"=СУММ({work_sheet[f'I{str(start_row)}'].value}:{work_sheet[f'I{str(last_row-1)}'].value}"

        work_sheet[f"I{str(last_row)}"].font = name_font
        work_sheet[f"I{str(last_row)}"].alignment = Alignment(horizontal="center", vertical='center')

        #work_sheet[f"I{str(last_row)}"] = f"=СУММ(I17:I{str(last_row-1)})"
        work_sheet[f"I{str(last_row)}"] = f"=СУММ(I17:I{str(last_row-1)})"
        work_sheet[f"I{str(last_row)}"].number_format = openpyxl.styles.numbers.BUILTIN_FORMATS[2]
        work_sheet[f"I{str(last_row)}"].fill = PatternFill(fill_type='solid', start_color='ffff00',
                                                              end_color='ffff00')
        work_sheet[f"I{str(last_row)}"].border = thin_border
        work_sheet[f"J{str(last_row)}"].value = ""
        work_sheet[f"J{str(last_row)}"].fill = PatternFill(fill_type='solid', start_color='ffff00',
                                                              end_color='ffff00')
        work_sheet[f"J{str(last_row)}"].border = thin_border
        work_sheet[f"K{str(last_row)}"].value = ""
        work_sheet[f"K{str(last_row)}"].border = thin_border
        work_sheet[f"L{str(last_row)}"].value = ""
        work_sheet[f"L{str(last_row)}"].fill = PatternFill(fill_type='solid', start_color='ffff00',
                                                              end_color='ffff00')
        work_sheet[f"L{str(last_row)}"].border = thin_border
        work_sheet[f"M{str(last_row)}"].value = ""
        work_sheet[f"M{str(last_row)}"].border = thin_border
        work_sheet[f"N{str(last_row)}"].value = ""
        work_sheet[f"N{str(last_row)}"].border = thin_border
        work_sheet[f"O{str(last_row)}"].value = ""
        work_sheet[f"O{str(last_row)}"].border = thin_border
        work_sheet[f"P{str(last_row)}"].value = ""
        work_sheet[f"P{str(last_row)}"].border = thin_border

        work_sheet.merge_cells('M10:P10')
        work_sheet.cell(row=10, column=13).value =  get_full_name_company(self.get_company_name())
        name_company_font = Font(size=9, bold=True)
        name_company_font.name = "Times New Roman"
        work_sheet.cell(row=10, column=13).font = name_company_font
        work_sheet.cell(row=10, column=13).alignment = Alignment(horizontal="right", vertical='center')

        #Разом
        work_sheet.merge_cells(f'F{str(last_row+1)}:M{last_row+1}')
        work_sheet[f"F{last_row+1}"].value = "Разом"
        #work_sheet.cell(row=6, column=last_row+1).value = "Разом"
        all_font = Font(size=9, bold=False)
        all_font.name = "Times New Roman"


        work_sheet[f"F{last_row + 1}"].font = all_font
        work_sheet[f"F{last_row + 1}"].alignment = Alignment(horizontal="left", vertical='center')
        print(str(last_row+1))

        #додаємо зображення https://www.excel-learn.com/insert-image-excel-sheet-openpyxl/
        wb.save(self.get_path_temp())
class Commercial_offer:
    pass
