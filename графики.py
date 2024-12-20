import matplotlib.pyplot as plt
import numpy as np

# Теоретические асимптотики
asymptotics = {
    "Линейный": ["θ(1)", "θ(n)", "θ(n)"],
    "Бинарный": ["θ(1)", "θ(log n)", "θ(log n)"],
    "Тернарный": ["θ(1)", "θ(log₃ n)", "θ(log₃ n)"],
    "Экспоненциальный": ["θ(1)", "θ(log i)", "θ(log n)"]
}

# Вывод теоретических асимптотик
print("Теоретические асимптотики алгоритмов поиска:")
print(f"{'Алгоритм':<15} {'Лучший случай':<15} {'Средний случай':<15} {'Худший случай':<15}")
for algo, times in asymptotics.items():
    print(f"{algo:<15} {times[0]:<15} {times[1]:<15} {times[2]:<15}")

# Функции для вычисления временных сложностей
def linear_best(n):
    return 1

def linear_avg(n):
    return n

def linear_worst(n):
    return n

def binary_best(n):
    return 1

def binary_avg(n):
    return np.log2(n)

def binary_worst(n):
    return np.log2(n)

def ternary_best(n):
    return 1

def ternary_avg(n):
    return np.log(n) / np.log(3)

def ternary_worst(n):
    return np.log(n) / np.log(3)

def exponential_best(n):
    return 1

def exponential_avg(n):
    return np.log2(n)

def exponential_worst(n):
    return np.log2(n)

# Генерация данных для графиков
n_values = np.linspace(1, 1000, 100)

linear_best_values = [linear_best(n) for n in n_values]
linear_avg_values = [linear_avg(n) for n in n_values]
linear_worst_values = [linear_worst(n) for n in n_values]

binary_best_values = [binary_best(n) for n in n_values]
binary_avg_values = [binary_avg(n) for n in n_values]
binary_worst_values = [binary_worst(n) for n in n_values]

ternary_best_values = [ternary_best(n) for n in n_values]
ternary_avg_values = [ternary_avg(n) for n in n_values]
ternary_worst_values = [ternary_worst(n) for n in n_values]

exponential_best_values = [exponential_best(n) for n in n_values]
exponential_avg_values = [exponential_avg(n) for n in n_values]
exponential_worst_values = [exponential_worst(n) for n in n_values]

# Построение графиков
def plot_and_save(title, best_values, avg_values, worst_values, filename):
    plt.figure()
    plt.plot(n_values, best_values, label='Лучший случай')
    plt.plot(n_values, avg_values, label='Средний случай')
    plt.plot(n_values, worst_values, label='Худший случай')
    plt.title(title)
    plt.xlabel('n')
    plt.ylabel('Время')
    plt.legend()
    plt.grid()
    plt.savefig(filename)
    plt.show()

# Линейный поиск
plot_and_save('Линейный поиск', linear_best_values, linear_avg_values, linear_worst_values, 'linear_search.png')

# Бинарный поиск
plot_and_save('Бинарный поиск', binary_best_values, binary_avg_values, binary_worst_values, 'binary_search.png')

# Тернарный поиск
plot_and_save('Тернарный поиск', ternary_best_values, ternary_avg_values, ternary_worst_values, 'ternary_search.png')

# Экспоненциальный поиск
plot_and_save('Экспоненциальный поиск', exponential_best_values, exponential_avg_values, exponential_worst_values, 'exponential_search.png')

# Общий график
plt.figure()
plt.plot(n_values, linear_avg_values, label='Линейный поиск')
plt.plot(n_values, binary_avg_values, label='Бинарный поиск')
plt.plot(n_values, ternary_avg_values, label='Тернарный поиск')
plt.plot(n_values, exponential_avg_values, label='Экспоненциальный поиск')
plt.title('Сравнение алгоритмов поиска')
plt.xlabel('n')
plt.ylabel('Время')
plt.legend()
plt.grid()
plt.savefig('comparison.png')
plt.show()
