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
  x = threading.Thread(target = thread_function(i))

  x.start()

  x.join()
  end = time.time()

  time_taken = end - start
  times.append(time_taken)
  
  i = i+1

print('avg: ', np.average(times))   # 7.062144093699269e-05
print('min: ', np.min(times))       # 4.649162292480469e-05
print('max: ', np.max(times))       # 0.0006959438323974609
print('std. dev.: ', np.std(times)) # 3.9885827680166593e-05