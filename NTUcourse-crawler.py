#抓取PTT NTUcourse版
import urllib.request as req
url = "https://www.ptt.cc/bbs/NTUcourse/index.html"
#建立Request物件
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

#解析原始碼
from bs4 import BeautifulSoup
root = BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)