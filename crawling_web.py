'''
爬取网页
http://st.kanxshuo.com/book-69397-37.html
'''

# 域名
base_url = "http://st.kanxshuo.com/"

import re
import requests
from bs4 import BeautifulSoup

start_url = "http://st.kanxshuo.com/book-69397-1.html"
file = "我的奋斗.txt"
with open(file,'a') as file_object:
    while None != start_url:
        r = requests.get(start_url)
        soup = BeautifulSoup(r.text, 'lxml')
        content = soup.find(class_='bookContent')
        print(content.get_text())
        file_object.write(content.get_text())
        page_content = soup.find(class_="bpages")
        link_content = page_content.find_all_next("a")
        next_page_url = link_content[1].get('href')
        if(None == next_page_url):
            break
        start_url = base_url + next_page_url
