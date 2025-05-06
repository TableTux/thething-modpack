import requests as rs
from bs4 import BeautifulSoup
import urllib.request

matches = []
linestoclear = []

with open('modlist.html', 'r') as one:
    matches = one.readlines()
with open('CreaTechAcademy (1).html', 'r') as two:
    linestoclear = two.readlines()


toWrite = True
with open('coso.html', 'w') as file:
    for line in linestoclear:
        toWrite = True
        soup = BeautifulSoup(line, 'html.parser')
        data = soup.find('a').string
        for match in matches:
            if match.strip().upper() == data.strip().upper():
                toWrite = False
                matches.remove(match)
                break
        if toWrite:
            file.write(line)
        
                
with open('coso.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    for link in soup.find_all('a'):
        badurl = link.get('href')
        #res = rs.head(badurl, allow_redirects=True)
        print(link.string)