from datetime import datetime, date
import openpyxl.styles.numbers

from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment
from openpyxl.styles.borders import Border, Side
import openpyxl.styles.numbers
from openpyxl.styles import Font, Fill #Стилі для текста
from openpyxl.styles import PatternFill #Cтили для ячеєк

from vectortool_customers.customers_db import *
from model import *

#Шрифти
company_description_font = Font(size=8, italic=True)
company_description_font.name = "Times New Roman"


date_font = Font(size=9,  bold=True)
date_font.name = "Times New Roman"

customer_name_font = Font(size=9,  bold=True)
customer_name_font.name = "Times New Roman"

table_title_font = Font(size=10,  bold=True)
table_title_font.name = "Times New Roman"

table_head_font = Font(size=5,  bold=True)
table_head_font.name = "Times New Roman"

description_font = Font(size=8)
description_font.name = "Arial Narrow"

description_ua_font = Font(size=7)
description_ua_font.name = "Times New Roman"

position_font = Font(size=7, bold=True)
position_font.name = "Times New Roman"

numbers_table_font = Font(size=7)
numbers_table_font.name = "Times New Roman"


#Рамка
thin_border = Border(left=Side(style='thin'),
                     right=Side(style='thin'),
                     top=Side(style='thin'),
                     bottom=Side(style='thin'))

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
    sheet.column_dimensions['D'].width = 24.43
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

#Поєднуємо необхідні комірки до таблиці
def merge_cells_before_table(
        sheet: openpyxl.worksheet.worksheet.Worksheet
) -> None:
    sheet.merge_cells(f'B8:P8')
    sheet.merge_cells(f'M10:P10')
    sheet.merge_cells(f'B12:P12')


def fill_company_info(
        sheet: openpyxl.worksheet.worksheet.Worksheet
) -> None:
    sheet['B8'].font = company_description_font
    sheet['B8'].alignment = Alignment(
        horizontal="center",
        vertical='center',
        wrapText=True
    )
    sheet['B8'].value = \
    "Компанія Tecnostamp (TS) засновано у 1978 году в м." +\
     " П'яченца на півночі Італії і сьогодні є найбільшим " +\
      "світовим виробником листозгинального інструменту. " +\
      "Бренд Tecnostamp " +\
     "представлений більш ніж в 30-ти країнах світу і займає " +\
      "провідні позиції на ринках Німеччини, Росії, Італії та США. " +\
     "Підбір інструменту за кресленнями та технічні консультації. " +\
     "Проектування спеціального інструменту під нестандартні " +\
     "задачі.  Обираючи бренд Tecnostamp, Ви отримуєте те " +\
     "надійний інструмент для гнуття преміум класу з великим " +\
     "терміном служби і гарантією бездоганної якості. Інструмент " +\
     "для гнуття для наступних верстатів:AMADA; TRUMPF; MVD; " +\
     "INAN;PRIMA POWER; FINN POWER; LVD;Bystronic; " +\
     "Safan; Salvagnini;EHT; Boschert; Darley;Gasparini; HACO; " +\
     "Farina; Schiavi; Adira; Guifil; Jordi; Ursviken; Hammerle; " +\
     "Dener; Durma; Ermaksan; Baykal."


def fill_today_before_table(
        sheet: openpyxl.worksheet.worksheet.Worksheet
) -> None:
    #Загальний формат комірки змінюємо на формат дату
    sheet['F10'].number_format = \
        openpyxl.styles.numbers.BUILTIN_FORMATS[14]
    sheet['F10'] = "=TODAY()"
    sheet['F10'].font = date_font
    sheet['F10'].alignment = Alignment(
        horizontal="left",
        vertical='top',
        wrapText=True
    )


#Заповнюємо назву компанії
def fill_customer_name(
        sheet: openpyxl.worksheet.worksheet.Worksheet,
        customer_name: str
) -> None:
    sheet["M10"].font = customer_name_font
    sheet['M10'].alignment = Alignment(
        horizontal="right",
        vertical='top',
        wrapText=True
    )
    sheet["M10"].value = get_full_name_company(customer_name)

#Заповнюємо назву таблиці
def fill_title_table(
        sheet: openpyxl.worksheet.worksheet.Worksheet
) -> None:
    sheet['B12'] = \
    "Техніко-комерційна пропозиція на постачання інструменту " +\
    "TECNOSTAMP S.R.L для листозгинального пресу з ЧПК"
    sheet['B12'] .font =  table_title_font


    sheet['B12'].alignment = Alignment(
    horizontal="center",
    vertical='center',
    wrapText=True
    )

#Заповнюємо назву таблиці
def fill_table_head(
        sheet: openpyxl.worksheet.worksheet.Worksheet
) -> None:
    sheet['B14'].value = "№"
    sheet['B14'].font = table_head_font
    sheet['B14'].border = thin_border
    sheet['B14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['C14'].border = thin_border

    sheet['D14'].value = "Description"
    sheet['D14'].font = table_head_font
    sheet['D14'].border = thin_border
    sheet['D14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )
    sheet['D14'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )

    sheet['E14'].border = thin_border
    sheet['E14'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )

    sheet['F14'].value = "Опис"
    sheet['F14'].font = table_head_font
    sheet['F14'].border = thin_border
    sheet['F14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['G14'].value = "/"
    sheet['G14'].font = table_head_font
    sheet['G14'].border = thin_border
    sheet['G14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['H14'].value = "Розмір, мм"
    sheet['H14'].font = table_head_font
    sheet['H14'].border = thin_border
    sheet['H14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['I14'].border = thin_border
    sheet['I14'].fill = PatternFill(
        fill_type='solid', start_color='ffff00', end_color='ffff00')

    sheet['J14'].value = "Вага"
    sheet['J14'].font = table_head_font
    sheet['J14'].border = thin_border
    sheet['J14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )
    sheet['J14'].fill = PatternFill(
        fill_type='solid', start_color='ffff00', end_color='ffff00')

    sheet['K14'].value = "Кіл-ть"
    sheet['K14'].font = table_head_font
    sheet['K14'].border = thin_border
    sheet['K14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['L14'].value = "ЗАКУПКА"
    sheet['L14'].font = table_head_font
    sheet['L14'].border = thin_border
    sheet['L14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )
    sheet['L14'].fill = PatternFill(
        fill_type='solid', start_color='ffff00', end_color='ffff00')

    sheet['M14'].value = "Ціна од. EURO"
    sheet['M14'].font = table_head_font
    sheet['M14'].border = thin_border
    sheet['M14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['N14'].value = "Ціна разом EURO"
    sheet['N14'].font = table_head_font
    sheet['N14'].border = thin_border
    sheet['N14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['O14'].value = "Ціна од. ГРН"
    sheet['O14'].font = table_head_font
    sheet['O14'].border = thin_border
    sheet['O14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['P14'].value = "Ціна разом ГРН"
    sheet['P14'].font = table_head_font
    sheet['P14'].border = thin_border
    sheet['P14'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

def fill_number_string(
        sheet: openpyxl.worksheet.worksheet.Worksheet
) -> None:
    sheet['B15'].value = 1
    sheet['B15'].font = table_head_font
    sheet['B15'].border = thin_border
    sheet['B15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['C15'].border = thin_border
    sheet['C15'].value = 2
    sheet['C15'].font = table_head_font
    sheet['C15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['D15'].font = table_head_font
    sheet['D15'].border = thin_border
    sheet['D15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )
    sheet['D15'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )

    sheet['E15'].border = thin_border
    sheet['E15'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )

    sheet['F15'].value = 3
    sheet['F15'].font = table_head_font
    sheet['F15'].border = thin_border
    sheet['F15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['G15'].font = table_head_font
    sheet['G15'].border = thin_border
    sheet['G15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['H15'].value = 4
    sheet['H15'].font = table_head_font
    sheet['H15'].border = thin_border
    sheet['H15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['I15'].border = thin_border
    sheet['I15'].fill = PatternFill(
        fill_type='solid', start_color='ffff00', end_color='ffff00')


    sheet['J15'].font = table_head_font
    sheet['J15'].border = thin_border
    sheet['J15'].fill = PatternFill(
        fill_type='solid', start_color='ffff00', end_color='ffff00')

    sheet['K15'].value = 5
    sheet['K15'].font = table_head_font
    sheet['K15'].border = thin_border
    sheet['K15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )


    sheet['L15'].font = table_head_font
    sheet['L15'].border = thin_border
    sheet['L15'].fill = PatternFill(
        fill_type='solid', start_color='ffff00', end_color='ffff00')

    sheet['M15'].value = 6
    sheet['M15'].font = table_head_font
    sheet['M15'].border = thin_border
    sheet['M15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['N15'].value = 7
    sheet['N15'].font = table_head_font
    sheet['N15'].border = thin_border
    sheet['N15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['O15'].value = 8
    sheet['O15'].font = table_head_font
    sheet['O15'].border = thin_border
    sheet['O15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet['P15'].value = 9
    sheet['P15'].font = table_head_font
    sheet['P15'].border = thin_border
    sheet['P15'].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

def empty_string(
        sheet: openpyxl.worksheet.worksheet.Worksheet,
        number_string: int
) -> None:

    sheet[f'B{str(number_string)}'].border = thin_border

    sheet[f'C{str(number_string)}'].border = thin_border

    sheet[f'D{str(number_string)}'].border = thin_border
    sheet[f'D{str(number_string)}'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )

    sheet[f'E{str(number_string)}'].border = thin_border
    sheet[f'E{str(number_string)}'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )

    sheet[f'F{str(number_string)}'].border = thin_border

    sheet[f'G{str(number_string)}'].border = thin_border

    sheet[f'H{str(number_string)}'].border = thin_border

    sheet[f'I{str(number_string)}'].border = thin_border
    sheet[f'I{str(number_string)}'].fill = PatternFill(
        fill_type='solid', start_color='ffff00', end_color='ffff00')

    sheet[f'J{str(number_string)}'].border = thin_border
    sheet[f'J{str(number_string)}'].fill = PatternFill(
        fill_type='solid', start_color='ffff00', end_color='ffff00')

    sheet[f'K{str(number_string)}'].border = thin_border

    sheet[f'L{str(number_string)}'].border = thin_border
    sheet[f'L{str(number_string)}'].fill = PatternFill(
        fill_type='solid', start_color='ffff00', end_color='ffff00')

    sheet[f'M{str(number_string)}'].border = thin_border

    sheet[f'N{str(number_string)}'].border = thin_border

    sheet[f'O{str(number_string)}'].border = thin_border

    sheet[f'P{str(number_string)}'].border = thin_border


def write_row(
        sheet: openpyxl.worksheet.worksheet.Worksheet,
        item: Item,
        number_string: int,
        index: int,
        provider_discount: float,
        rate: str
) -> None:
    sheet[f"B{str(number_string)}"].value = index + 1
    sheet[f"B{str(number_string)}"].border = thin_border
    sheet[f"B{str(number_string)}"].alignment = \
        Alignment(horizontal="center", vertical='center')
    sheet[f"B{str(number_string)}"].font = position_font

    sheet[f"C{str(number_string)}"].border = thin_border

    sheet[f"D{str(number_string)}"].border = thin_border
    sheet[f"D{str(number_string)}"].value = \
        item.get_en_name_item()
    sheet[f"D{str(number_string)}"].font = description_font
    sheet[f"D{str(number_string)}"].alignment = Alignment(
        horizontal="left",
        vertical='center',
        wrapText=True
    )
    sheet[f'D{str(number_string)}'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )

    sheet[f"E{str(number_string)}"].border = thin_border
    sheet[f'E{str(number_string)}'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )

    sheet[f"F{str(number_string)}"].border = thin_border
    sheet[f"F{str(number_string)}"].value = \
        item.get_ua_name_item()
    sheet[f"F{str(number_string)}"].font = description_ua_font
    sheet[f"F{str(number_string)}"].alignment = Alignment(
        horizontal="left",
        vertical='center',
        wrapText=True
    )

    sheet[f"G{str(number_string)}"].border = thin_border

    sheet[f"H{str(number_string)}"].border = thin_border

    sheet[f"K{str(number_string)}"].border = thin_border
    sheet[f"K{str(number_string)}"].value = item.get_amount_item()
    sheet[f"K{str(number_string)}"].font = numbers_table_font
    sheet[f"K{str(number_string)}"].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet[f"J{str(number_string)}"].border = thin_border
    sheet[f"J{str(number_string)}"].font = numbers_table_font
    sheet[f"J{str(number_string)}"].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )
    sheet[f'J{str(number_string)}'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )
    sheet[f"J{str(number_string)}"].value = \
        item.get_weight_item()

    sheet[f"I{str(number_string)}"].border = thin_border
    sheet[f"I{str(number_string)}"].font = numbers_table_font
    sheet[f"I{str(number_string)}"].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )
    sheet[f'I{str(number_string)}'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )

    sheet[f"I{str(number_string)}"].value = \
        f"=J{str(number_string)}*K{str(number_string)}"

    sheet[f"L{str(number_string)}"].border = thin_border
    sheet[f"L{str(number_string)}"].font = numbers_table_font
    sheet[f"L{str(number_string)}"].value = \
        f"={item.get_price_item()}*((100-{provider_discount})/100)"
    sheet[f'L{str(number_string)}'].fill = PatternFill(
        fill_type='solid',
        start_color='ffff00',
        end_color='ffff00'
    )
    sheet[f"L{str(number_string)}"].alignment = Alignment(
        horizontal="center",
        vertical='center'
    )

    sheet[f"O{str(number_string)}"].border = thin_border
    sheet[f"O{str(number_string)}"].value = 0
    sheet[f"O{str(number_string)}"].font = numbers_table_font
    sheet[f"O{str(number_string)}"].alignment = Alignment(
        horizontal="right",
        vertical='center'
    )

    sheet[f"M{str(number_string)}"].border = thin_border
    sheet[f"M{str(number_string)}"].value = \
        f"=O{str(number_string)}/{float(str(rate).replace(',','.'))}"
    sheet[f"M{str(number_string)}"].font = numbers_table_font
    sheet[f"M{str(number_string)}"].alignment = Alignment(
        horizontal="right",
        vertical='center'
    )

    sheet[f"N{str(number_string)}"].border = thin_border
    sheet[f"P{str(number_string)}"].border = thin_border