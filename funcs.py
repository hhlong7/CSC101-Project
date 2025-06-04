from classes import *
from data import *

def timeadd(t1: Time, t2: Time)-> Time:
    totalmin = t1.minute + t2.minute
    totalhour = t1.hour + t2.hour
    secondtomin = 0
    mintohour = 0
    if totalmin >= 60:
        mintohour = totalmin // 60
        totalmin = totalmin % 60
    totalhour += mintohour
    return Time(totalhour, totalmin)

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

def one_stop(start, stop, end):
    first = (start, stop)
    second = (stop, end)
    total_distance = routes.get(first)[0] + routes.get(second)[0]
    return total_distance

def one_stop_time(start, stop, end):
    first = (start, stop)
    second = (stop, end)
    time_for_first = routes.get(first)[1]
    time_for_second = routes.get(second)[1]
    total_time = timeadd(time_for_first, time_for_second)
    return total_time

def two_stops(start, stop1, stop2, end):
    first = (start, stop1)
    second = (stop1, stop2)
    third = (stop2, end)
    total_distance = routes.get(first)[0] + routes.get(second)[0] + routes.get(third)[0]
    return total_distance

def two_stops_time(start, stop1, stop2, end):
    first = (start, stop1)
    second = (stop1, stop2)
    third = (stop2, end)
    time_for_first = routes.get(first)[1]
    time_for_second = routes.get(second)[1]
    time_for_third = routes.get(third)[1]
    time1 = timeadd(time_for_first, time_for_second)
    time2 = timeadd(time1, time_for_third)
    total_time = time2
    return total_time

def three_stops(start, stop1, stop2, stop3, end):
    first = (start, stop1)
    second = (stop1, stop2)
    third = (stop2, stop3)
    four = (stop3, end)
    total_distance = routes.get(first)[0] + routes.get(second)[0] + routes.get(third)[0] + routes.get(four)[0]
    return total_distance

def three_stops_time(start, stop1, stop2, stop3, end):
    first = (start, stop1)
    second = (stop1, stop2)
    third = (stop2, stop3)
    four = (stop3, end)
    time_for_first = routes.get(first)[1]
    time_for_second = routes.get(second)[1]
    time_for_third = routes.get(third)[1]
    time_for_four = routes.get(four)[1]
    time1 = timeadd(time_for_first, time_for_second)
    time2 = timeadd(time1, time_for_third)
    time3 = timeadd(time2, time_for_four)
    total_time = time3
    return total_time

def time_in_hours(t):
    pass

def avg_v(d, t):
    pass

def welcome():
    print("This is the tool to show you time and distance between cities in California.")
    print("Cities included (from North to South):")
    print("\n\tSacramento, Stockton, San Francisco, Fremont, Modesto, San Jose, Fresno, San Luis Obispo, "
          "\n\tBakersfield, Los Angeles, Long Beach, Riverside, Irvine, San Diego.")

# print(two_stops_time("Sacramento", "San Francisco", "San Jose", "San Luis Obispo"))
#
# print(three_stops_time("Sacramento", "San Francisco", "San Jose", "San Luis Obispo", "Bakersfield"))



