def main():
    import csv
    f = open('2022_Seoul_Temp.csv', 'r', encoding='cp949')
    data = csv.reader(f)
    header = next(data)
    header = next(data)
    header = next(data)
    header = next(data)
    header = next(data)
    header = next(data)
    header = next(data)
    header = next(data)

    sumMx = 0
    sumMn = 0
    sumMean = 0
    i = 0
    for row in data:
        if (len(row) == 5):
            if(row[0] == '' or row[1] == '' or row[2]=='' or row[3]=='' or row[4]==''):
                continue

            i = i + 1
            sumMean = sumMean + float(row[2])
            sumMn = sumMn + float(row[3])
            sumMx = sumMx + float(row[4])
  

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print()
    print("Average Temperature: {:.2f} Celsius".format(sumMean/i))
    print()
    print("Average Temperature: {:.2f} Celsius".format(sumMn/i))
    print()
    print("Average Temperature: {:.2f} Celsius".format(sumMx/i))

    f.close()

if __name__ =="__main__":
    main()