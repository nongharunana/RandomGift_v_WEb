import pandas as pd
import os
# f = open('products.csv').read().splitlines()
# os.remove('results.csv')
# f2 = open('products2.csv').read().splitlines()
# print('remove it successful')
# a = open('results.csv','a')
# # print(len(f))
# for i in range(15602):
#         a.write(f'{f[i]}\n')
#         # a.write('\n')
# # a.write(f[15602])
# for i in f2:
#     a.write(f'{i}\n')
# a.close()
df = pd.read_csv('results.csv')
df.name.unique()
# print(df)

re=df.sort_values('price')
# print(re)
export_csv = re.to_csv (r'sort.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
