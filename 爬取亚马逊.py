import requests
url= "https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B01M8L5Z3Y"
try:
    kv = {"user-agent":"Mozilla/5.0"}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding()=r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
