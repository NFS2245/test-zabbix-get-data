import pandas as pd
import requests
from openpyxl import load_workbook
from openpyxl.styles import Border, Side

with open(r'F:/magang/New folder/data.txt', 'r') as file:
    input_data_list = [line.strip() for line in file.readlines()]
tables_list = []
added_data = set()
for input_data in input_data_list:
    if input_data in added_data:
        continue

    url = f'https://mrtg.iconpln.co.id/check/zabbix?s={input_data}'
    print(f'Meminta URL: {url}')

    try:
        response = requests.get(url)
        response.raise_for_status()  

        if response.status_code == 200:
            print(f'Success: Dapatkan data untuk {input_data}')
            try:
                tables = pd.read_html(url)
                if tables:
                    table = tables[0]
                    table.insert(0, 'Data', [''] * len(table))
                    table.at[0, 'Data'] = input_data  
                    tables_list.append(table)
                else:
                    empty_row = pd.DataFrame([[input_data, None, None, None]], columns=['Data', 1, 2, 3])
                    tables_list.append(empty_row)
            except Exception as e:
                print(f'Gagal membaca tabel untuk {input_data}: {e}')
                empty_row = pd.DataFrame([[input_data, None, None, None]], columns=['Data', 1, 2, 3])
                tables_list.append(empty_row)
    except requests.exceptions.RequestException as e:
        print(f'Error saat mengakses URL {url}: {e}')
        empty_row = pd.DataFrame([[input_data, None, None, None]], columns=['Data', 1, 2, 3])
        tables_list.append(empty_row)

    added_data.add(input_data)

df_with_no_spacing = pd.concat(tables_list, ignore_index=True)

excel_path = r'F:/magang/New folder/output.xlsx'
df_with_no_spacing.to_excel(excel_path, index=False)

wb = load_workbook(excel_path)
ws = wb.active

border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

for row in ws.iter_rows():
    for cell in row:
        cell.border = border

for col in ws.columns:
    max_length = 0
    column = col[0].column_letter  
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2)  
    ws.column_dimensions[column].width = adjusted_width
wb.save(excel_path)
print(f'Data berhasil disimpan ke {excel_path}.')
