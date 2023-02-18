class Athlete:
  name = ""
  pushups = []
  pullups = []
  maxhang = []
  maxplank = []
  squats = []
  top5 = []

  def getPushupDifference(self):
    return self.pushups[1]-self.pushups[0]
    pass
  def getPullupDifference(self):
    return self.pullups[1]- self.pullups[0]
    pass
  def getSquatDifference(self):
    return self.squats[1]- self.squats[0]
    pass

  #int("1") -> 1
  #split(":") -> ["1", "33"]
  def getMaxHangDifference(self):
    if self.maxhang[0].isalpha():
      return ("x")
    if self.maxhang[1].isalpha():
      return ("x")
    time1 = self.maxhang[1].split(":")
    if len(time1) != 2:
      return ("x")
    if len(time1[0]) == 0:
      time1[0] = 0
    seconds = int (time1[0]) * 60
    seconds += int(time1[1])
    time2 = self.maxhang[0].split(":")
    if len(time2[0]) == 0:
      time2[0] = 0
    if len(time2) != 2:
      return ("x")
    seconds2 = int (time2[0]) * 60
    seconds2 += int(time2[1])
    return seconds- seconds2
    pass
  def getMaxPlankDifference(self):
    if self.maxplank[0].isalpha():
      return ("x")
    if self.maxplank[1].isalpha():
      return ("x")
    time1 = self.maxplank[1].split(":")
    if len(time1) != 2:
      return ("x")
    if len(time1[0]) == 0:
      time1[0] = 0
    seconds = int (time1[0]) * 60
    seconds += int(time1[1])
    time2 = self.maxplank[0].split(":")
    if len(time2[0]) == 0:
      time2[0] = 0
    if len(time2) != 2:
      return ("x")
    seconds2 = int (time2[0]) * 60
    seconds2 += int(time2[1])
    return seconds- seconds2
    pass
  def getTop5Difference(self):
    return self.top5[1]- self.top5[0]
    pass
  def getTop5Average(self):
    x-y
    pass