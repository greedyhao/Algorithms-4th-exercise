def main():
    info = input()
    info_split = info.split()
    num = round((float)(info_split[1])/(float)(info_split[2]),3)
    info_split.append(num)
    print(info_split)

main()
