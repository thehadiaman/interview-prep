from datetime import datetime, timedelta

# get time slots
def get_time_slots():
    # Start and end time
    start_time = datetime.strptime("10:00 AM", "%I:%M %p")
    end_time = datetime.strptime("5:00 PM", "%I:%M %p")
    # Interval
    break_start = datetime.strptime("1:00 PM", "%I:%M %p")
    break_end = datetime.strptime("2:00 PM", "%I:%M %p")
    available_slots = []

    while start_time < end_time:
        if break_start <= start_time < break_end:
            start_time += timedelta(minutes=30)
            continue

        slot = start_time.strftime('%I:%M %p') + ' - ' + (start_time + timedelta(minutes=30)).strftime('%I:%M %p')
        available_slots.append(slot)
        start_time += timedelta(minutes=30)

    return available_slots