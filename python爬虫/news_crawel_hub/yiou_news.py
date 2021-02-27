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
for i  in range(1,11):
    content = result['data']['briefing_list'][i]['content']
    title = result['data']['briefing_list'][i]['title']
    print(content)
    print(title)
