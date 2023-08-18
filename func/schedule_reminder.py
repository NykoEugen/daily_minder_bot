from datetime import datetime


class RemindersCheck:
    def __init__(self, reminders):
        self.reminders = reminders
        self.schedule_now_lst = []
        self.alerts = []

    def time_formating(self):
        now = datetime.now().replace(second=0, microsecond=0)
        datetime_str = now.strftime("%Y-%m-%d %H:%M")
        datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        return datetime_obj

    def schedule_alert(self):
        self.schedule_now_lst = []
        datetime_obj = self.time_formating()
        for item in self.reminders:
            item_time = item[2]
            if str(datetime_obj) == item_time:
                data = {
                    "id": item[0],
                    "description": item[1],
                    "time": item[2],
                    "user_id": item[4],
                }
                self.schedule_now_lst.append(data)
        return self.schedule_now_lst



# now = datetime.now().replace(second=0, microsecond=0)
# datetime_str = now.strftime("%Y-%m-%d %H:%M")
# datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
# reminders = get_reminders_to_show(datetime_obj)
# scheduler = RemindersCheck(reminders)
# print(f"Daily {scheduler.schedule_daily()}")
# print(f"Minutes {scheduler.schedule_minutes()}")
