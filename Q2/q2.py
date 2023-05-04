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

    Mx = -100000
    MxDay = ""
    Mn = 100000
    MnDay = ""

    i = 0
    for row in data:
        if (len(row) == 5):
            if(row[0] == '' or row[1] == '' or row[2]=='' or row[3]=='' or row[4]==''):
                continue

            i = i + 1
            newval = float(row[4]) - float(row[3])
            if(newval > Mx):
                Mx = newval
                MxDay = row[0]
            if(newval < Mn):
                Mn = newval
                MnDay = row[0]
  
    MxDay.strip()
    MnDay.strip()
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print()
    print("Day with the Largest Temperature Variation:", MxDay.strip())
    print()
    print("Maximum Temperature Difference: {:.1f} Celsius".format(Mx))
    print()
    print("Day with the Smallest Temperature Variation:", MnDay.strip())
    print()
    print("Minimum Temperature Difference: {:.1f} Celsius".format(Mn))

    f.close()

if __name__ =="__main__":
    main()