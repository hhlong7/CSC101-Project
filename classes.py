class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return "Hours: {}, Minutes: {}".format(self.hour, self.minute)

    def __str__(self):
        return "Hours: {}, Minutes: {}".format(self.hour, self.minute)

