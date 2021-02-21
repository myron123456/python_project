import requests
from fake_useragent import UserAgent
from lxml import etree
requests.packages.urllib3.disable_warnings()


def crawel_kuaixun(url):
    user_agent = UserAgent()
    ua = user_agent.random
    headers = {
        "User-Agent": ua,
        "Refer": "https://www.36kr.com/",
    }
    # proxy = {'http': 'http://112.246.233.201:8060'}
    proxy ={"http": "http://5.39.17.96:80"}
    res = requests.get(url=url, headers=headers, verify=False,proxies=proxy,timeout=15)
    # print(res.text)
    return res.text

def parse_news(html):
    result_list = []
    tree = etree.HTML(html)
    for i in range(1,11):
        title_path = "//*[@id=\"app\"]/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div/div[1]/div["+str(i)+"]/div[2]/div/a/text()"
        content_path = "//*[@id=\"app\"]/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div/div[1]/div["+str(i)+"]/div[2]/div/div[2]/span/text()"
        news_titles = tree.xpath(title_path)
        news_contents = tree.xpath(content_path)
        result_list.append(news_titles)
        # print(news_titles)
        # for news_title in news_titles:
        #     # print(news_title)
        #     result_list.append(news_title)
        # return result_list
    return result_list

def main():
    url = "http://36kr.com/newsflashes"
    html = crawel_kuaixun(url)
    newstitle = parse_news(html)
    print(newstitle)
main()