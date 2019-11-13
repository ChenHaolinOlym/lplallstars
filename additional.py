# 用于爬取选手及解说主持人的编号

from bs4 import BeautifulSoup
import csv


f = open("data.html", "r", encoding="utf-8")

data = f.read()

soup = BeautifulSoup(data, 'html.parser')

for li in soup.find_all('div', class_="sel-con-item"):
    with open("order.csv", "a+", newline="", encoding="utf-8") as file:
        f_csv = csv.writer(file)
        f_csv.writerow([li.text.strip(), li['id'].split('_')[1]])

for ul in soup.find_all('ul', class_="narrate-list"):
    lis = ul.find_all("li")
    for li in lis:
        with open("order.csv", "a+", newline="", encoding="utf-8") as file:
            f_csv = csv.writer(file)
            f_csv.writerow([li.text.strip(), li['id'].split('_')[1]])



f.close()
# print(soup)





