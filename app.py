from flask import Flask,jsonify,request
from models.cxk import Cxk
from spiders.cxk import start_crawl

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():
    return jsonify({'help':{'/crawl':'crawl cxk videos','/cxk':'get cxk from db (ps: params: page and size,which default value is 0 and 10)'}})


@app.route('/crawl/<int:page>',methods=['GET'])
def crawl(page=5):
    count = start_crawl(page)
    return jsonify({'count':count,'ret':'ok'})


@app.route('/cxk',methods=['GET'])
def cxk():
    page=request.args.get('page',default=0,type=int)
    size=request.args.get('size',default=10,type=int)
    try:
        res,count = Cxk.query_items(page,size)
        return jsonify({'page':page,'size':size,'count':count,'res':res})
    except Exception as e:
        print(e)
        return jsonify({'error':'error happened'})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
