from urllib.request import urlopen
from bs4 import BeautifulSoup

player_dic = {}
with open('urls2.txt') as f:
    for elem in f:
        page1 = urlopen(elem)
        soup1 = BeautifulSoup(page1, 'html.parser')
        header = soup1.find('h1', attrs = {'itemprop': 'name'})
        name = header.text.strip()
        count = 0
        for tr in soup1.findAll('tr'):
            th = tr.th
            s = th.text
            if '*' in s:
                count += 1
        player_dic[name] = count
