from func.DayTimeCheck import time_formatting, datetime_to_utc3
from handlers.db_handler import get_reminder_list, get_reminders_to_show


def schedule_alert():
    schedule_lst = []
    datetime_obj = time_formatting()
    reminders = get_reminders_to_show(datetime_obj)
    print(reminders)
    # (3, 'cghjfghj', datetime.datetime(2023, 8, 28, 21, 35), False, 385833312)
    if reminders is not None:
        for item in reminders:
            item_time = item[2]
            if datetime_obj >= item_time:
                date = datetime_to_utc3(item[2])
                data = {
                    "id": item[0],
                    "description": item[1],
                    "is_done": item[3],
                    "time": date,
                    "user_id": item[4],
                }
                schedule_lst.append(data)
        return schedule_lst


def reminder_list(user_pk):
    reminders_lst = []
    datetime_obj = time_formatting()
    lst = get_reminder_list(datetime_obj, user_pk)
    print(lst)
    # [('tset description', datetime.datetime(2023, 8, 29, 0, 20), False, 385833312)]
    for item in lst:
        date = datetime_to_utc3(item[2])
        data = {
            "reminder_id": item[0],
            "description": item[1],
            "time": date,
        }
        reminders_lst.append(data)

    return reminders_lst


def alert_lst():
    print('cron works')
    data = schedule_alert()
    if data:
        return data
    else:
        print("event doesn't exist")
