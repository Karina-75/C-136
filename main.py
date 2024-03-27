from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({
        'data': data, 
        'message': 'success'
    })

@app.route('/planet')
def planet():
    name = request.args.get('name')
    planet_data = next(item for item in data if item['name']==name)
    #planet_data = []
    '''for item in data:
        if item['name']==name:
            planet_data.append(item)'''
    return({
        'data': planet_data,
        'message': 'success'
    })


if __name__=='__main__':
    app.run()

