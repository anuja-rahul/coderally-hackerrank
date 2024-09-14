import math

test_cases = int(input().strip())

for case in range(test_cases):
    num_of_pegs = int(input().strip())


def is_a_perfect_square(number):
    square_root = int(math.sqrt(number))
    return square_root * square_root == number


def hanoi_tower(n):
    pegs = [[] for _ in range(n)]
    count = 0
    value = 1

    seen_states = set()  # To detect cycles

    while True:
        state = tuple(tuple(peg) for peg in pegs)
        if state in seen_states:
            return -1
        seen_states.add(state)

        placed = False

        for i in range(n):

            if not pegs[i]:
                pegs[i].append(value)
                count += 1
                value += 1
                placed = True
                break

            elif is_a_perfect_square(pegs[i][-1] + value):
                pegs[i].append(value)
                count += 1
                value += 1
                placed = True
                break

        if not placed:
            break

    return count


for pegs_num in range(1, num_of_pegs + 1):
    print(hanoi_tower(pegs_num))
