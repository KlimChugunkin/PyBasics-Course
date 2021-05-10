"""
Задание 1
Не используя библиотеки для парсинга, распарсить файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).

"""

import requests


def get_tuple_of_str(string_to_parse: str):
    """
    Splits source string and returns tuple of type (<remote_addr>, <request_type>, <requested_resource>)
    :param string_to_parse: string of one line of the log file
    :return: tuple of type (<remote_addr>, <request_type>, <requested_resource>),if spliting of string_to_parse
    doesn't give enough elements to make output tuple returns tuple (None, None, None)
     """
    split_string = string_to_parse.split(' ')
    if len(split_string) > 6:
        return split_string[0], split_string[5].replace('"', ''), split_string[6]
    else:
        return None, None, None


URL_LOG = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

response = requests.get(URL_LOG)
response_str = requests.get(URL_LOG).text
result_list = [get_tuple_of_str(elem) for elem in response_str.split('\n')]
print(*result_list[:20], *result_list[-20:], sep='\n')
