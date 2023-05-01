import math

import numpy as np
import matplotlib.pyplot as plt

consumption = np.array([105, 109, 110, 113, 120, 122, 123, 126, 134, 140, 145, 150])
profit = np.array([102, 105, 108, 110, 115, 117, 119, 125, 132, 130, 141, 144])

# Апроксимація даних методом найменших квадратів
a, b = np.polyfit(consumption, profit, deg=1)
# mean
meanX = np.mean(consumption)
meanY = np.mean(profit)
el_koef = b*(meanX/meanY)/10
print("Коефіцієнти апроксимації:")
print("a =", a)
print("b =", b)
print("Коефіцієнт еластичності", el_koef)
#STD
n=len(consumption)
sum = 0
for i in range(0, n):
    sum += (consumption[i]-meanX)**2/n
    i+=1
std = math.sqrt(sum)
print("Середньоквадратичне відхилення", std)

# Coef of Variatiom
variation =(std/meanX)*100
print("Коефіцієнт варіації:", variation)


# Розрахунок коефіцієнта детермінації
y_pred = a * consumption + b
r_squared = 1 - (np.sum((profit - y_pred)**2) / ((n - 1) * np.var(profit, ddof=1)))
print("Коефіцієнт детермінації:", r_squared)

#Коефіцієнт кореляції

r = math.sqrt(r_squared)
print("Коефіцієнт кореляції:", r)


fisher_num = 0
fisher_den =0
for i in range(0, n):
    fisher_num += ((a + b*consumption[i]) - meanY)**2
    fisher_den += (profit[i]- (a + b*consumption[i]))**2/(n-2)
    i+=1
fisher = fisher_num/fisher_den
print("критерій Фішера:", fisher)


# Побудова графіку
plt.plot(consumption, profit, marker='o', label='Фактичні дані')
plt.plot(consumption, a*np.array(consumption) + b, label='Апроксимація')

plt.xlabel('Обсяг споживання (у.о.)')
plt.ylabel('Наявний прибуток (у.о.)')
plt.title('Графік залежності наявного прибутку від обсягу споживання')

plt.legend()
plt.show()


fisher_den=0

