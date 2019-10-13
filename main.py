import requests
from bs4 import BeautifulSoup
import pprint
res=requests.get("https://news.ycombinator.com/news")
res2=requests.get("https://news.ycombinator.com/news?p=2")
soup=BeautifulSoup(res.text,'html.parser')
soup2=BeautifulSoup(res2.text,'html.parser')
link=soup.select(".storylink")
link2=soup2.select("storylink")
score=soup.select(".score")
score2=soup2.select(".score")
mega_link=link+link2
mega_score=score+score2
def create_custom_hacker_news(mega_link,mega_score):
    hn=[]
    for i , item in enumerate(mega_link):
        title=mega_link[i].getText()
        href=mega_link[i].get("href",None)
        votes=int(mega_score[i].getText().replace("points",""))
        if votes>99:
            hn.append({"title":title,"link":href,"votes":votes})
    hn=sorted(hn,key = lambda i:i["votes"],reverse=True)
    return hn

pprint.pprint(create_custom_hacker_news(mega_link,mega_score))
