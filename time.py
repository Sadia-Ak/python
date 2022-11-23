import time 

#total_minutes = int(input('Hours * 60'))
time.strftime('%H , %M , %S')

Hours= int(input('HOURS>')) 
Minutes = int(input('MINUTES>'))
Alarm_time = str(input('ALARM TIME:'))
#Seconds = int(input())
#Actual_time = str(input('ACTUAL TIME:'))

if (Minutes<40):
  Minutes = 60 - (40 - Minutes)
  Hours = Hours - 1 
  if (Hours < 0):
   Hours = 23

else : 
 Minutes = Minutes - 40

Hours =  time.strftime(Hours,Minutes,Alarm_time)
print(', MINUTES')
