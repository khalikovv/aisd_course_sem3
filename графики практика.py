import matplotlib.pyplot as plt
import numpy as np
import re
from collections import defaultdict

filename = 'results.txt'

data = defaultdict(lambda: defaultdict(list))

with open(filename, 'r') as file:
    for line in file:
        match = re.match(r"Size: (\d+), Algorithm: (\w+), Case: (\w+), Time: ([\d\.e\-]+)", line)
        if match:
            size, algorithm, case, time = match.groups()
            size = int(size)
            time = float(time)
            data[algorithm][case].append((size, time))

cases = ['best', 'worst', 'average']
colors = {'best': 'blue', 'worst': 'red', 'average': 'green'}
case_labels = {'best': 'Лучший случай', 'worst': 'Худший случай', 'average': 'Средний случай'}

for algorithm, cases_data in data.items():
    plt.figure(figsize=(10, 6))

    print(f"Полиномы регрессии для алгоритма {algorithm}:")

    for case in cases:
        if case in cases_data:
            sizes, times = zip(*sorted(cases_data[case]))
            sizes = np.array(sizes)
            times = np.array(times)

            degree = 2 if algorithm in ['linear_search', 'exponential_search'] else 1
            coef = np.polyfit(sizes, times, degree)  
            poly = np.poly1d(coef)
            predicted_times = poly(sizes)

            poly_str = ' + '.join(f'{c:.6e} * x^{i}' for i, c in enumerate(coef[::-1]))
            print(f"  {case_labels[case]}: y = {poly_str}")

            plt.scatter(sizes, times, color=colors[case], label=case_labels[case])
            plt.plot(sizes, predicted_times, linestyle='--', color=colors[case])

    plt.title(f'Производительность алгоритма {algorithm.replace("_", " ").capitalize()}')
    plt.xlabel('Размер входных данных')
    plt.ylabel('Время (с)')
    plt.legend()
    plt.grid(True)
    plt.show()
