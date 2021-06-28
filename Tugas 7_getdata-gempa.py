import requests
from bs4 import BeautifulSoup

web = requests.get('https://www.bmkg.go.id/gempabumi/gempabumi-terkini.bmkg')
data = web.text
bs = BeautifulSoup(data, "html.parser")
body = bs.find('tbody')
baris = body.find_all('tr')
for i in baris:
    kolom = i.find_all('td')
    print("No\t\t:",kolom[0].text)
    print("Waktu\t\t:",kolom[1].text)
    print("Lintang\t\t:",kolom[2].text)
    print("Bujur\t\t:",kolom[3].text)
    print("Magnitudo\t:",kolom[4].text)
    print("Kedalaman\t:",kolom[5].text)
    print("Wilayah\t\t:",kolom[6].text)
    print("\n")