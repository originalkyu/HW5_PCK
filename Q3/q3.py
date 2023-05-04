def main():
    import csv
    f = open('202303_Seoul_Subway.csv', 'r', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data)


    dic = {}

# row[1] 호선
# row[4] 승차객수 
    for row in data:
        if row[1] in dic:
            dic[row[1]] = dic[row[1]] + int(row[4])+int(row[5])
        else:
            dic[row[1]] = int(row[4]) + int(row[5])

    newList = sorted(dic.items(), key = lambda x: x[1])

    print("*** Subway Report for Seoul on March 2023 ***")
    print()
    print("1st Busiest Line: Line {} ({})".format(newList[len(newList)-1][0], newList[len(newList)-1][1]))
    print()
    print("2nd Busiest Line: Line {} ({})".format(newList[len(newList)-2][0], newList[len(newList)-2][1]))
    print()
    print("1st Least used Line: Line {} ({})".format(newList[0][0], newList[0][1]))
    print()
    print("2nd Least used Line: Line {} ({})".format(newList[1][0], newList[1][1]))
    print()
 
    f.close()

if __name__ =="__main__":
    main()