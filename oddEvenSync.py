import time 

def basic_func(x): 
    if x == 0: 
        return 'zero' 
    elif x%2 == 0: 
        return 'even' 
    else: 
        return 'odd' 

starttime = time.time() 

for i in range(0,10): 
    y = i*i 
    time.sleep(2) 
    print('{} squared results in a/an {} number'.format(i, basic_func(y))) 

print('That took {} seconds'.format(time.time() - starttime)) 

