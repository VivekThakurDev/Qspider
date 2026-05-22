# @ total time ---> total time taken for execution of a program 

import time


def total_time(func):
    def wapper(*args,**kwargs):
        start= time.time()
        func(*args,**kwargs)
        end = time.time()
        print('total time taken ',end-start)
    return wapper
        
@total_time
def natural_num():
    for i in range(1,100):
        return(i)
natural_num()




