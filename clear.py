from bs4 import BeautifulSoup

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
