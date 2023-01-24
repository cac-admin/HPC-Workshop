import time 
from dask import delayed

def basic_func(x): 
    time.sleep(2) 
    if x == 0: 
        return 'zero' 
    elif x%2 == 0: 
        return 'even' 
    else: 
        return 'odd' 

starttime = time.time() 

delayed_basic_func = delayed(basic_func)

final_results = ''

for i in range(0,10): 
    y = i*i 
    delayed_results = delayed_basic_func(y) # or delayed(basic_func)(y)
    final_results += str(i) + ' squared results in a/an ' + delayed_results + ' number \n'

    
print(final_results.compute())
print('That took {} seconds'.format(time.time() - starttime)) 

