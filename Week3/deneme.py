import requests
from bs4 import BeautifulSoup
import time

from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells

for i in range(10):
    url = "https://www.bloomberght.com/doviz/dolar"
    pagetemp = requests.get(url)

    page = pagetemp.content

    soup = BeautifulSoup(page,"html.parser")

    divs = soup.find_all('div', class_= "detailHeadLine3")

    b = divs[0].find_all('b')

    print(b)

    result = b[0]
    print(result)
    str_result = result.get_text()
    ws.append([str_result])

    print(result)
    time.sleep(2)

wb.save("sample.xlsx")
