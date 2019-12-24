from random import randint
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
product=open('sort.csv.csv').read().splitlines()
table=[i.split(',') for i in product]

app = Flask(__name__)
# Enable CORS
CORS(app)
def get_index(min_p,max_p):
    i_min = min([i for i in range(1,len(product)) if float(table[i][1])>=min_p])
    i_max = max([j for j in range(1,len(product)) if float(table[j][1])<=max_p])
    return i_min,i_max

def get_product(index): 
    pd_name = table[index][0]
    pd_price = table[index][1]
    pd_img = table[index][2]
    pd_link = table[index][3]
    return pd_name,pd_price,pd_img,pd_link

@app.route("/randomgift", methods=["POST"])
def predict():
    if request.method=="POST":
        input_min = request.json["min"]
        input_max = request.json["max"]
        i_min,i_max=get_index(input_min,input_max)
        index = randint(i_min,i_max)
        pd_name,pd_price,pd_img,pd_link=get_product(index)
    return jsonify(name=pd_name,price=pd_price,image=pd_img,url=pd_link),201