import json
import codecs
import pandas as pd
df = pd.read_csv('products.csv')
re=df.sort_values('price')
price = re['price']
name = re['name']
img=re['img']
link=re['link']
with codecs.open(f'product.json', 'w','utf-8') as outfile:  
    outfile.write('{"product":[\n')

for i in range(len(re.index)):
    detail = {}
    detail['name'] = name[i] 
    detail['price'] = price[i]
    detail['img'] = img[i]
    detail['url'] = link[i]

    with codecs.open(f'product.json', 'a','utf-8') as outfile:  
        json.dump(detail, outfile,ensure_ascii=False)
        if i+1 < len(re.index):
            outfile.write(',\n')

with codecs.open(f'product.json', 'a','utf-8') as outfile:  
    outfile.write(']\n}')