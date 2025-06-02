class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return "Hours: {}, Minutes: {}, Seconds: {}".format(self.hour, self.minute, self.second)

    def __str__(self):
        return "Hours: {}, Minutes: {}, Seconds: {}".format(self.hour, self.minute, self.second)

