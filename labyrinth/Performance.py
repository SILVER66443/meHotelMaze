import RecBack
import matplotlib.pyplot as plt
import time

size = 27
times = []
for i in range(20):
    start = time.time()
    maze = RecBack.RecBack([size + i * 20, size + i * 20])
    during = time.time() - start
    print(during)
    times.append([size + i * 20, during])
print(times)
x = []
y = []
for point in times:
    x.append(point[0])
    y.append(point[1])
plt.plot(x, y)
plt.xlabel("size")
plt.ylabel("time")
plt.show()
