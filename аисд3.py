import time
import random

# Функция линейного поиска
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Функция бинарного поиска
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Функция тернарного поиска
def ternary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        third1 = low + (high - low) // 3
        third2 = high - (high - low) // 3
        if arr[third1] == x:
            return third1
        if arr[third2] == x:
            return third2
        if x < arr[third1]:
            high = third1 - 1
        elif x > arr[third2]:
            low = third2 + 1
        else:
            low = third1 + 1
            high = third2 - 1
    return -1

# Функция экспоненциального поиска
def exponential_search(arr, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= x:
        i *= 2
    return binary_search(arr[:min(i, len(arr))], x)

# Функция для измерения времени выполнения
def measure_time(func, arr, x):
    start_time = time.perf_counter()
    func(arr, x)
    return time.perf_counter() - start_time

# Функция для генерации массива
def generate_array(size):
    return sorted(random.sample(range(size * 10), size))

# Функция для выполнения измерений
def perform_measurements():
    sizes = [10000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    algorithms = {
        'linear_search': linear_search,
        'binary_search': binary_search,
        'ternary_search': ternary_search,
        'exponential_search': exponential_search
    }
    results = []
    num_iterations = 50

    for size in sizes:
        arr = generate_array(size)

        for algorithm_name, algorithm in algorithms.items():
            if algorithm_name == 'linear_search':
                best_case = arr[0]
                worst_case = arr[-1]
                average_case = arr[size // 2]
            elif algorithm_name == 'binary_search':
                best_case = arr[size // 2]
                worst_case = arr[-1]
                average_case = arr[size // 4]
            elif algorithm_name == 'ternary_search':
                best_case = arr[size // 3]
                worst_case = arr[-1]
                average_case = arr[size // 2]
            elif algorithm_name == 'exponential_search':
                best_case = arr[0]
                worst_case = arr[-1]
                average_case = arr[size // 2]

            best_times = [measure_time(algorithm, arr, best_case) for _ in range(num_iterations)]
            worst_times = [measure_time(algorithm, arr, worst_case) for _ in range(num_iterations)]
            average_times = [measure_time(algorithm, arr, average_case) for _ in range(num_iterations)]

            best_time_avg = sum(best_times) / num_iterations
            worst_time_avg = sum(worst_times) / num_iterations
            average_time_avg = sum(average_times) / num_iterations

            results.append((size, algorithm_name, 'best', best_time_avg))
            results.append((size, algorithm_name, 'worst', worst_time_avg))
            results.append((size, algorithm_name, 'average', average_time_avg))

    return results

# Функция для записи результатов в файл
def write_results_to_file(results, filename='results.txt'):
    with open(filename, 'w') as file:
        for result in results:
            file.write(f"Size: {result[0]}, Algorithm: {result[1]}, Case: {result[2]}, Time: {result[3]:.6e}\n")

# Основная функция
def main():
    results = perform_measurements()
    write_results_to_file(results)

if __name__ == "__main__":
    main()
