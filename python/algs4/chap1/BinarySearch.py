from RNFF import read_num_from_file


def rank(key, list):
    lo = 0
    hi = len(list) - 1
    while lo <= hi:
        mid = int((lo + hi) / 2)
        if key < list[mid]:
            hi = mid - 1
        elif key > list[mid]:
            lo = mid + 1
        else:
            return mid
    return False


with open(".../largeW.txt", "r") as src_file:
    with open(".../largeT.txt", "r") as cmp_file:
        src_list = read_num_from_file(src_file)
        cmp_list = read_num_from_file(cmp_file)
        src_list.sort()
        cmp_list.sort()
        printed = []

        for cmp_num in cmp_list:
            # if cmp_num not in src_list:
            #     print(cmp_num)
            # if cmp_num not in printed:
            if not rank(cmp_num, src_list):
                # printed.append(cmp_num)
                print(cmp_num)
