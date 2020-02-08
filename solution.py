import os


def main():

    for name in os.listdir('input_data'):
        input_file = [int(x) for x in open("./input_data/{}".format(name)).read().split()]
        length_slices = input_file[:2]
        slices = input_file[2:]

        arr_of_indexes = [str(x) for x in alghoritm(slices, length_slices)]

        output_file = open("./output_data/{}".format(name), 'w')

        output_file.write(str(len(arr_of_indexes)))
        output_file.write('\n')
        output_file.write(' '.join(arr_of_indexes))


def alghoritm(slices, length_slices):
    best_sum = 0
    best_arr_of_indexes = []
    j, i = length_slices[1] - 1, length_slices[1] - 1
    while i >= 0:
        j = i
        arr_of_indexes = []
        sum = 0
        while j >= 0:
            temp = slices[j]
            if sum + temp < length_slices[0]:
                sum += temp
                arr_of_indexes.append(j)
            elif sum + temp == length_slices[0]:
                sum += temp
                arr_of_indexes.append(j)
                break
            j -= 1
        if best_sum < sum:
            best_sum = sum
            best_arr_of_indexes = arr_of_indexes
        if best_sum == length_slices[0]:
            break
        i -= 1
    return best_arr_of_indexes[::-1]


if __name__ == '__main__':
    main()
