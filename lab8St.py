import numpy as np
from scipy.stats import t

# вхідні дані
x = np.array([105, 109, 110, 113, 120, 122, 123, 126, 134, 140, 145, 150])
y = np.array([102, 105, 108, 110, 115, 117, 119, 125, 132, 130, 141, 144])

# визначаємо середні значення кожної вибірки
x_mean = np.mean(x)
y_mean = np.mean(y)

print("Середнє значення для x: ", x_mean)
print("Середнє значення для y: ", y_mean)

# визначаємо дисперсії кожної вибірки
x_var = np.var(x, ddof=1)
y_var = np.var(y, ddof=1)

print("Дисперсія для x: ", x_var)
print("Дисперсія для y: ", y_var)

# обчислюємо t-статистику
t_statistic = (x_mean - y_mean) / np.sqrt((x_var / len(x)) + (y_var / len(y)))

# визначаємо кількість ступенів свободи та критичне значення t
degrees_of_freedom = len(x) + len(y) - 2
alpha = 0.05
t_critical = t.ppf(1 - alpha / 2, degrees_of_freedom)

print("t-статистика: ", t_statistic)
print("Критичне значення t: ", t_critical)

# порівнюємо t_statistic та t_critical
if abs(t_statistic) > t_critical:
    print("Різниця між середніми значеннями статистично значуща")
else:
    print("Різниця між середніми значеннями нестатистично значуща")