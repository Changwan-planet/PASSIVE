import os
import radiospectra
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

DATE1="2021-12-04"
tstart, tend = DATE1+"T22:30:00", DATE1+"T24:00:00"
#tstart, tend = DATE1+"T22:30:00", DATE1+"T25:45:00"

#DATE2="2021-12-04"
#tstart, tend = DATE2+"T00:00:00", DATE2+"T08:00:00"

#EVENT_3-HUMAIN-BELGIUM
#DATE3="2011-08-01"
#tstart, tend = DATE3+"T08:00:00", DATE3+"T08:15:00"

#PLEASE USE THIS, IF YOUR COMPUTER FAST. 
"""
DATE1="2021-11-04"
DATE2="2021-11-05"
tstart, tend = DATE1+"T22:30:00", DATE2+"T08:00:00"
"""
callisto = CallistoSpectrogram.from_range("KASI", tstart, tend)
callisto_nobg = callisto.subtract_bg()
callisto_nobg.peek(vmin=0)
#callisto.peek()


#EVENT_1
#DATE3="2011-08-04"
#tstart, tend = DATE3+"T03:50:00", DATE3+"T04:15:00"

#EVENT_2-BLEN5M-SWISS
#DATE3="2007-05-19"
#tstart, tend = DATE3+"T12:45:00", DATE3+"T13:00:00"

#EVENT_3-HUMAIN-BELGIUM
#DATE3="2011-08-01"
#tstart, tend = DATE3+"T07:45:00", DATE3+"T08:00:00"

#EVENT_4-KRIM-UKRINE-INTERFERENCE FROM THE SURFACE OF SEA.
#DATE3="2012-01-21"
#tstart, tend = DATE3+"T05:15:00", DATE3+"T05:30:00"





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

