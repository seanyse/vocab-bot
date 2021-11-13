import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0. 8' ,
    'Accept-Language': 'en-US, en;q=0.5',
    'DNT': '1',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'Accept-Encoding':'identity',
}

try:
    print(i)
except:
    i = 0

with open('proxies.txt') as f:
    proxy_list = f.readlines()

if i > len(proxy_list):
    i = 0

# split proxy into user pass ip port
proxy = proxy_list[i].split(":")

print(proxy[0])
print(proxy[1])
print(proxy[2])
print(proxy[3])

user = proxy[2]
password = proxy[3]
ip = proxy[0]
port = proxy[1]

proxies = {
    "http" : f"http://{user}:{password}@{ip}:{port}",
    "https": f"https://{user}:{password}@{ip}:{port}"
}
r = requests.Session()
r.proxies.update(proxies)
result = r.get("https://vocabulary.com", headers=headers,)

