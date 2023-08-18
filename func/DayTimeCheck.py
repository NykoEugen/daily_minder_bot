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



# set_time = '32.60'
# date = '25.20.23'
# valid_time = time_check(set_time)
# print(valid_time)
# valid_date = date_check(date)
# print(valid_date)
# date_time = valid_datetime(valid_date, valid_time)
# print(date_time)
