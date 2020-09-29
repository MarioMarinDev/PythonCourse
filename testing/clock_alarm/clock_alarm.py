import datetime


def is_weekday():
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5
