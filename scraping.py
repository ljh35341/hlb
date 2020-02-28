import requests
from bs4 import BeautifulSoup


def TaskA():

    new_info = []

    # 구글뉴스
    new_info.append('----------뉴스----------')
    url = 'https://www.google.com/search?sxsrf=ALeKk03UZLKH4Yb88EU6d4Rq8bUi9stgTQ:1582601425545&source=lnms&tbm=nws&sa=X&ved=2ahUKEwinoKne4evnAhVDMN4KHcAnBroQ_AUoAnoECBgQBA&biw=958&bih=959'
    News_Corp = {'q': '에이치엘비'}
    r = requests.get(url, params=News_Corp)
    soup = BeautifulSoup(r.content, 'lxml')
    titles = soup.find_all('div', class_="BNeawe vvjwJb AP7Wnd")
    for title in titles:
        new_info.append(title.text)

    # 공시
    new_info.append('----------공시----------')
    url = 'http://dart.fss.or.kr/api/companyRSS.xml'
    Dart_Corp = {'crpCd': '00199252'}
    r = requests.get(url, params=Dart_Corp)
    soup = BeautifulSoup(r.content, 'lxml')
    titles = soup.find_all('title')
    for title in titles[1:]:
        new_info.append(title.text)
    # links = soup.find_all('guid')
    # for link in links:
    #    print(link.text)

    return new_info
    #for i in new_info:
    #   print(i)