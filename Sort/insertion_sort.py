from typing import List


def insertion_sort(input_list: List[int]):
    """
    Сортировка вставкой: на каждой итерации i для элемента input_list[i]
    выбирается место для вставки в массив input_list[0..i-1]

    :param input_list:
    :return:
    """
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j -= 1

        input_list[j + 1] = key

    return input_list


if __name__ == "__main__":
    print(insertion_sort([1, 3, 5, 2]))
    print(insertion_sort([5, 2, 4, 6, 1, 3]))
