from typing import List


def read_data():
    left_side = []
    right_side = []
    with open('input.txt', 'r') as file:
        for line in file:
            columns = line.strip().split()
            if len(columns) == 2:
                left_side.append(int(columns[0]))
                right_side.append(int(columns[1]))

    # Get sum of distance
    total_distance = calculate_distance(left_side, right_side)
    print(f'The total distance is: {total_distance}')


def calculate_distance(left_list: List[int], right_list: List[int]) -> int:
    distance = 0

    while left_list and right_list:
        smallest_left = min(left_list)
        smallest_right = min(right_list)

        if smallest_left > smallest_right:
            difference = smallest_left - smallest_right
        else:
            difference = smallest_right - smallest_left
        distance += difference

        left_list.remove(smallest_left)
        right_list.remove(smallest_right)

    return distance


read_data()
