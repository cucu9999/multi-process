import requests


urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 101)
]
def craw(url):
    r = requests.get(url)
    # print(url, len(r.text))

craw(urls[0])