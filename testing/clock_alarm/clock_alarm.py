import datetime


def is_weekday():
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5


if __name__ == '__main__':
    print(is_weekday())
