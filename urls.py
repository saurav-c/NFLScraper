from urllib.request import urlopen
from bs4 import BeautifulSoup

fh = open("urls2.txt", "a")

ulist = []
ulist.append('https://www.pro-football-reference.com/players/A/')
ulist.append('https://www.pro-football-reference.com/players/B/')
ulist.append('https://www.pro-football-reference.com/players/C/')
ulist.append('https://www.pro-football-reference.com/players/D/')
ulist.append('https://www.pro-football-reference.com/players/E/')
ulist.append('https://www.pro-football-reference.com/players/F/')
ulist.append('https://www.pro-football-reference.com/players/G/')
ulist.append('https://www.pro-football-reference.com/players/H/')
ulist.append('https://www.pro-football-reference.com/players/I/')
ulist.append('https://www.pro-football-reference.com/players/J/')
ulist.append('https://www.pro-football-reference.com/players/K/')
ulist.append('https://www.pro-football-reference.com/players/L/')
ulist.append('https://www.pro-football-reference.com/players/M/')
ulist.append('https://www.pro-football-reference.com/players/N/')
ulist.append('https://www.pro-football-reference.com/players/O/')
ulist.append('https://www.pro-football-reference.com/players/P/')
ulist.append('https://www.pro-football-reference.com/players/Q/')
ulist.append('https://www.pro-football-reference.com/players/R/')
ulist.append('https://www.pro-football-reference.com/players/S/')
ulist.append('https://www.pro-football-reference.com/players/T/')
ulist.append('https://www.pro-football-reference.com/players/U/')
ulist.append('https://www.pro-football-reference.com/players/W/')
ulist.append('https://www.pro-football-reference.com/players/Y/')
ulist.append('https://www.pro-football-reference.com/players/Z/')

player_sites = []
for site in ulist:
    page = urlopen(site)
    soup = BeautifulSoup(page, 'html.parser')
    contents = soup.find('div', attrs = {'class': 'section_content'})
    for p in contents.findAll('p'):
        for a in p.findAll('a'):
            player_sites.append(a['href'])


for url in player_sites:
    page_url = 'https://www.pro-football-reference.com' + url
    fh.write(page_url + '\n')

fh.close()
