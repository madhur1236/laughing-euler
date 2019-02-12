#pb-3
from datetime import datetime

def largestPrimeFactor(n):
  l_fact = 1
  while n % 2 == 0:
    l_fact = 2
    n = n/2
 
    
  p = 3
  while n != 1:
    while n % p == 0:
      l_fact = p
      n = n/p
    p += 2
  return l_fact
   
if __name__== "__main__":
  start_time = datetime.now()
  print(largestPrimeFactor(5))
  end_time = datetime.now()
  print('Duration in microseconds: {}'.format(end_time - start_time))

  
  
        
    
