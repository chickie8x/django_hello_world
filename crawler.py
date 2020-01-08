import random
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled.settings")
django.setup()
from news.models import Article, Category

init_depth = 1
depth = 10
url1 = 'http://genk.vn/ajax-home/page-'
url2 = '/20191113154319894__20191127162422723__20191129112104066__20191128123141223__20191128152623316.chn'
list_article = []


def web_spider(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    for link in soup.find_all('div', class_='knswli-left fl'):
        article_feature_img = link.img.get('src')
        article_url = 'http://genk.vn' + link.a.get('href')
        article = get_content(article_url, article_feature_img)
        list_article.append(article)
    return list_article


def get_content(url, url_img):
    dict_content = {}
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    content = soup.find_all('div', id='ContentDetail')
    images = soup.find_all('img', id=True)
    title = soup.find('h1', class_='kbwc-title clearfix')
    article_description = soup.find('h2', class_='knc-sapo')
    try:
        article_datetime = soup.select_one('span[title*=T]').attrs.__getitem__('title').split('T')[0].replace('-', '/')
        pub_date = datetime.strptime(article_datetime, '%Y/%m/%d').date()
    except:
        pass

    if not title or not article_description:
        print('no objects found')
    else:
        for detail in content:
            detail
        for img in images:
            item_id = random.randint(5, 1000)
            if url_img:
                dict_content = dict(id=item_id, article_feature_img=url_img, article_title=title.get_text(),
                                    article_desc=article_description.get_text(), article_content=str(detail),
                                    article_category=random.randint(1, 4), published_date=pub_date)
            else:
                print('no url img')
    return dict_content


for i in range(init_depth, depth):
    test = web_spider(url1 + str(i) + url2)

a = filter(None, test)
obj = [Article(article_feature_img=item['article_feature_img'], article_title=item['article_title'],
               article_desc=item['article_desc'], article_content=item['article_content'],
               article_category=Category.objects.get(id=item['article_category']),
               published_date=item['published_date']) for item in a]
Article.objects.bulk_create(obj)
