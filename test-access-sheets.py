import openpyxl
ws = openpyxl.load_workbook('sample.xlsx')

#print (ws.get_sheet_names())

#Accessing sheet by name and printing values of cells
sheet = ws.get_sheet_by_name('Sheet2')
print (sheet['A2'].value)

#Aceesing multiple columns
multiple_cells = sheet['A1':'B6']
for row in multiple_cells:
    for cell in row:
        print (cell.value)

