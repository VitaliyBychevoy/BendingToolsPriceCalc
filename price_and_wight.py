from openpyxl import load_workbook

root: str = "data/PRICE-LIST TS-2022.xlsx"
work_book: str = "data/DB_bending.xlsx"


wb_1 = load_workbook(root)

wb_2 = load_workbook(work_book)

sheet_1 = wb_1["LISTINO 2022"]

sheet_2 = wb_2["Матриця багаторучова"]
wb_2.active
weight = None
price = None

for index in range(2, sheet_2.max_row + 1):
    if sheet_2["C" +str(index)] == sheet_1["B" +str(index)]:
        sheet_2["H" +str(index)] = sheet_1["G" +str(index)]
        sheet_2["I" +str(index)] = sheet_1["E" +str(index)]
        continue

wb_2.save("data/DB_bending_1.xlsx")