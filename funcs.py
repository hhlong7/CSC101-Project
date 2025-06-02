from classes import *
from data import *

def timeadd(t1: Time, t2: Time)-> Time:
    totalsecond = t1.second + t2.second
    totalmin = t1.minute + t2.minute
    totalhour = t1.hour + t2.hour
    secondtomin = 0
    if totalsecond >= 60:
        secondtomin = totalsecond // 60
        totalsecond = totalsecond % 60
    totalmin += secondtomin
    mintohour = 0
    if totalmin >= 60:
        mintohour = totalmin // 60
        totalmin = totalmin % 60
    totalhour += mintohour
    return Time(totalhour, totalmin, totalsecond)

def mile_to_km(n1):
    return n1 * 1.609

def get_distance(start, end):
    try:
        location_key = (start, end)
        d = routes.get(location_key)
        if d != None:
            return d[0]
        else:
            raise Exception("Location is not within the database.")
    except Exception as e:
        print(e)

def get_time(start, end):
    try:
        location_key = (start, end)
        d = routes.get(location_key)
        if d != None:
            return d[1]
        else:
            raise Exception("Try another location.")
    except Exception as e:
        print(e)

def third_location(start, end, stop):
    first = (start, stop)
    second = (stop, end)
    total_distance = routes.get(first)[0] + routes.get(second)[0]
    return total_distance


