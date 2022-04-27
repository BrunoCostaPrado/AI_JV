import datetime


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        awnser = 'São {} horas e {} minutos'.format(now.hour, now.minute)
        return awnser


now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
