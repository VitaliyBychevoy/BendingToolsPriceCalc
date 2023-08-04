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

class Commercial_offer:
    pass


class Calculation:
    pass
