file = open('input.txt')


def parse_value(val):
    return int(val)


def split_values(values):
    def fn(string):
        split_value = string.split()
        key = split_value[0]
        numeric_value = parse_value(split_value[1])
        return [key, numeric_value]

    return list(map(fn, values))


def count_increase(arr):
    horizontalPosition = 0
    depth = 0
    aim = 0

    for item in arr:
        step = item[0]
        value = item[1]

        if step == 'down':
            aim += value

        if step == 'up':
            aim -= value

        if step == 'forward':
            horizontalPosition += value
            depth = (aim * value) + depth

    return horizontalPosition * depth


if __name__ == '__main__':
    values = split_values(file)
    result = count_increase(values)
    print('results', result)

file.close()
