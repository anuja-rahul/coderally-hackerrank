

def bioHazards(n, allergic, poisonous):
    all_bacteria = [b for b in range(1, n+1)]
    universal_sample = all_possible_outcomes(all_bacteria)
    exclude = []
    for i in range(len(allergic)):
        current_set = [allergic[i], poisonous[i]]
        exclude.append(current_set)
    # print(universal_sample)
    # print(len(universal_sample))

    test_list = []

    for items in universal_sample:
        if items in exclude:
            test_list.append(items)

    for data in universal_sample:
        for item in exclude:
            # print(f"data: {data}, item: {item}, result: {item[0] not in data and item[1] not in data}")
            if item[0] in data and item[1] in data:
                test_list.append(data)

    temp = []
    for item in universal_sample:
        if item not in test_list:
            temp.append(item)

    print(len(temp))


def all_possible_outcomes(data_list):
    subsets = []
    for i in range(len(data_list)):
        for j in range(i + 1, len(data_list) + 1):
            subset = data_list[i:j]
            subsets.append(subset)
    return subsets


def filter_list(data_list, matching_str):
    return [item for item in data_list if matching_str not in item]


bioHazards(4, [1, 2], [3, 4])
