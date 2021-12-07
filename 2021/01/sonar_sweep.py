from functools import reduce

file = open('input.txt')


def parse_values(values):
    return list(map(int, values))


def sum_3d_values(values):
    return list(map(lambda x: sum(x), values))


def convert_to_3d(arr):
    output = []

    for index, value in enumerate(arr):
        if index + 2 < len(arr):
            output.append([value, arr[index + 1], arr[index + 2]])

    return output


def count_increases(arr):
    def fn(acc, curr):
        index = curr[0]
        num = curr[1]

        # Stop looping if reached arr length
        if index + 1 == len(arr):
            return acc

        if arr[index + 1] > num:
            acc += 1

        return acc

    return reduce(fn, enumerate(arr), 0)


if __name__ == '__main__':
    parsed_values = parse_values(file)
    three_dimensions_values = convert_to_3d(parsed_values)
    sum_values = sum_3d_values(three_dimensions_values)
    increases = count_increases(sum_values)
    print('increases', increases)

file.close()
