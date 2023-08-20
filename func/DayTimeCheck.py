from datetime import datetime


def time_check(in_time):
    try:
        time_obj = datetime.strptime(in_time, '%H.%M').time()
        return time_obj
    except ValueError:
        print('Invalid time format')
        return None


def date_check(in_date):
    try:
        date_obj = datetime.strptime(in_date, '%d.%m.%y').date()
        return date_obj
    except ValueError:
        print('Invalid date format')
        return None


def valid_datetime(date_obj, time_obj):
    try:
        datetime_obj = datetime.combine(date_obj, time_obj)
        return datetime_obj
    except Exception as e:
        return e


def time_formatting():
    now = datetime.now().replace(second=0, microsecond=0)
    datetime_str = now.strftime("%Y-%m-%d %H:%M")
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
    return datetime_obj
