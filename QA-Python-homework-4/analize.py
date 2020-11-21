#!/usr/bin/env python
import argparse
import re
import json
from os.path import isfile


def a(lines):
    return len(lines)


def m(requests):
    methods = ['OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT']
    stats = {}
    for dict_ in requests:
        method = dict_['method']
        if not method in methods:
            continue

        if not method in stats.keys():
            stats[method] = 0

        stats[method] += 1

    ret = []
    for key in stats:
        dict_ = {}
        dict_['method'] = key
        dict_['count'] = stats[key]
        ret.append(dict_)

    return ret


def b(requests):
    requests.sort(key=lambda x: x['url'])
    group = []
    ans = []
    f = True
    tmp = {}
    for elm in requests:
        if f:
            tmp['url'] = elm['url']
            f = False
        if elm['url'] != tmp['url']:
            group.sort(key=lambda x: x['len'], reverse=True)
            ans.append(group[0])
            ans[-1]['count'] = len(group)
            group.clear()
            group.append(elm)
            tmp['url'] = elm['url']
        else:
            group.append(elm)

    group.sort(key=lambda x: x['len'], reverse=True)
    ans.append(group[0])
    ans[-1]['count'] = len(group)
    ans.sort(key=lambda x: x['len'], reverse=True)
    ans = ans[:10]

    ret = []
    for request in ans:
        dict_ = {}
        dict_['url'] = request['url']
        dict_['code'] = request['code']
        dict_['count'] = request['count']
        ret.append(dict_)

    return ret


def c(requests):
    requests = list(filter(lambda x: x['code'] in range(400, 500), requests))
    requests.sort(key=lambda x: x['url'])

    group = []
    ans = []
    f = True
    tmp = {}
    for elm in requests:
        if f:
            tmp['url'] = elm['url']
            f = False
        if elm['url'] != tmp['url']:
            ans.append(group[0])
            ans[-1]['count'] = len(group)
            group.clear()
            group.append(elm)
            tmp['url'] = elm['url']
        else:
            group.append(elm)

    ans.append(group[0])
    ans[-1]['count'] = len(group)
    ans.sort(key=lambda x: x['count'], reverse=True)
    ans = ans[:10]

    ret = []
    for request in ans:
        dict_ = {}
        dict_['url'] = request['url']
        dict_['code'] = request['code']
        dict_['ip'] = request['ip']
        ret.append(dict_)

    return ret


def s(requests):
    requests = list(filter(lambda x: x['code'] in range(500, 600), requests))
    requests.sort(key=lambda x: x['url'])
    group = []
    ans = []
    f = True
    tmp = {}
    for elm in requests:
        if f:
            tmp['url'] = elm['url']
            f = False
        if elm['url'] != tmp['url']:
            group.sort(key=lambda x: x['len'], reverse=True)
            ans.append(group[0])
            group.clear()
            group.append(elm)
            tmp['url'] = elm['url']
        else:
            group.append(elm)

    group.sort(key=lambda x: x['len'], reverse=True)
    ans.append(group[0])
    ans.sort(key=lambda x: x['len'], reverse=True)
    ans = ans[:10]

    ret = []
    for request in ans:
        dict_ = {}
        dict_['url'] = request['url']
        dict_['code'] = request['code']
        dict_['ip'] = request['ip']
        ret.append(dict_)

    return ret


def to_requests(lines):
    requests = []
    for line in lines:
        dict_ = {}
        splited = re.split('[ "]', line)
        dict_['ip'] = splited[0]
        dict_['method'] = splited[6]
        dict_['url'] = splited[7]
        dict_['code'] = int(splited[10])
        if splited[11] == '-':
            dict_['len'] = 0
        else:
            dict_['len'] = int(splited[11])
        requests.append(dict_)

    return requests


def main():
    outfile = 'analyzed'

    parser = argparse.ArgumentParser(usage='analyze.py  [--json]  a | m | b | c | s  <FILE>',
                                     epilog=f'Имя выходного файла - {outfile}.')
    parser.add_argument('task', action='store', help='см. в README.md', choices=['a', 'm', 'b', 'c', 's'])
    parser.add_argument('file', action='store', metavar='FILE', help='входной файл')
    parser.add_argument('--json', action='store_true', help='записать вывод в формате JSON')

    args = parser.parse_args()

    if isfile(outfile):
        print(f"File '{outfile}' exists, overwrite? (yes/NO): ", end='')
        in_ = input()
        if not (in_ == 'y' or in_ == 'yes'):
            raise FileExistsError()

    with open(args.file) as f:
        lines = f.read().split('\n')

    method = '^(OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT)$'
    for line in lines:
        if not re.search(method, line):
            del line

    if lines[-1] == '':
        del lines[-1]

    task = args.task
    if task == 'a':
        res = a(lines)
    else:
        requests = to_requests(lines)
        if task == 'm':
            res = m(requests)
        elif task == 'b':
            res = b(requests)
        elif task == 'c':
            res = c(requests)
        elif task == 's':
            res = s(requests)
        else:
            raise Exception()

    with open(outfile, 'w') as f:
        if args.json:
            f.write(json.dumps(res))
        else:
            if isinstance(res, list):
                for line in res:
                    for key in line:
                        f.write(str(line[key]) + ' ')
                    f.write('\n')
            elif isinstance(res, int):
                f.write(str(res))
            else:
                raise Exception()


if __name__ == '__main__':
    main()
