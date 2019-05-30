#coding:utf-8
import json
numbers = [3,4,4,1,2,8,11]
filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj) #使用dump来存储数字列表