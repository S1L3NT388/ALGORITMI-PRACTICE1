import random


def generate_random_array(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


def count_and_sum_even_in_range(arr, start, end):
    count = 0
    total = 0
    for i in range(start, end + 1):
        if arr[i] % 2 == 0:
            count += 1
            total += arr[i]
    return count, total


def average_and_count_above_average(arr):
    average = sum(arr) / len(arr) if arr else 0
    count = sum(1 for value in arr if value > average)
    return average, count


def pairwise_sum(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Масиви повинні мати однакову довжину")
    return [a + b for a, b in zip(arr1, arr2)]


def concatenate(arr1, arr2):
    return arr1 + arr2


def swap_max_and_min(arr):

    if not arr:
        return arr
    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))
    arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
    return arr


def split_positive_negative(arr):
    positive = [x for x in arr if x > 0]
    negative = [x for x in arr if x < 0]
    return positive, negative


def remove_max_min_duplicates(arr):
    if not arr:
        return arr

    max_value = max(arr)
    min_value = min(arr)

    result = []
    max_added = False
    min_added = False

    for value in arr:
        if max_value == min_value:
            if not max_added:
                result.append(value)
                max_added = True
        elif value == max_value:
            if not max_added:
                result.append(value)
                max_added = True
        elif value == min_value:
            if not min_added:
                result.append(value)
                min_added = True
        else:
            result.append(value)

    return result


def elements_between_averages(arr1, arr2):
    avg1 = sum(arr1) / len(arr1) if arr1 else 0
    avg2 = sum(arr2) / len(arr2) if arr2 else 0
    low, high = min(avg1, avg2), max(avg1, avg2)

    result = [x for x in arr1 if low <= x <= high]
    result += [x for x in arr2 if low <= x <= high]

    return avg1, avg2, result


def main():
    arr = generate_random_array(10, -20, 20)
    print(f"Вихідний масив = {arr}\n")

    count, total = count_and_sum_even_in_range(arr, 2, 7)
    print(f"Завдання 1: кількість парних елементів у діапазоні [2..7] = {count}, сума = {total}\n")

    average, count_above = average_and_count_above_average(arr)
    print(f"Завдання 2: середнє арифметичне = {average:.2f}, "
          f"кількість елементів більших за середнє = {count_above}\n")

    a3a = generate_random_array(6, 1, 10)
    a3b = generate_random_array(6, 1, 10)
    print(f"Завдання 3: масив A = {a3a}")
    print(f"Завдання 3: масив B = {a3b}")
    print(f"Завдання 3: попарна сума = {pairwise_sum(a3a, a3b)}\n")

    a4a = generate_random_array(4, 1, 10)
    a4b = generate_random_array(7, 1, 10)
    print(f"Завдання 4: масив A = {a4a}")
    print(f"Завдання 4: масив B = {a4b}")
    print(f"Завдання 4: конкатенація = {concatenate(a4a, a4b)}\n")

    a5 = generate_random_array(8, -10, 10)
    print(f"Завдання 5: до обміну = {a5}")
    swap_max_and_min(a5)
    print(f"Завдання 5: після обміну max та min = {a5}\n")

    a6 = generate_random_array(10, -10, 10)
    print(f"Завдання 6: вихідний масив = {a6}")
    positive, negative = split_positive_negative(a6)
    print(f"Завдання 6: додатні елементи = {positive}")
    print(f"Завдання 6: від'ємні елементи = {negative}\n")

    a7 = [3, 9, 1, 9, 5, 1, 9, 2, 1]
    print(f"Завдання 7: вихідний масив = {a7}")
    print(f"Завдання 7: без дублікатів max/min = {remove_max_min_duplicates(a7)}\n")

    a8a = generate_random_array(6, 1, 20)
    a8b = generate_random_array(6, 1, 20)
    avg1, avg2, result8 = elements_between_averages(a8a, a8b)
    print(f"Завдання 8: масив A = {a8a}")
    print(f"Завдання 8: масив B = {a8b}")
    print(f"Завдання 8: середнє1 = {avg1:.2f}, середнє2 = {avg2:.2f}")
    print(f"Завдання 8: елементи в межах середніх = {result8}")


if __name__ == "__main__":
    main()