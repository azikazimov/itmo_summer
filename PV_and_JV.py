import matplotlib.pyplot as plt
import numpy as np



areaMeasurementAccuracy = 5 # здесь указать точность измерения площади. Если до 3-его знака, то указать 5
filename = 'main.txt' # здесь указать имя файла
a = np.loadtxt(filename, skiprows=3, usecols=(0, 1, 2, 3))
f = open(filename, 'r')
text = f.read()
s = text[text.find('S=') + 2: text.find('S=') + 2 + areaMeasurementAccuracy] # выделяем площадь солнца. Костыль, но работает

listWt = []
for i in range(len(a)):
    listWt.append((-1) * a[i][3] * float(s) * a[i][0])

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
ax1.plot(a[:, 0], a[:, 3])
ax1.axhline(y=0, c='black')
ax1.set_ylabel('mA/cm2')
ax1.set_xlabel('V')
ax1.grid()
ax2.plot(a[:, 0], listWt)
ax2.axhline(y=0, c='black')
ax2.set_ylabel('Wt')
ax2.set_xlabel('V')
ax2.grid()

VocMin, VocMax = 0, 0
for i in range(len(a)):
    if a[i][3] < 0:
        VocMax = a[i][0]
        break

for i in range(len(a)-1, -1, -1):
    if a[i][3] > 0:
        VocMin = a[i][0]
        break

mediana = (abs(VocMax) + abs(VocMin)) / 2

print('Jsc = ' + str(a[-1, 3]))
print('Voc = ' + str(mediana))
print('Pmax = ' + str(max(listWt)))
print('Vmax = ' + str(a[listWt.index(max(listWt))][0]))
plt.show()