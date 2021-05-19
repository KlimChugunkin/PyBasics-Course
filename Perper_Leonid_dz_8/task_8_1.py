"""
Задание 1
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.

"""

import re


def email_parse(email_address: str):
    """
    Returns dict of user and domain names from e-mail address string. Raises ValueError exception if <email_address>
    doesn't match pattern <any symbols except ' ' or '@'>@<any symbols except ' ' ,'@','.'>.<lowercase letters a-z>
    :param email_address:
    :return: dict {'user_name': <user_name>, 'domain': <domain>}
    """

    if not re.match(r'[^@\s]+@[^@\s\.]+\.[a-z]+$', email_address):
        raise ValueError('некорректный адрес')
    return {'user_name': re.match(r'\S+(?=@)', email_address)[0],
            'domain': re.search(r'(?<=@)[^@\s\.]+\.[a-z]+$', email_address)[0]}


print(email_parse('vasya_1989@gmail.com'))
