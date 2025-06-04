from funcs import *
from data import *
from classes import *

def main():
    welcome()
    i1 = input("\nInitial location: ")
    i2 = input("Final location: ")
    distance = get_distance(i1, i2)
    time = get_time(i1, i2)
    if distance and time != None:
        print("\nDistance {}, ETA: {}".format(distance, time))
        new = input("\nWant to stop by any place on the way? (y/n) ")
        if new == 'y':
            stops = int(input("How many stops: (1,2,3) "))
            if stops == 1:
                stop1 = input("Stop: ")
                distance1 = one_stop(i1, stop1, i2)
                time1 = one_stop_time(i1, stop1, i2)
                print("\nDistance: {}, Time: {}".format(distance1, time1))
            if stops == 2:
                stop1 = input("First stop: ")
                stop2 = input("Second stop: ")
                distance2 = two_stops(i1, stop1, stop2, i2)
                time2 = two_stops_time(i1, stop1, stop2, i2)
                print("\nDistance: {}, Time: {}".format(distance2, time2))
            if stops == 3:
                stop1 = input("First stop: ")
                stop2 = input("Second stop: ")
                stop3 = input("Third stop: ")
                distance3 = three_stops(i1, stop1, stop2, stop3, i2)
                time3 = three_stops_time(i1, stop1, stop2, stop3, i2)
                print("\nDistance: {}, Time: {}".format(distance3, time3))
        print("Have a safe trip.")
    else:
        None


# def error(start, end, stop):
#     if stop == None:
#         return None
#
#     try:
#         if routes.get(location) == None:
#             raise Exception("This is an error, the location is not within CA")
#     except Exception as e:
#         print(e)


if __name__ == '__main__':
    main()