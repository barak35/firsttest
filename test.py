#import auth
#import logininfo

from importlib import reload
import price
import time

chklow=0
chkhigh=0
curVal=0

def valueChk(lastVal):
    reload(price)
    curVal = price.korbit.lastXRP

    global chkcnt

    if curVal < lastVal:
        chkcnt = chkcnt +1
    return chkcnt

while 1:
    time.sleep(5)
    chk = valueChk(price.korbit.lastXRP)


