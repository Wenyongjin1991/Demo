# 作 者：wen
# 时 间：2021/11/12 21:43
from urllib.request import urlopen

url = 'http://www.baidu.com'
resp = urlopen(url)

with open('mybaidu.html',mode = 'w')as f:
    f.write(resp.read().decode('utf-8'))
print('over!')