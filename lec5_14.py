import time 

timer = time.time()
for i in range (10):
    print(i)
    time.sleep(2)

print(f"{time.time() - timer}, seconds")