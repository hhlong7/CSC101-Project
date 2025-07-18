from classes import *
from data import *

def timeadd(t1: Time, t2: Time)-> Time:
#time add functions.
    totalmin = t1.minute + t2.minute
    totalhour = t1.hour + t2.hour
    secondtomin = 0
    mintohour = 0
    if totalmin >= 60:
        mintohour = totalmin // 60
        totalmin = totalmin % 60
    totalhour += mintohour
    return Time(totalhour, totalmin)

def get_distance(start, end):
#get the distance when input 2 location
    try:
        location_key = (start, end)
        d = routes.get(location_key)
        if d != None:
            return d[0]
        else:
            raise Exception("\nLocation is not within the database.")
    except Exception as e:
        print(e)


def get_time(start, end):
#get the time when input 2 locations
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
#get the distance when input 3 locations
    try:
        first = (start, stop)
        second = (stop, end)
        total_distance = routes.get(first)[0] + routes.get(second)[0]
        return total_distance
    except TypeError:
        print("\nLocation is not in Database")

def one_stop_time(start, stop, end):
#get the time when input 3 locations
    try:
        first = (start, stop)
        second = (stop, end)
        time_for_first = routes.get(first)[1]
        time_for_second = routes.get(second)[1]
        total_time = timeadd(time_for_first, time_for_second)
        return total_time
    except TypeError:
        print("Try another location.")

def two_stops(start, stop1, stop2, end):
#get the distance when input 4 locations
    try:
        first = (start, stop1)
        second = (stop1, stop2)
        third = (stop2, end)
        total_distance = routes.get(first)[0] + routes.get(second)[0] + routes.get(third)[0]
        return total_distance
    except TypeError:
        print("\nLocation is not in Database.")

def two_stops_time(start, stop1, stop2, end):
# get the time when input 4 locations, try and except for location outside of the database
    try:
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
    except TypeError:
        print("Try another location.")

def three_stops(start, stop1, stop2, stop3, end):
#get the distance when input 5 locations
    try:
        first = (start, stop1)
        second = (stop1, stop2)
        third = (stop2, stop3)
        four = (stop3, end)
        total_distance = routes.get(first)[0] + routes.get(second)[0] + routes.get(third)[0] + routes.get(four)[0]
        return total_distance
    except TypeError:
        print("\nLocation is not in Database")

def three_stops_time(start, stop1, stop2, stop3, end):
#get the time when input 5 locations, try and except for location outside of the database
    try:
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
    except TypeError:
        print("Try another location.")

def avg_v(d, t):
#This function compute the velocity that is required to get to the final destination within the given time
    hour = int(t.hour)
    minutes = int(t.minute)
    minutes_to_hour = minutes / 60
    total_hour = hour + minutes_to_hour
    speed = d / total_hour
    return round(speed,2)

def welcome():
#This function will display the welcome message when the user run the code.
    print("This is the tool to show you time and distance between cities in California.")
    print("Cities included (from North to South):")
    print("\n\tSacramento, Stockton, San Francisco, Fremont, Modesto, San Jose, Fresno, San Luis Obispo, "
          "\n\tBakersfield, Los Angeles, Long Beach, Riverside, Irvine, San Diego.")




