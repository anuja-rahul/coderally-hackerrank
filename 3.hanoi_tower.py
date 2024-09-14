import math

test_cases = int(input().strip())

peg_record = {}


def check_squares(num):
    return int(math.sqrt(num)) ** 2 == num


for case in range(test_cases):
    crashed = False
    current_ball = 1
    next_ball = None
    peg_record[case] = {}
    num_of_pegs = int(input().strip())
    for peg in range(1, num_of_pegs + 1):
        peg_record[case][peg] = [0]
        if current_ball == 1:
            peg_record[case][peg].append(current_ball)

        while not crashed:
            if check_squares(current_ball):
                crashed = True

        current_ball += 1


print(peg_record)



