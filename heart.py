import max30102
import hrcalc
import my_heart_calc
import numpy as np

def heart_beat():
    rate=0
    oxy=0
    count=0
    a = 0
    base=[]
    while a<10:
        m=max30102.MAX30102()
        red,ir,time=m.read_sequential()
        v=my_heart_calc.final_rate(red)
        base.append(v)
        a=a+1
    pulse_mean=np.mean(base)
    n=pulse_mean/0.1
    heart_beat=n*4.4
    print "heart beat is ",str(heart_beat)
