from datetime import datetime, date

from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment
from openpyxl.styles.borders import Border, Side
import openpyxl.styles.numbers
from openpyxl.styles import Font, Fill #Стилі для текста
from openpyxl.styles import PatternFill #Cтили для ячеєк


def name_offer(customer_name: str) -> str:
    this_moment_list = str(datetime.now()).split(" ")
    today = this_moment_list[0].split("-")[::-1]
    this_time = this_moment_list[1].split(":")[:2]
    return f"{customer_name}_({this_time[0]} {this_time[1]})_{today[0]}.{today[1]}.{today[2]}.xlsx"


#Встановлюємо ширину та колір стовбчиків
def column_style(
        sheet: openpyxl.worksheet.worksheet.Worksheet
) -> None:
    sheet.column_dimensions['A'].width = 1 * 1.72
    sheet.column_dimensions['B'].width = 1.57 * 1.5
    sheet.column_dimensions['C'].width = 1 * 1.72
    sheet.column_dimensions['D'].width = 24.43 * 1.72
    sheet.column_dimensions['D'].fill = (PatternFill(fill_type='solid',
                                                     start_color='ffff00',
                                                     end_color='ffff00'))
    sheet.column_dimensions['E'].width = 1.14 * 1.72
    sheet.column_dimensions['E'].fill = (PatternFill(fill_type='solid',
                                                     start_color='ffff00',
                                                     end_color='ffff00'))
    sheet.column_dimensions['F'].width = 43.29 * 1.0169
    sheet.column_dimensions['G'].width = 1.43 * 1.5
    sheet.column_dimensions['H'].width = 25.71 * 1.0284
    sheet.column_dimensions['I'].width = 4.43 * 1.72
    sheet.column_dimensions['I'].fill = (PatternFill(fill_type='solid',
                                                     start_color='ffff00',
                                                     end_color='ffff00'))
    sheet.column_dimensions['J'].width = 2.71 * 1.72
    sheet.column_dimensions['J'].fill = (PatternFill(fill_type='solid',
                                                     start_color='ffff00',
                                                     end_color='ffff00'))
    sheet.column_dimensions['K'].width = 3.14 * 1.25
    sheet.column_dimensions['L'].width = 4.71 * 1.72
    sheet.column_dimensions['L'].fill = (PatternFill(fill_type='solid',
                                                     start_color='ffff00',
                                                     end_color='ffff00'))
    sheet.column_dimensions['M'].width = 9 * 1.08
    sheet.column_dimensions['N'].width = 9 * 1.08
    sheet.column_dimensions['O'].width = 9 * 1.08
    sheet.column_dimensions['P'].width = 9 * 1.08
    sheet.column_dimensions['Q'].width = 1 * 1.72


#Оброблюємо строки до таблички
def row_style(
        sheet: openpyxl.worksheet.worksheet.Worksheet
) -> None:
    sheet.row_dimensions[6].height = 15 * 0.3
    sheet.row_dimensions[7].height = 15 * 2.38
    sheet.row_dimensions[8].height = 15 * 4.35
    sheet.row_dimensions[9].height = 15 * 0.24
    sheet.row_dimensions[10].height = 15 * 0.75
    sheet.row_dimensions[11].height = 15 * 0.24
    sheet.row_dimensions[12].height = 15 * 0.75
    sheet.row_dimensions[13].height = 15 * 0.24
    sheet.row_dimensions[14].height = 15 * 0.8
    sheet.row_dimensions[15].height = 15 * 0.45
    sheet.row_dimensions[16].height = 15 * 0.65


def merge_cell(
        sheet: openpyxl.worksheet.worksheet.Worksheet
) -> None:
    sheet.merge_cells(f'B8:P8')
    sheet.merge_cells(f'M10:P10')
    sheet.merge_cells(f'B12:P12')


def fill_before_table(
        sheet: openpyxl.worksheet.worksheet.Worksheet
) -> None:
    sheet['F10'] = "=TODAY()"

