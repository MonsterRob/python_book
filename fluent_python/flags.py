# encoding=utf-8
import os
import time
import sys
import requests
from concurrent.futures import ThreadPoolExecutor

POP20_CC = ("CN IN US ID BR PK NG BD RU JP MX "
            "PH VN ET EG DE IR TR CD FR").split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = "downloads/"
MAX_WORKERS = 20


def save_flags(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as f:
        f.write(img)


def get_flag(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    return requests.get(url).content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in cc_list:
        img = get_flag(cc)
        show(cc)
        save_flags(img, cc.lower() + '.gif')
    return len(cc_list)


def download_many2(cc_list):
    workers = min(len(cc_list), MAX_WORKERS)
    with ThreadPoolExecutor(workers) as excuter:
        res = excuter.map(download_one, sorted(cc_list))
    return len(list(res))


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    e = time.time() - t0
    msg = '\n {} flags downloaded in {:.2f}s'
    print(msg.format(count, e))


def download_one(cc):
    img = get_flag(cc)
    show(cc)
    save_flags(img, cc.lower() + '.gif')
    return cc


if __name__ == '__main__':
    main(download_many2)
