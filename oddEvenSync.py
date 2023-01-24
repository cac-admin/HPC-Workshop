import time 

def basic_func(x): 
   time.sleep(2)
   if x == 0: 
     return 'zero'
   elif x%2 == 0: 
     return 'even' 
   else: 
     return 'odd'

starttime = time.time() 

final_results = ''

for i in range(0,10): 
   y = i*i 
   results = basic_func(y)
   final_results += str(i) + ' squared results in a/an ' + results + ' number \n'

print(final_results)
print('That took {} seconds'.format(time.time() - starttime)) 
