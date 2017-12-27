# _*_ coding:utf-8 _*_

import Scripts.TestCases.Concurrency.JoinUrl
import requests
import multiprocessing as m

processes = 100


def concurrency():
    url = ""
    # urllib.request.urlopen(url)
    requests.get(url)


if __name__ == '__main__':
    pool = m.Pool(processes)
    for i in range(processes):
        pool.apply_async(func=concurrency)
    pool.close()
    pool.join()