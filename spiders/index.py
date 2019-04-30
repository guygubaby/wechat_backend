import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
# from fake_useragent import UserAgent


class BiliBiliSpider:
    # ua=UserAgent(use_cache_server=False, verify_ssl=False)
    cxk_db=MongoClient(host='service.db',port=27017).my_db.cxk
    url_template='https://search.bilibili.com/all?keyword={}&page={}'
    headers={
        # 'User-Agent':ua.random,
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        'Referer':'https://www.bilibili.com/',
    }

    session=requests.session()
    session.headers=headers

    res=[]

    def __init__(self,search_text='蔡徐坤',end_page=2):
        self.urls=[self.url_template.format(search_text,i) for i in range(1,end_page+1)]

    def delete_previous(self):
        self.cxk_db.delete_many({})

    def get_content(self):
        # self.delete_previous() # 删除之前的防止重复数据
        for url in self.urls:
            try:
                res=self.session.get(url).text
                soup=BeautifulSoup(res,'html.parser')
                videos=soup.find_all(class_='video matrix')
                for item in videos:
                    try:
                        title =item.find('a',class_='title')['title']
                        # cover = item.find('div',class_='lazy-img')
                        # print(cover)
                        time =list(item.find('span',class_='so-icon time').strings)[0].strip()
                        watch_count =list(item.find('span',class_='so-icon watch-num').strings)[0].strip()
                        last_time = item.find('span',class_='so-imgTag_rb').string
                        self.res.append({
                            'title':title,
                            'time':time,
                            'watch_count':watch_count,
                            'last_time':last_time,
                        })
                    except Exception as e:
                        print(e)
                        continue

            except Exception as e:
                print(url,e)
                continue
            print('saving page of {} data into mongo ... '.format(url.split('page=')[1]))
            if len(self.res)==0:
                print('get no content ...')
                return
            self.cxk_db.insert_many(self.res)
            self.res=[]

    def get_total_count(self):
        count = self.cxk_db.find().count()
        return count


def start_crawl(text='蔡徐坤',page=5):
    cxk=BiliBiliSpider(search_text=text,end_page=page)
    cxk.get_content()
    return cxk.get_total_count()


if __name__ == '__main__':
    start_crawl('guygubaby',2)