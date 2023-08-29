from datetime import datetime

import pytz


def time_check(in_time):
    try:
        user_tz = pytz.timezone('Europe/Kiev')
        user_time_obj = datetime.strptime(in_time, '%H.%M').time()
        user_datetime = datetime.combine(datetime.today(), user_time_obj)
        utc_time = user_tz.localize(user_datetime).astimezone(pytz.utc).time()
        return utc_time
    except ValueError:
        print('Invalid time format')
        return None


def date_check(in_date):
    try:
        user_tz = pytz.timezone('Europe/Kiev')
        user_date_obj = datetime.strptime(in_date, '%d.%m.%y').date()
        user_datetime = datetime.combine(user_date_obj, datetime.max.time())
        utc_date = user_tz.localize(user_datetime).astimezone(pytz.utc).date()
        return utc_date
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
    now_utc = datetime.now(pytz.utc).replace(second=0, microsecond=0)
    datetime_str = now_utc.strftime("%Y-%m-%d %H:%M")
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
    return datetime_obj


def datetime_to_utc3(utc_datetime):
    try:
        utc_plus_3_tz = pytz.timezone('Europe/Kiev')
        correct_datetime = utc_datetime.astimezone(utc_plus_3_tz)
        formatted_datetime = correct_datetime.strftime('%Y-%m-%d %H:%M')
        return formatted_datetime
    except Exception as e:
        print(f"Error {e}")
        return None
