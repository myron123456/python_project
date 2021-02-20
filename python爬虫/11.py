import requests
import re
import time

requests.packages.urllib3.disable_warnings()


def crawel_one_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    }
    res = requests.get(url, headers=headers, verify=False,
                       allow_redirects=False, timeout=15)
    if res.status_code == 200:
        return res.text
    return None


def parse_one_page(html):
    cve_list = []
    pattern = "(CVE-\d+-\d+)"
    items = re.findall(pattern, html)
    for item in items:
        cve_list.append(item)
    return cve_list


def write_to_txt(pocs_list):
    with open('cve.txt', 'a', encoding='utf-8') as f:
        for item in pocs_list:
            f.write(item + '\n')


def main():
    poc_list = []
    for i in range(1, 101):
        url = "https://www.seebug.org/vuldb/vulnerabilities?has_poc=true&page={}".format(
            i)
        time.sleep(0.5)
        html = crawel_one_page(url)
        pocs = parse_one_page(html)
        print(pocs)
        poc_list.extend(pocs)
    # print(poc_list)
    # print(len(poc_list))
    poc_list = set(poc_list)
    write_to_txt(poc_list)
    print(poc_list)
    print(len(poc_list))
    # if "CVE-2020-17518" in poc_list:
    #     print('true')


main()
