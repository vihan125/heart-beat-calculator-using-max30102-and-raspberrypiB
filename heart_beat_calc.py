import numpy as nn

def calc_pulse(red_log):
    red_mean=int(nn.mean(red_log))
    pulse=0
    n=0
    count=0
    while n<len(red_log):
        piece=red_log[n:n+10]
        if piece_mean(piece,red_mean)>=20:
            count=count+1
            for i in range(1,len(red_log)-(10+n)):
                n=n+1
                piece=red_log[n:n+10]
                if piece_mean(piece,red_mean)>=5:
                    count=count+1
                elif i==10:
                    break
                else:
                    break
            if count>=5:
                pulse=pulse+1
        count=0
        n=n+1
    return pulse
                
            
def final_rate(red_data):
    no_pulse=calc_pulse(red_data)
    return no_pulse

def piece_mean(piece,red_mean):
    piece_mean=int(nn.mean(piece))
    return piece_mean-red_mean
