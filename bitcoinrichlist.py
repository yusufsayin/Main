######## import bileşenleri
import requests
import bs4
##### boş bir liste olduğunu belirtmemiz gerekiyor.
son = []

###### for döngüsü başlatarak sayfa adreslerini 1 den 99 a kadar sıralamasını sağlıyoruz.
for h in range(1,99):
  h = str(h)
######## siteye erişim adresin olduğun yeri bulma
  url = "https://bitinfocharts.com/top-100-richest-bitcoin-addresses-" + h + ".html"
  response = requests.get(url)
  data = []
####site içeriğini data haline getirip şekillendiriyoruz.
  html_icerigi = response.content
  soup = bs4.BeautifulSoup(html_icerigi,"html.parser")
  table = soup.find('table', attrs={"class":"table table-striped abtb"})
  table_body = table.find('tbody')
  rows = table_body.find_all('tr')
  
  for row in rows:
      cols = row.find_all('td')
      cols = [ele.text.strip() for ele in cols]
      data.append([ele for ele in cols if ele])
  a = 0
  
  for i in data:
      print(data[a][1])
      if len(data[a][1]) == 34:
        son.append(data[a][1])
      a = a + 1
print("cüzdan adresleri", len(son), son)
############ cüzdan adresini alıp not defterine kaydetme ve çıkış
print(son)
ths = open("btc_richlist_liste_ciktisi.txt", "w")
for item in son:  
  ths.write("%s\n" % item)
ths.close()
