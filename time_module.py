import time
print(time.time()) #prints the time in seconds from epoch
print(time.ctime((time.time())))# The time is represented as the number of seconds since January 1, 1970.
# // it is the point at which unix time start "epoch"
# we get time in string from the seconds we enter in the time.ctime()
print(time.localtime()) #it gives a time structure with year,month,date,hours...etc...
print(time.asctime()) # takes in arg as tuple which is returned by localtime() and returns time in ctime() format