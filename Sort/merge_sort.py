def merge(input_list, n, p, q):
    """
    Функция производит слияние двух подмассивов: input_list[n:p] и input_list[p:q]

    :param input_list:
    :param n: начало
    :param p: разделитель
    :param q: конец
    :return:
    """
    right = input_list[n:p]
    left = input_list[p:q]

    i = 0
    j = 0

    for k in range(n, q):
        if i == len(right):
            input_list[k:q] = left[j:]
            return
        elif j == len(left):
            input_list[k:q] = right[i:]
            return

        if right[i] < left[j]:
            input_list[k] = right[i]
            i += 1
        else:
            input_list[k] = left[j]
            j += 1


def merge_sort(input_list, start: int = 0, end: int = None):
    """
    Сортировка слиянием: рекурсивно разделяет массив на два подмассива пока длина подмассива > 1,
    после чего производит процесс слияния двух подмассивов

    :param input_list:
    :param start:
    :param end:
    :return:
    """
    end = end or len(input_list)

    if start < end - 1:
        separator = (start + end) // 2
        merge_sort(input_list, start, separator)
        merge_sort(input_list, separator, end)
        merge(input_list, start, separator, end)
    return input_list


if __name__ == "__main__":
    test_list = [5, 2, 4, 6, 1]
    print(merge_sort(test_list))
