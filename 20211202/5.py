# [0: icID, 1: cardType, 2:tradeType, 3: UpLine, 4: UpTime, 5: UpStation, 
#  6: DownLine, 7: DownTime, 8: DownStation]
import time
from tqdm import tqdm

data_file = r"20211202\Subway_20180301\Subway_20180301.txt"
# data_file = r"20211202\Subway_20180301\Subway_20190301_top100000.txt"
# data_file = "test.txt"
out_file = r"20211202\PeopleInSubwayCount.txt"

def t2tStamp(t: str):
    return int(time.mktime(time.strptime(t,"%Y%m%d%H%M%S")))

sTime = int(t2tStamp("20180301000000"))
eTime = int(t2tStamp("20180302000000"))

timeslot = {}

for i in range(sTime, eTime, 10*60):
    timeslot["{}-{}".format(i, i+10*60)] = 0
    # timeslot["1519833600-1519834200"]

# convert second to minutes with rounding off
def sec2min(s: float):
    return round(s / 60)

# remove redundant char in a line
def lineProcess(l: str):
    lst = l.lstrip('SUB,').rstrip(',NM\n').split(',')
    if (lst[4][:8] != "20180301") or (lst[7][:8] != "20180301"):
        print(lst[4], lst[4][:8], lst[7], lst[7][:8])
        # print("wrong date")
        return None
    return lst

def count(l: list):
    for k in timeslot.keys():
        if (int(k[11:]) < t2tStamp(l[4])) or (int(k[:10]) >= t2tStamp(l[7])):
            # print(time.strftime("%H:%M",time.localtime(int(k[:10]))))
            # print(time.strftime("%H:%M",time.localtime(int(k[11:]))))
            # print(l[4][8:])
            # print(l[7][8:])
            continue
        else:
            timeslot[k] += 1

with open(data_file, 'r') as f:
    with (tqdm(total=5304940)) as pbar:
        line = f.readline()  # Discard first line
        line = f.readline()  # Read in second line for processing
        pbar.update(2)
        while line != '':
            lineLst = lineProcess(line)
            pbar.update(1)
            if lineLst == None:
                line = f.readline()
                continue
            count(lineLst)
            line = f.readline()

with open(out_file, 'w') as f:
    for k in timeslot.keys():
        f.write("[{}-{}]\t{}\n".format(
            time.strftime("%H:%M",time.localtime(int(k[:10]))), 
            time.strftime("%H:%M",time.localtime(int(k[11:]))), timeslot[k]))
