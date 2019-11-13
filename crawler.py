# 主爬虫
import requests
import json
import time
import csv
from bs4 import BeautifulSoup

Liver = {}

Player = {}

# Get Liver List
with open("Liver.csv", "r", encoding="utf-8") as LiverCSV:
    Liver_reader = csv.reader(LiverCSV)
    for i in Liver_reader:
        Liver[str(i[0])] = i[1]
# Get Player List
with open("Player.csv", "r", encoding="utf-8") as PlayerCSV:
    Player_reader = csv.reader(PlayerCSV)
    for i in Player_reader:
        Player[str(i[0])] = i[1]


header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# urlLiver = "https://lol.sw.game.qq.com/lol/commact/?proj=a20191025allstarpc&c=a20191025allstarpcVlixhli&a=get_ticket&act=liver"
# urlNewStars = "https://lol.sw.game.qq.com/lol/commact/?proj=a20191025allstarpc&c=a20191025allstarpcVlixhli&a=get_ticket&act=newstars"
# # urlLeader = "https://lol.sw.game.qq.com/lol/commact/?proj=a20191025allstarpc&c=a20191025allstarpcVlixhli&a=get_leader" 此链接没有票数
# urlAllStars = "https://lol.sw.game.qq.com/lol/commact/?proj=a20191025allstarpc&c=a20191025allstarpcVlixhli&a=get_ticket&act=allstars"
# urlLeader = "https://lol.sw.game.qq.com/lol/commact/?proj=a20191025allstarpc&c=a20191025allstarpcVlixhli&a=get_ticket&act=leader"

url = "https://lol.sw.game.qq.com/lol/commact/"

# Liver

r = requests.get(url, headers=header, params={'proj':'a20191025allstarpc','c':'a20191025allstarpcVlixhli','a':'get_ticket','act':'liver'})
LiverSdw = r.content.decode('utf-8')
LiverText = json.loads(LiverSdw.split("var res = ")[1])

with open(f"Liver{time.strftime('%Y%m%d%H%M',time.localtime(time.time()))}.csv", "w") as f:
    pass
for i in LiverText['data'].keys():
    with open(f"Liver{time.strftime('%Y%m%d%H%M',time.localtime(time.time()))}.csv", "a+", newline="", encoding="utf-8") as f:
        f_csv = csv.writer(f)
        f_csv.writerow([Liver[i], LiverText['data'][i]['num']])

# NewStars

r = requests.get(url, headers=header, params={'proj':'a20191025allstarpc','c':'a20191025allstarpcVlixhli','a':'get_ticket','act':'newstars'})
NewStarsSdw = r.content.decode('utf-8')
NewStarsText = json.loads(NewStarsSdw.split("var res = ")[1])

with open(f"NewStars{time.strftime('%Y%m%d%H%M',time.localtime(time.time()))}.csv", "w") as f:
    pass
for i in NewStarsText['data'].keys():
    with open(f"NewStars{time.strftime('%Y%m%d%H%M',time.localtime(time.time()))}.csv", "a+", newline="", encoding="utf-8") as f:
        f_csv = csv.writer(f)
        f_csv.writerow([Player[i], NewStarsText['data'][i]['num']])

# Leader

r = requests.get(url, headers=header, params={'proj':'a20191025allstarpc','c':'a20191025allstarpcVlixhli','a':'get_ticket','act':'leader'})
LeaderSdw = r.content.decode('utf-8')
LeaderText = json.loads(LeaderSdw.split("var res = ")[1])

with open(f"Leader{time.strftime('%Y%m%d%H%M',time.localtime(time.time()))}.csv", "w") as f:
    pass
for i in LeaderText['data'].keys():
    if i != '0':
        with open(f"Leader{time.strftime('%Y%m%d%H%M',time.localtime(time.time()))}.csv", "a+", newline="", encoding="utf-8") as f:
            f_csv = csv.writer(f)
            f_csv.writerow([Player[i], LeaderText['data'][i]['num']])

# AllStars

r = requests.get(url, headers=header, params={'proj':'a20191025allstarpc','c':'a20191025allstarpcVlixhli','a':'get_ticket','act':'allstars'})
AllStarsSdw = r.content.decode('utf-8')
AllStarsText = json.loads(AllStarsSdw.split("var res = ")[1])

with open(f"AllStars{time.strftime('%Y%m%d%H%M',time.localtime(time.time()))}.csv", "w") as f:
    pass
for i in AllStarsText['data'].keys():
    with open(f"AllStars{time.strftime('%Y%m%d%H%M',time.localtime(time.time()))}.csv", "a+", newline="", encoding="utf-8") as f:
        f_csv = csv.writer(f)
        f_csv.writerow([Player[i], AllStarsText['data'][i]['num']])

