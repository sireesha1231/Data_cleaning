from bs4 import BeautifulSoup
in_file = open('superbowl.html', 'r', encoding = 'utf-8')
mydata = []
s = in_file.read()
soup = BeautifulSoup(s,'html.parser')
div = soup.select('#mw-content-text')[0]
table = div.findChildren('table')[1]
rows = table.findChildren('tr')
out_file = open('result.csv', 'w', encoding = 'utf-8')
#print('Game number,year,winning team,score,losing team,venue')
out_file.write('Game number,year,winning team,score,losing team,venue\n')
for row in rows[1:51]:        
    cells = row.findChildren('td')
    gno = cells[0].findChildren('span')[1].text
    year = cells[1].findChildren('span')[0].text[8:12]
    wteam = cells[2].findChildren('span')[0].text.strip()[:-1].strip()
    score = cells[3].findChildren('span')[1].text
    lteam = cells[4].findChildren('span')[0].text.strip()[:-1].strip()
    venue = cells[5].findChildren('span')[0].text.strip()[:-1].strip()
    #print("{}, {}, {}, {}, {}".format(gno, year, wteam, score, lteam, venue))
    out_file.write("{}, {}, {}, {}, {}, {}\n".format(gno, year, wteam, score, lteam, venue))
    
#print('All done!')
out_file.close()
in_file.close()
