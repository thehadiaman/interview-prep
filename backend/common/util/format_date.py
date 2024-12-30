from datetime import datetime, timedelta

# Get formatted date
def get_formatted_date(date):
    try:
        return datetime.strptime(date, '%Y-%m-%d').date(), True
    except Exception as e:
        return e, False