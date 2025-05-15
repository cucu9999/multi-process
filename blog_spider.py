import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50)
]
def craw(url):
    r = requests.get(url)
    # print(url, len(r.text))
    return r.text



def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_ = "post-item-title")
    return [ (link.get("href"), link.get_text()) for link in links]


if __name__ == "__main__":
    craw(urls[0])
    
    # for result in parse(craw(urls[1])):
    #     print(result)