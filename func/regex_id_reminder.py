import re


def regex_id_reminder(message):
    match = re.search(r'Reminder id: (\d+)', message)
    if match:
        reminder_id = match.group(1)
        try:
            int_val = int(reminder_id)
            return int_val
        except TypeError as e:
            print(e)

    else:
        return
