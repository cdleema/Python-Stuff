from bs4 import BeautifulSoup
import requests, time

#for readnovelfull.com
#Skips chapter titles with special characters and prints TEMP_PLACEHOLDER for manual completion
#occasionally gets wrong chapter title, so requires manual searching and replacing for regex: >\w*\s*\d*\s*<
url = 'https://readnovelfull.com/ancient-strengthening-technique/ast-1946-brilliant-attack-astonishing-forming-feuds.html'

#specific to my computer, to prevent problems with website not accepting crawling
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}

req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

#functions more as minimum number to get, as it stops when it can't find next chapter
num_chapters = 2495 
with open('url_list2.txt','a') as f:

    for x in range(num_chapters):
        try:
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "html.parser")
        except:
            print('error getting next chapter\n' + url)
            break
        temp = soup.find(id='next_chap')
        url_next = 'https://readnovelfull.com'+ temp.get('href')
        ch_title = soup.find(id='chr-content').p.string

        try:
            list_format = '<a href="' + str(url) + '">' + ch_title + '</a>\n'
            list_format = list_format.encode('utf-8','ignore').decode('utf-8')
        
            f.write(list_format)
            time.sleep(2)
        except:
            f.write('TEMP_PLACEHOLDER\n')
        url = url_next
        print(list_format)
    f.close()

