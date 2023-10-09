from openpyxl import *

DEFAULT_PATH = "vectortool_customers/customers_vectortool.xlsx"

company_index: int = 0


def get_short_name_list() -> list:

    short_name_list: list = ["Оберіть компанію"]

    wb = load_workbook(DEFAULT_PATH)
    worksheet = wb[" Companies"]

    rows = worksheet.max_row

    for item in range(1, rows):
        short_name_list.append(worksheet["A" + str(item)].value)

    wb.close()
    return short_name_list

def get_full_name_list() -> list:
    full_name_list: list = []
    wb = load_workbook(DEFAULT_PATH)
    worksheet = wb[" Companies"]

    rows = worksheet.max_row

    for item in range(1, rows):
        full_name_list.append(worksheet["B" + str(item)].value)

    wb.close()
    return full_name_list


def get_full_name_company(short_name: str) -> str:
    short_name_list: list = get_short_name_list()[1:]
    full_name_index: int = short_name_list.index(short_name) + 1
    wb = load_workbook(DEFAULT_PATH)
    worksheet = wb[" Companies"]
    full_name_company = worksheet["B" + str(full_name_index)].value
    wb.close()
    return full_name_company


