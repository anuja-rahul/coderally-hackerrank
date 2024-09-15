from itertools import zip_longest

if __name__ == '__main__':
    case = int(input().strip())
    input()

    def check_ferry(cases):
        for _ in range(cases):
            ferry_length = int(input().strip())
            car_list = []

            while True:
                car_length = int(input().strip())
                if car_length == 0:
                    break
                else:
                    car_list.append(car_length / 100)

            ferry_left_length = ferry_length
            ferry_right_length = ferry_length
            ferry_right = []  # Starboard
            ferry_left = []  # Port
            car_len = 0
            for i in range(len(car_list)):
                car_len += car_list[i]
                print(car_len, ferry_length*2)
                if car_len > ferry_length * 2:
                    break
                if ferry_right_length + ferry_right_length >= 0:
                    if ferry_right_length <= ferry_left_length:
                        ferry_left.append("port")
                        ferry_left_length -= float(car_list[i])
                    elif ferry_left_length <= ferry_right_length:
                        ferry_right.append("starboard")
                        ferry_right_length -= float(car_list[i])

            print(len(ferry_left) + len(ferry_right))
            zipped = zip_longest(ferry_left, ferry_right, fillvalue=None)

            for port, starboard in zipped:
                if starboard is None:
                    pass
                else:
                    print(starboard)
                if port is None:
                    pass
                else:
                    print(port)

            print("")

    check_ferry(case)
