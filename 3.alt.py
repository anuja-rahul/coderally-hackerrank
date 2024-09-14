import math


def is_a_perfect_square(number):
    square_root = int(math.sqrt(number))
    return square_root * square_root == number


def hanoi_tower(N):
    pegs = [[] for _ in range(N)]
    count = 0
    value = 1

    seen_states = set()

    while True:
        state = tuple(tuple(peg) for peg in pegs)
        if state in seen_states:
            return -1
        seen_states.add(state)

        placed = False

        for i in range(N):
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


# Read the number of test cases
import sys

# input = sys.stdin.read
data = input().strip().split()

T = int(data[0])

results = []
for i in range(1, T + 1):
    N = int(data[i])
    results.append(hanoi_tower(N))

# Output the results for each test case
for result in results:
    print(result)