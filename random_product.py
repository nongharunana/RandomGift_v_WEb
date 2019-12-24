import pandas as pd
from random import randint
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
df = pd.read_json('product.json')
app = Flask(__name__)
# Enable CORS
CORS(app)

def get_product(index): 
    # print(index)
    pd_name = df['product'][index]['name']
    pd_price = df['product'][index]['price']
    pd_img = df['product'][index]['img']
    pd_link = df['product'][index]['url']
    return pd_name,pd_price,pd_img,pd_link

@app.route("/randomgift", methods=["POST"])
def predict():
    if request.method=="POST":
        input_min = request.json["min"]
        input_max = request.json["max"]
        i_min = min([i for i in range(len(df['product'].index)) if float(df['product'][i]['price'])>=input_min])
        i_max = max([j for j in range(len(df['product'].index)) if float(df['product'][j]['price'])<=input_max])
        index = randint(i_min,i_max)
        pd_name,pd_price,pd_img,pd_link=get_product(index)
    return jsonify(name=pd_name,price=pd_price,image=pd_img,url=pd_link),201