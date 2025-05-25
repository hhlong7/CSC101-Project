from classes import *

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

def km_to_mile(n1):
    return n1 / 1.609

