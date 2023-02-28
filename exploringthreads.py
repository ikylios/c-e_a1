import threading
import time
import numpy as np

# Inside the thread you are expected to 
# add the first N (1 < N < 1000) numbers in the array 
# provided as an argument from function spawning the threads.
def thread_function(upto):
  np.sum(np.arange(upto))

times = []
i = 0

while (i <= 1000):
  start = time.time()
  upto = np.random.randint(1000)

  x = threading.Thread(target = thread_function(upto))
#  thread_function(upto)
  x.start()

  x.join()
  end = time.time()

  time_taken = end - start
  times.append(time_taken)
  
  i = i+1

print('avg: ', np.average(times))   
print('min: ', np.min(times))       
print('max: ', np.max(times))       
print('std. dev.: ', np.std(times)) 
