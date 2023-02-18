import csv
from classes import Athlete

f = open("data.csv" , 'r')

greg = Athlete()
greg.name = "Greg"
greg.pushups.append(31)
greg.pushups.append(41)
greg.pullups.append(31)
greg.pullups.append(41)
#for time, left of : times 60 + right of :
#'1:33' -> 1,33, (1x60) + 33
greg.maxhang.append(470)
greg.maxhang.append(490)
greg.maxplank.append(500)
greg.maxplank.append(501)
greg.squats.append(90)
greg.squats.append(100)
#"4 4 4 4 4" -> ['4','4','4',4,4] 
greg.top5.append([4,4,4,4,4])
greg.top5.append([5,4,5,2,3])


athletes = []
with f:
  reader = csv.reader(f)
  skip = next(reader)
  while(True):
    try:
      row1 = next(reader)
      row2 = next(reader)
    except:
      break
      
    #Readaing data
    a = Athlete()
    a.name = row1[0]
    if(len(row1[1]) > 0 and row1[1] != "injury"):
      a.pushups = [int(row1[1])]
    else:
      a.pushups = [0]
      
    if(len(row2[1]) > 0 and row2[1] != "injury"):
      a.pushups.append(int(row2[1]))
    else:
      a.pushups.append(0)
      
    if(len(row1[2]) > 0) and row1[2] != "injury":
      a.pullups = [int(row1[1])]
    else:
      a.pullups= [0]
    if(len(row2[2]) > 0 and row2[2] != "injury"):
      a.pullups.append(int(row2[2]))
    else:
      a.pullups.append(0)
    a.maxhang = [row1[3] , row2[3]]
    a.maxplank = [row1[4] , row2[4]]
    if(len(row1[5]) > 0 and row1[5] != "injury"):
      a.squats = [int(row1[5])]
    else:
      a.squats= [0]
    if(len(row2[5]) > 0 and row2[5] != "injury"):
      a.squats.append(int(row2[5]))
    else:
      a.squats.append(0)
    a.top5 = [row1[7] , row2[7]]
    athletes.append(a)
    #end reading
    
for a in athletes:
  print(a.name, str(a.getPushupDifference()) + " pushups,", str(a.getSquatDifference()) + " squats,", str(a.getPullupDifference()) + " pullups,", str(a.getMaxHangDifference()) + " overall hang time,", str(a.getMaxPlankDifference()) + " overall plank time")