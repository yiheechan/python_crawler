from bs4 import BeautifulSoup
from datetime import datetime
import os
import requests

os.makedirs('docs', exist_ok=True)
URL = "https://m.etnews.com/news/hot_content_list.html"
#URL = "https://www.etnews.com/news/hot_content_list.html"

# 오늘의 인기기사 RSS 피드 URL (방화벽 차단 확률 매우 낮음)
#URL = "http://rss.etnews.com/Section903.xml"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

res = requests.get(URL, headers=headers, timeout=10)
soup = BeautifulSoup(res.text, 'html.parser')

section = soup.select_one("section.textthumb")
top = section.select('ul li strong a')[:10]

now = datetime.now().strftime('%Y-%m-%d')
with open('docs/index.md','w',encoding='utf-8') as f:
	f.write(f"# {now} 많이본뉴스\n\n")
	for i, a in enumerate(top, 1):
		title = a.text.strip()
		link = "https://m.etnews.com"+a['href']
		f.write(f"{i}. [{title}]({link})\n")