from funcs import *
from data import *
from classes import *

def main():
    i1 = input("Initial location: ")
    i2 = input("Final location: ")

    distance = get_distance(i1, i2)
    time = get_time(i1, i2)

    if distance and time != None:
        print("Distance {}, ETA: {}".format(distance, time))
        new = input("Want to stop by any place on the way? (y/n) ")
        total_distance = 0
        total_time = Time(0, 0, 0)
        while new == 'y':
            i3 = input("Stop: ")
            total_distance += get_distance(i1, i3) + get_distance(i3, i2)
            delta_time = timeadd(get_time(i1, i3), get_time(i3, i2))
            total_time = timeadd(total_time, delta_time)
            print("Distance {}, ETA: {}".format(total_distance, total_time))
            new = input("Want to stop by another place? (y/n) ")

        print("Have a safe trip.")
    else:
        None

    # new = input("Want to stop by any place on the way? ")
    # while new == 'yes':
    #     total_distance = 0
    #     total_time = 0
    #     i3 = input("Stop: ")
    #     total_distance += get_distance(i1,i3) + get_distance(i3, i2)
    #     total_time = timeadd(get_time(i1,i3), get_time(i3,i2))
    #     print("Distance {}, ETA: {}".format(total_distance, total_time))
    #     new = input("Want to stop by another place? ")

    # if distance and time != None:
    #     print("Distance {}, ETA: {}".format(distance, time))
    #     #new = input("Want to stop by any place on the way? (y/n) ")
    #     new = "y"
    #     total_distance = 0
    #     total_time = Time(0,0,0)
    #     i3 = "San Jose"
    #     while new == 'y':
    #         i3 = input("Stop: ")
    #         delta_distance = get_distance(i1, i3) + get_distance(i3,i2)
    #         delta_time = timeadd(get_time(i1, i3), get_time(i3, i2))
    #
    #         #new = input("Want to stop by another place? (y/n) ")
    #         new = 'y'
    #         if new == 'y':
    #             i1 = i3
    #     total_distance += delta_distance
    #     total_time = timeadd(total_time, delta_time)
    #     print("Distance {}, ETA: {}".format(total_distance, total_time))
    #     print("Have a safe trip.")
    # else:
    #     None


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