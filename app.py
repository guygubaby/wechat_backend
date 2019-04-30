from flask import Flask,jsonify,request
from models.bilibili_item import BiliBiliVideoItem
from spiders.index import start_crawl

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def help():
    return jsonify({'help':
                        {'/crawl':'crawl videos',
                         '/get':'get video from db'}
                    })


@app.route('/crawl',methods=['GET'])
def crawl():
    text = request.args.get('name',default='蔡徐坤',type=str)
    page = request.args.get('page',default=5,type=int)
    count = start_crawl(text,page)
    return jsonify({'count':count,'ret':'ok'})


@app.route('/get',methods=['GET'])
def video():
    page=request.args.get('page',default=0,type=int)
    size=request.args.get('size',default=10,type=int)
    try:
        res,count = BiliBiliVideoItem.query_items(page,size)
        return jsonify({'page':page,'size':size,'count':count,'res':res})
    except Exception as e:
        print(e)
        return jsonify({'error':'error happened'})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
