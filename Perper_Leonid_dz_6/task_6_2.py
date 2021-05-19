"""
Не используя библиотеки для парсинга, распарсить файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
Найти IP адрес спамера и количество отправленных им запросов.  код должен работать даже с файлами, размер которых
превышает объем ОЗУ компьютера.

"""

import requests

URL_LOG = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

ip_dict = {}    # словарь { key = ip: val = количество запросов }
with requests.get(URL_LOG, stream=True) as resp:
    for raw_line in resp.iter_lines():
        curr_ip = raw_line.decode('utf-8').split(' ')[0]
        if ip_dict.get(curr_ip):
            ip_dict[curr_ip] += 1
        else:
            ip_dict.update({curr_ip: 1})
ip_sorted = sorted(ip_dict.items(), key=lambda item: item[1], reverse=True)
print(f'IP c наибольшим количеством запросов: {ip_sorted[0][0]}',
      f'Количество запросов: {ip_sorted[0][1]}', sep='\n')
