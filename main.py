# for checking conditions

from baseSkills import listen
import skills as skill


time = ["saat","kaç","saat kaç","kaç saat","zaman"]
date = ["bugün ayın kaçı","ayın","kaçı","bugün günlerden ne","günler","günlerden","bu gün ayın"]
weather = ["derece","hava","kaç","hava kaç","sıcaklık kaç","sıcaklık","hava durumu"]
news = ["haberler","haberleri","haber","gündem","gazete","oku","haberleri oku"]
wikiSearch = ["nedir","kimdir","ne","nasıl"]
playYouTube = ["çal","oynat","aç"]
close = ["sistemi kapat","uyu","kendini kapat"]

def mergen(data):
    if data in time:
        skill.clock()
    if data in date:
        skill.date()
    if data in weather:
        skill.weather()
    if data in news:
        skill.news()
    if data in wikiSearch:
        skill.search(data)

while True:
    datax = listen()
    if datax in close:
        skill.close()
        break
    else:
        mergen(datax)
