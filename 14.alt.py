def ferry_loading(ferry_len, car_len):
    car_order = []
    right_len = ferry_len

    car_order.append("port")
    left_len = ferry_len - car_len[0]
    for i in range(1, len(car_len) - 1):
        if left_len > right_len:
            if car_len[i] < left_len:
                left_len -= car_len[i]
                car_order.append("port")
        else:
            if car_len[i] < right_len:
                right_len -= car_len[i]
                car_order.append("starboard")

    return len(car_order), car_order


T = int(input().strip())
input()

for _ in range(T):
    l = int(input().strip())
    ferry_len = l * 100

    car_len = []
    while True:
        car = int(input().strip())
        if car == 0:
            break
        car_len.append(car)

    length, array = ferry_loading(ferry_len, car_len)

    print(length)
    for char in array:
        print(char)

    if _ != T - 1:
        print()