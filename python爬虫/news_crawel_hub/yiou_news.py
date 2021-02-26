import requests
import json
from fake_useragent import UserAgent

requests.packages.urllib3.disable_warnings()

user_agent = UserAgent()
ua = user_agent.random
headers = {
    "user_agent": ua
}
url = "https://api.iyiou.com/api/list/briefing?page=1"
proxy = {'http': 'http://148.251.153.6:1080'}
res = requests.get(url=url, headers=headers, verify=False,
                   allow_redirects=False, proxies=proxy, timeout=15)
result = json.loads(res.text)

content = result['data']['briefing_list'][0]['content']
title = result['data']['briefing_list'][0]['title']
print(content)
print(title)
