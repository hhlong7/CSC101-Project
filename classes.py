class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return "Hours: {}, Minutes: {}, Seconds: {}".format(self.hour, self.minute, self.second)

    def __str__(self):
        return "Hours: {}, Minutes: {}, Seconds: {}".format(self.hour, self.minute, self.second)

    def __eq__(self, other):
        return (type(self) == type(other)) or self.hour == other.hour and self.minute == other.minute and self.second == other.second


class