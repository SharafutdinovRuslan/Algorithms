# Напишите функцию сравнения двух номеров версий программы. Номер версии — это строка, содержащая цифры и точки.
# Примеры:
#
# version_cmp("2.0", "1.0"); // -> 1
# version_cmp("1.0", "2.0"); // -> -1
# version_cmp("1.0", "1.0"); // -> 0
#
# Предполагаем, что номера версий состоят только из цифр и точек и всегда валидны.
#
# Уточнение 1: Версия "1.10" новее, чем "1.1".
# Уточнение 2. Версия может иметь вид “1.12.123" и т.п.
# Уточнение 3. “1.1” и “1.1.0” — это две разные записи одной и той же версии.

def version_cmp(left_version: str, right_version: str) -> int:
    left_versions_list = left_version.split(".")
    right_versions_list = right_version.split(".")
    min_len = min(len(left_versions_list), len(right_versions_list))

    for i in range(min_len):
        if int(left_versions_list[i]) > int(right_versions_list[i]):
            return 1
        elif int(left_versions_list[i]) < int(right_versions_list[i]):
            return -1

    if len(left_versions_list) == len(right_versions_list):
        return 0
    elif len(left_versions_list) > len(right_versions_list):
        if int(left_versions_list[min_len]) > 0:
            return 1
        else:
            return 0
    else:
        if int(right_versions_list[min_len]) > 0:
            return -1
        else:
            return 0


print(version_cmp("2.0", "1.0") == 1)
print(version_cmp("1.0", "2.0") == -1)
print(version_cmp("1.0", "1.0") == 0)
print(version_cmp("1", "1.0") == 0)
# print(version_cmp("1.", "1.0") == 0)
print(version_cmp("123.0.10", "123.0") == 1)
print(version_cmp("123.0.0", "123.0") == 0)
print(version_cmp("1.0.10", "1.0.10") == 0)
print(version_cmp("1.0.11", "1.0.11") == 0)
print(version_cmp("1.0.1", "1.0.11") == -1)
