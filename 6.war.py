people_list = {"friends": [], "enemies": []}


def setFriends(x, y):
    current_set = [x, y]
    if current_set not in people_list["friends"] and current_set not in people_list["enemies"]:
        people_list["friends"].append(current_set)

        for items in people_list["friends"]:
            for sample in people_list["friends"]:
                if items[0] in sample[0]:
                    people_list["friends"].append([items[1], sample[1]])
                elif items[1] in sample[1]:
                    people_list["friends"].append([items[0], sample[0]])
                elif items[0] == sample[1]:
                    people_list["friends"].append([items[1], sample[0]])
                elif items[1] == sample[0]:
                    people_list["friends"].append([items[0], sample[1]])

    elif current_set in people_list["enemies"]:
        return -1


def setEnemies(x, y):
    current_set = [x, y]
    if current_set not in people_list["friends"] and current_set not in people_list["enemies"]:
        people_list["enemies"].append(current_set)
    elif current_set in people_list["friends"]:
        return -1


def areFriends(x, y):
    pass


def areEnemies(x, y):
    pass


def main():
    num_of_people = int(input().strip())

    while True:
        data = input().strip()

        if int(data) == 0:
            break

        c = int(data[0])
        x = int(data[1])
        y = int(data[2])

        if c == 1:
            setFriends(x, y)
        elif c == 2:
            setEnemies(x, y)
        elif c == 3:
            areFriends(x, y)
        elif c == 4:
            areEnemies(x, y)

        print(f"C: {c}, X: {x}, Y: {y}")


if __name__ == '__main__':
    main()

# TODO: Fix this
