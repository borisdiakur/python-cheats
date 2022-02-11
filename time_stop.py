import time

start_time = time.time()

n = 10000
result = 0
for i in range(n):
    result += i

end_time = time.time()

print(f"It took {end_time - start_time}s.")
