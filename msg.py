import requests
import json
SCKEY = "SCU97223Tb71ed152160cd8b2841a256675dc8ba35eb6d3db532c1"+".send?"
root = "https://sc.ftqq.com/"+SCKEY+"text="
try:
    desp = open("weibo/处处吻--/7264541047.json","r",encoding='utf-8')
    k = desp.read()
    desp.close()
    dic = json.loads(k)
    text = dic["weibo"][0]["text"]
    url = root + text
    requests.get(url)
except:
    requests.get(root+"用户名已更改，请修改文件路径")
