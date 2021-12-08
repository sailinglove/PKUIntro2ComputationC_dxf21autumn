# [0: icID, 1: cardType, 2:tradeType, 3: UpLine, 4: UpTime, 5: UpStation, 
#  6: DownLine, 7: DownTime, 8: DownStation]
import time

data_file = r"20211202\Subway_20180301\Subway_20180301.txt"
# data_file = r"20211202\Subway_20180301\Subway_20190301_top100000.txt"
# data_file = "test.txt"
out_file = r"20211202\PeopleInSubwayTime.txt"

timeslot = {}

# remove redundant char in a line
def lineProcess(l: str):
    lst = l.lstrip('SUB,').rstrip(',NM\n').split(',')
    return lst

# calculate ride time, return None if data is invalid
def rideTime(l: list):
    if (l[4][:8] != "20180301") or (l[7][:8] != "20180301"):
        print(l[4], l[4][:8], l[7], l[7][:8])
        # print("wrong date")
        return None
    upTime = time.mktime(time.strptime(l[4],"%Y%m%d%H%M%S"))
    downTime = time.mktime(time.strptime(l[7],"%Y%m%d%H%M%S"))
    timeUsed = downTime - upTime
    if (timeUsed == 0) or (timeUsed <= 0):
        # print("wrong time")
        return None
    return timeUsed

# convert second to minutes with rounding off
def sec2min(s: float):
    return round(s / 60)

# record ride time to its corresponding dictionary item
def record(t: int):
    global timeslot
    if t > 120:
        t = 120
    if t in timeslot.keys():
        timeslot[t] += 1
    else:
        timeslot[t] = 1

with open(data_file, "r") as f:
    line = f.readline()  # Discard first line
    line = f.readline()  # Read in second line for processing
    while line != '':
        lineLst = lineProcess(line)
        rtime = rideTime(lineLst)
        if rtime:
            record(sec2min(rtime))
        line = f.readline()

with open(out_file, "w") as f:
    for i in range(121):
        if i in timeslot.keys():
            f.write("{} {}\n".format(i, timeslot[i]))
