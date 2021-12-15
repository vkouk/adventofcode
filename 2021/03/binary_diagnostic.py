from collections import Counter

with open('input.txt') as file:
    data = [x for x in file.read().split()]


def binary_to_int(binary):
    return int(binary, 2)


def find_o2(arr):
    index = 0
    while len(arr) > 1:
        zeros = list()
        ones = list()

        for item in range(0, len(arr)):
            if arr[item][index] == '0':
                zeros.append(arr[item])
            else:
                ones.append(arr[item])

        if len(zeros) > len(ones):
            arr = zeros
        else:
            arr = ones

        index += 1

    return arr.pop()


def find_co2(arr):
    index = 0
    while len(arr) > 1:
        zeros = list()
        ones = list()
        for item in range(0, len(arr)):
            if arr[item][index] == '0':
                zeros.append(arr[item])
            else:
                ones.append(arr[item])

        if len(ones) < len(zeros):
            arr = ones
        else:
            arr = zeros

        index += 1

    return arr.pop()


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
    o2 = binary_to_int(find_o2(data.copy()))
    co2 = binary_to_int(find_co2(data.copy()))
    result = o2 * co2

    print('results', result)

file.close()
