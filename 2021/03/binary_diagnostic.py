from collections import Counter

file = open('input.txt')


def binary_to_decimal(binary):
    return int(binary, 2)


def split_binary_vertically(arr):
    result = list()
    binary_dict = dict()

    for index, binary in enumerate(arr):
        binary_dict[index] = list(binary)

    for binary in list(zip(*binary_dict.values())):
        result.append(''.join(binary))

    return result


def common_binary(arr):
    most_common = ''

    for binary in arr:
        binary_counter = Counter(binary)
        most_common += max(binary_counter, key=binary_counter.get)

    return most_common


def least_common_binary(arr):
    least_common = ''

    for binary in arr:
        binary_counter = Counter(binary)
        least_common += '1' if max(binary_counter, key=binary_counter.get) == '0' else '0'

    return least_common


if __name__ == '__main__':
    binary_list = split_binary_vertically(file)
    most_common = common_binary(binary_list)
    least_common = least_common_binary(binary_list)
    most_common_decimal = binary_to_decimal(most_common)
    least_common_decimal = binary_to_decimal(least_common)
    print('results', most_common_decimal * least_common_decimal)

file.close()
