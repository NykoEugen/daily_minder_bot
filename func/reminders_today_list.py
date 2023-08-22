from func.DayTimeCheck import time_formatting
from handlers.db_handler import get_reminder_list, get_reminders_to_show


def schedule_alert():
    schedule_lst = []
    datetime_obj = time_formatting()
    reminders = get_reminders_to_show(datetime_obj)
    if reminders is not None:
        for item in reminders:
            item_time = item[2]
            if str(datetime_obj) >= item_time:
                data = {
                    "id": item[0],
                    "description": item[1],
                    "event_id": item[3],
                    "time": item[2],
                    "user_id": item[4],
                }
                schedule_lst.append(data)
        return schedule_lst


def reminder_list():
    reminders_lst = []
    datetime_obj = time_formatting()
    lst = get_reminder_list(datetime_obj)

    for item in lst:
        data = {
            "description": item[1],
            "time": item[2],
        }
        reminders_lst.append(data)

    return reminders_lst
