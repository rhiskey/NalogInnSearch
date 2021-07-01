import requests
import json
import logging
from sys import exit


def get_valid_inns(inn_list, page):
    url = "https://rmsp.nalog.ru/search-proc.json"

    # TODO: change page and pageSize?
    payload = {'mode': 'inn-list',
               'page': page,
               'innList': inn_list,
               'pageSize': '100',
               'sortField': 'NAME_EX',
               'sort': 'ASC'}
    files = [

    ]
    headers = {
        'Cookie': '_ym_uid=1605688049584689471; _ym_d=1605688049; JSESSIONID=397D9E4821DCFACDF98BA13237FBFB0F; '
                  '_ym_visorc=b; _ym_isad=2',
        'Origin': 'https://rmsp.nalog.ru',
        'Referer': 'https://rmsp.nalog.ru/search.html?mode=inn-list',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    json_resp = ''
    try:
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        rsp = response.text.encode('utf8')
        json_resp = json.loads(rsp)
    except Exception as e:
        # logging.warning('Request error')
        # logging.debug('Request error')
        logging.exception("Request exception")
        exit(5)

    return json_resp
