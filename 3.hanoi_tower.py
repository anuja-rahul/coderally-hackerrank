import math


def is_a_perfect_square(number):
    square_root = int(math.sqrt(number))
    return square_root * square_root == number


def hanoi_tower(N):

    pegs = [[] for _ in range(N)]  # Initialize N empty pegs
    count = 0  # Total number of balls placed
    value = 1  # Start with the first ball

    seen_states = set()  # To detect cycles

    while True:
        state = tuple(tuple(peg) for peg in pegs)  # Create a hashable state representation
        if state in seen_states:
            return -1  # Infinite loop detected
        seen_states.add(state)

        placed = False

        for i in range(N):
            # If peg is empty, place the ball directly
            if not pegs[i]:
                pegs[i].append(value)
                count += 1
                value += 1
                placed = True
                break
            # Check if the sum with the last ball on the peg is a perfect square
            elif is_a_perfect_square(pegs[i][-1] + value):
                pegs[i].append(value)
                count += 1
                value += 1
                placed = True
                break

        # If no ball was placed after trying all pegs, stop the loop
        if not placed:
            break

    return count


T = int(input().strip())
final_list = []
for i in range(T):
    N = int(input().strip())
    result = hanoi_tower(N)
    final_list.append(result)

for item in final_list:
    print(item)
