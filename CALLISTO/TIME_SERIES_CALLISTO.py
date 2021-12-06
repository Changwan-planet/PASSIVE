import os
from radiospectra.sources.callisto import CallistoSpectrogram
from callistoDownloader import callistoDownloader as cd
from astropy.io import fits

#cd.instrument_codes()
#cd.download(2021,11,1,['KASI'])

#     ++++++++++++++++++
#++++++TIME_SERIES_DATA++++++
#     ++++++++++++++++++
#KOREA UT FROM 22:30:00 TO 24:00:000
#KOREA UT FROM 00:00:00 TO 08:00:00

DATE1="2021-11-16"
tstart, tend = DATE1+"T22:30:00", DATE1+"T23:45:00"
#DATE2="2021-11-17"
#tstart, tend = DATE2+"T00:00:00", DATE2+"T08:00:00"

#PLEASE USE THIS, IF YOUR COMPUTER FAST. 
"""
DATE1="2021-11-04"
DATE2="2021-11-05"
tstart, tend = DATE1+"T22:30:00", DATE2+"T08:00:00"
"""
callisto = CallistoSpectrogram.from_range("KASI", tstart, tend)
callisto_nobg = callisto.subtract_bg()
callisto_nobg.peek(vmin=0)


#EVENT_1
#DATE2="2011-08-04"
#tstart, tend = DATE2+"T03:50:00", DATE2+"T04:15:00"






"""
#     ++++++++++++++++++++++++
#++++++DETAILED_DATA_ANALYSIS++++++
#     ++++++++++++++++++++++++
path="/home/changwan/PASSIVE/CALLISTO/e-Callisto/2021/11/01/"

file_list = os.listdir(path)
file_list.sort()

len_f_list = list(range(0,len(file_list),1))
print(len_f_list)
print(file_list[0])

#callisto = CallistoSpectrogram.read(path+file_list[0])

f1 = fits.open(path+file_list[0])
header = f1[0].header
#print(header)
#print(header['DATE-OBS'])


#print(callisto.get_header(TIME$_OB 

for i in len_f_list:
    print("i=",i)
    callisto = CallistoSpectrogram.read(path+file_list[i])
    callisto_nobg = callisto.subtract_bg()
    callisto_nobg.peek(vmin=0)
"""

