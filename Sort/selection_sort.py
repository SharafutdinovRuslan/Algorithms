from typing import List


def selection_sort(input_list: List[int]):
    for i in range(len(input_list) - 1):
        min_value = input_list[i]
        min_position = i
        for j in range(i + 1, len(input_list)):
            if input_list[j] < min_value:
                min_value = input_list[j]
                min_position = j

        input_list[i], input_list[min_position] = min_value, input_list[i]

    return input_list


if __name__ == "__main__":
    print(selection_sort([1, 3, 5, 2]))
    print(selection_sort([5, 2, 4, 6, 1, 3]))
