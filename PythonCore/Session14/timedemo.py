'''
time: it is a built-in module in python which is used to impelment date and time related implementation.
Handling "Epoch time" in Python typically means working with Unix timestamps—the number of seconds that have passed since January 1, 1970 (UTC)(except leap year).
Value    Meaning
0        Standard Time:DST is not in effect (the "normal" clock).
1        Daylight Saving Time: DST is active (usually the clock is set 1 hour forward).
'''
from time import *
val=time()
print("EPOSH time:",val)
print("=============")

tup_time = localtime(val)
print("Tuple Time:",tup_time)
print("=============")

usabletime = asctime(tup_time)
print("Time is:",usabletime)
print("=============")

gmt_tuptime = gmtime(val)
print("GMT Tuple:",gmt_tuptime)
print("=============")

gmt_usabletime = asctime(gmt_tuptime)
print("GMT Time is:",gmt_usabletime)
print("=============")

'''
%a : Tue
%A : Tuesday
%b : May
%c : Tue May  5 14:54:11 2026
%C : 20
%d : 05
%D : 05/05/26
%e : 5
%F : 2026-05-05
%g : 26
%G : 2026
%h : May
%H : 15
%I : 03
%j : 125
%m : 05
%M : 06
%p : PM
%r : 03:08:52 PM
%R : 15:09
%S : 33
%T : 15:10:13 
%u : 2
val=strftime("%u") uses the strftime function to return the current weekday as a decimal number ranging from 1 to 7, where Monday is 1 and Sunday is 7
%U : 18
The strftime("%U") command returns the week number of the current year as a decimal number (00 - 53)
%x : 05/05/26
%X : 15:17:20
%y : 26
%Y : 2026
'''
val=strftime("%d-%m-%Y %H:%M:%S %p")
#05-05-2026 15:19:53 PM
#print(val)
print("===========")
while True:
    val=strftime("%c")
    print(val)
    sleep(1)














