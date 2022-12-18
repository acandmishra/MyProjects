import calendar as c
print(c.calendar(2022)) # takes year as argument
c.prcal(2022) # directly prints on screen without using print function
print(c.month(2022,12)) #takes year and month number and returns calendar for that month in that year
print(c.isleap(2022)) # returns boolean value for whetehr the year is leap or not
print(c.leapdays(2022,2065)) # 22 inclusive 65 exclusive ... gives no. of leap years in the range
print(c.weekday(2022,12,13)) # below indices are returned 
# M T W TH F SAT SUN
# 0 1 2  3 4  5   6
