import numpy as np
import pandas as pd
import multiprocessing as mp
import time
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt


df = pd.DataFrame(np.random.randint(3, 10, size=[20000,100]))
#print(df.head())

def minmax(df):
  return np.sqrt((df[1].min())**2 + (df[1].max())**2)
    #return result
    #taking min and max of column passed in pool below as df.columns

with mp.Pool(1) as pool:
    starttime1 = time.time()
    seq = [df[i] for i in df.columns]
    result = pool.imap(minmax, seq, chunksize=10)
    output = [round(x, 2) for x in result]
    output1 = time.time() - starttime1

print(output1)
print('Execution Time CPU = 1: {time.time() - starttime1} seconds')
#print(output)


with mp.Pool(2) as pool:
    starttime2 = time.time()
    seq = [df[i] for i in df.columns]
    result = pool.imap(minmax, seq, chunksize=10)
    output = [round(x, 2) for x in result]
    output2 = time.time() - starttime2


print(output2)
#print(output)
print('Execution Time CPU = 2: {time.time() - starttime2} seconds')


with mp.Pool(4) as pool:
    starttime4 = time.time()
    seq = [df[i] for i in df.columns]
    result = pool.imap(minmax, seq, chunksize=10)
    output = [round(x, 2) for x in result]
    output4 = time.time() - starttime4

print(output4)
#print(output)
print('Execution Time CPU = 4: {time.time() - starttime4} seconds')

with mp.Pool(8) as pool:
    starttime8 = time.time()
    seq = [df[i] for i in df.columns]
    result = pool.imap(minmax, seq, chunksize=10)
    output = [round(x, 2) for x in result]
    output8 = time.time() - starttime8

print(output8)
#print(output)
print('Execution Time CPU = 8: {time.time() - starttime8} seconds')


processors = [1,2,4,8]
elapsed_Pool = [output1,output2,output4,output8]

plt.plot(processors,elapsed_Pool, label='Pool', color='red')
plt.xlabel('All the Processors')
plt.ylabel('Elapsed Time')
plt.legend()
plt.savefig('Elapsed_time.png',transparent=True, bbox_inches='tight')
plt.show()


# print(minmax(df))
