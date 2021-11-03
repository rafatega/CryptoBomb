import time
start_time = time.time()

for i in range(100000):
    print('aaaaaaaaa')

execution_time = round((time.time() - start_time), 2)

print(execution_time)
