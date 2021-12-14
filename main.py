import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import numpy as np

# Изучить характер эволюции популяции,
# описываемый моделью,
# при значениях параметров a = 1, R = 1, N_0 = 100
# в зависимости от значения параметра b
# в диапазоне 0,1 ≤ b < 10.
# Есть ли качественные различия
# в характере эволюции
# в зависимости от значения b?
#
# N_(t+1) = (N_t ∙ R)/(1 + (a ∙ N_t) ^ b)
#
# N_t = N_0 ∙ R ^ t

A = 1
R = 1
N_0 = 100

# Выведем значения в консоль

t = 0
b = 0.1

while b <= 10:
  N_t = N_0 * (R ** t)
  N_next = (N_t * R)/(1 + ((A * N_t) ** b))
  # print(N_t) # при R = 1 всегда равняется 100
  print(f'При b = {b} \t N(t+1) = {N_next}')
  b = round(b + 0.1, 2)
  t += 1

# N_t = N_0 * (R ** t)
# N_next = (N_t * R)/(1 + ((A * N_t) ** b))
# # print(N_t) # при R = 1 всегда равняется 100
# print(f'При b = {b} N(t+1) = {N_next}')


# Построим график

# Независимая (x) и зависимая (y) переменные
b = np.linspace(0.1, 10, 100)
N_next = (100 * R)/(1 + ((A * 100) ** b))

# Построение графика
plt.title("N \u209C\u208A\u2081 = (N \u209C \u2027 R) / (1 + (a \u2027 N \u209C) \u1D47)") # заголовок
plt.xlabel("b") # ось абсцисс
plt.ylabel("N \u209C\u208A\u2081") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(b, N_next)  # построение графика

plt.show()
