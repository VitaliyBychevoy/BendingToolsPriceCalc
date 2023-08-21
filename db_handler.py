import openpyxl
from openpyxl import *
from openpyxl.utils import get_column_letter

DB_PATH = ""
COMMERCIAL_OFFER_EMPTY_SAMPLE_PATH = ""

CALCULATION_EMPTY_SMPLE_PATH = ""



class My_db:

    def __init__(self):
        self.path_db = DB_PATH

    def get_type_holder_list(self) -> list:
        pass

    def get_type_item_list(self) -> list:
        pass

    def get_code_list(self, holder_item: list[str]) -> list:
        holder: str = holder_item[0]
        item: str = holder_item[1]
        wb = load_workbook("data/DB_bending.xlsx")
        code_list: list = [" "]
        work_sheet = wb[item]
        max_row_item = work_sheet.max_row
        for i in range(1, max_row_item + 1):
            if work_sheet["B"+str(i)].value == holder:
                code_list.append(work_sheet["C"+str(i)].value[0:6])
        result_list = list(set(code_list))
        result_list.sort()
        return result_list

    def get_length_item(self, holder_item_code: list) -> list:
        wb = load_workbook("data/DB_bending.xlsx")
        holder: str = holder_item_code[0]
        item: str = holder_item_code[1]
        code: str = holder_item_code[2]
        work_sheet = wb[item]
        length_list: list = [" "]
        max_row_item = work_sheet.max_row
        for i in range(1, max_row_item + 1):
            if work_sheet["B"+str(i)].value == holder and work_sheet["C"+str(i)].value[0:6] == code:
                length_list.append(work_sheet["G"+str(i)].value)
        return length_list

    @staticmethod
    def get_en_description(data_list: list) -> str:
        en_description = "en_description"
        holder: str = data_list[0]
        item: str = data_list[1]
        code: str = data_list[2]
        length: str = data_list[3]
        full_code: str = data_list[4]
        wb = load_workbook("data/DB_bending.xlsx")
        work_sheet = wb[item]
        max_row_item = 0
        max_row_item = work_sheet.max_row
        for i in range(1, max_row_item + 1):
            if work_sheet["C"+str(i)].value == full_code:
                return work_sheet["D"+str(i)].value
        return en_description

    @staticmethod
    def get_ua_description(data_list: list) -> str:
        ua_description = "ua_description"
        holder: str = data_list[0]
        item: str = data_list[1]
        code: str = data_list[2]
        length: str = data_list[3]
        full_code: str = data_list[4]
        wb = load_workbook("data/DB_bending.xlsx")
        work_sheet = wb[item]
        max_row_item = 0
        max_row_item = work_sheet.max_row
        for i in range(1, max_row_item + 1):
            if work_sheet["C"+str(i)].value == full_code:
                return work_sheet["E"+str(i)].value
        return ua_description
    @staticmethod
    def get_length(length: str) -> str:
        # if length in ["+", "="]:
        #     pass
        if "=" in str(length):
            return length[-3:]

        return length


    def get_item(self, parameters_list: list) -> list:
        type_loder: str = parameters_list[0]
        item: str = parameters_list[1]
        code: str = parameters_list[2]
        length_item: str = My_db.get_length(parameters_list[3])

    @staticmethod
    def get_full_code_item(parameters: list) -> str:
        full_code: str = ""
        holder: str = parameters[0]
        item: str = parameters[1]
        code: str = parameters[2]
        length: str = parameters[3]
        wb = load_workbook("data/DB_bending.xlsx")
        work_sheet = wb[item]
        max_row_item = 0
        max_row_item = work_sheet.max_row

        for i in range(1, max_row_item + 1):
            if work_sheet["C"+str(i)].value[0:6] == code and \
                    str(work_sheet["G" + str(i)].value) == length:

                return work_sheet["C" + str(i)].value
        return full_code

    @staticmethod
    def get_info_item(data_list: list) -> dict:
        info_item: dict = {}
        wb = load_workbook("data/DB_bending.xlsx")
        work_sheet = wb[data_list[1]]
        max_row_item = work_sheet.max_row
        max_column_item = work_sheet.max_column
        for i in range(1, max_row_item):
            if work_sheet["C" + str(i)].value == data_list[-1]:
                info_item["type_holder"] = work_sheet["B" + str(i)].value
                info_item["item"] = work_sheet.title
                info_item["code_item"] = work_sheet["C" + str(i)].value
                info_item["en_name_item"] = work_sheet["D" + str(i)].value
                info_item["ua_name_item"] = work_sheet["E" + str(i)].value
                info_item["image_path"] = work_sheet["F" + str(i)].value
                info_item["length_item"] = str(work_sheet["G" + str(i)].value)
                info_item["weight"] = work_sheet["H" + str(i)].value
                info_item["price_item"] = work_sheet["I" + str(i)].value
                info_item["parameters"] = {}
                for j in range(9, max_column_item):
                    info_item["parameters"][work_sheet[chr(65 + j) + "1"].value] = work_sheet[chr(65 + j) + str(i)].value

        return info_item

class Pre_commercial_offer_xlsx():

    def __init__(self):
        self.path_file

class Calculation:
    pass
