from pymongo import MongoClient


class Cxk:
    db = MongoClient(host='service.db', port=27017).my_db.cxk
    res = []

    def __init__(self,title,time,watch_count,last_time):
        self.title=title
        self.time=time
        self.watch_count=watch_count
        self.last_time=last_time

    @classmethod
    def query_items(self,page=0,size=10):
        self.res=[]
        count=self.db.find().count()
        res=self.db.find().limit(size).skip(page*size)
        for item in res:
            item.pop('_id')
            self.res.append(item)
        return self.res,count