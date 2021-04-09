MINUTE = 60
HOUR = 3600
DAY = 86400


def get_day(duration):
    return duration // DAY


def get_hour(duration):
    return duration%DAY // HOUR


def get_min(duration):
    return duration%HOUR // MINUTE


def get_sec(duration):
    return duration % MINUTE


def get_time(duration):
    if duration // MINUTE == 0:
        return f'{duration} сек'
    elif duration // HOUR == 0:
        return f'{get_min(duration)} мин {get_sec(duration)} сек'
    elif duration // DAY == 0:
        return f'{get_hour(duration)} час {get_min(duration)} мин {get_sec(duration)} сек'
    else:
        return f'{get_day(duration)} день {get_hour(duration)} час {get_min(duration)} мин {get_sec(duration)} сек'


test = [48, 60, 1312, 3600, 8954, 86400, 95133]
for duration in test:
    print(get_time(duration))
