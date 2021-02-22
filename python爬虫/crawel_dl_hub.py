import requests
from fake_useragent import UserAgent
import time
import random
import re

requests.packages.urllib3.disable_warnings()
user_agent = UserAgent()
ua = user_agent.random
# print(ua.random)

class CrawelDlHub():
    def crawel_xiladl(self):
        # xila free proxy IP,页面1的url特殊
        for i in range(1, 21):
            try:
                if i == 1:
                    url = "http://www.xiladaili.com/gaoni/"
                else:
                    url = "http://www.xiladaili.com/gaoni/{}/".format(str(i))
                time.sleep(3.6)
                headers = {
                    "User-Agent": ua,
                    'Connection': 'close'
                }
                # proxy = {"HTTP": "52.149.152.236:80"}
                res = requests.get(url, headers=headers, verify=False,
                                   allow_redirects=False, timeout=15)
                if res.status_code == 200:
                    html = res.text
                if html is not None:
                    pattern = "<tr>[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>(.*?)</td>"
                    items = re.findall(pattern, html)
                    for item in items:
                        item = list(item)
                        if item[1] == "HTTP代理":
                            item[1] = "http"
                        elif item[1] == "HTTPS代理" or item[1] == "HTTP,HTTPS代理":
                            item[1] = "https"
                        yield {
                            # 'type': item[1],
                            # 'target': item[0]
                            "{}".format(item[1]): "{}".format(str(item[1]) + "://" + str(item[0]))
                        }

                    for content in parse_one_page(html):
                        # print(content)
                        # write_to_txt(content)
                        verify(content)
                else:
                    print("访问目标网站失败")
            except Exception as e:
                print(e)