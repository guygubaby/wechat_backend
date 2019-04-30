### api

1. `/crawl` 

    func
    * to get the latest video from bilibili 
    
    params
    * name default 蔡徐坤
    * page default 5
    
    eg
    * `/crawl?page=5&name=蔡徐坤` [crawl5Page](http://guygubaby.top:8888/crawl?page=5&name=蔡徐坤)

2. `/get`

    func
    * to get data from mongodb,
    
    params
    * page default 0
    * size default 10
    
    eg
    * `/get?page=0&size=10`  [get50Video](http://guygubaby.top:8888/get?page=0&size=50)
    
### deploy
```
git clone https://github.com/guygubaby/wechat_backend.git
cd  wechat_backend
docker-compose up -d
``` 
