def main():
    import csv
    f = open('202303_Seoul_Subway.csv', 'r', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data)


    Mx1 = 0
    Mx1L = ""
    Mn1 = 999999999
    Mn1L = ""
    Mx2 = 0
    Mx2L = ""
    Mn2 = 999999999
    Mn2L = ""
    Mx3 = 0
    Mx3L = ""
    Mn3 = 999999999
    Mn3L = ""
    Mx4 = 0
    Mx4L = ""
    Mn4 = 999999999
    Mn4L = ""

# row[1] 호선
# row[4] 승차객수 
    for row in data:
        num = int(row[4]) + int(row[5])
        if row[1]=="1호선":
            if num > Mx1:
                Mx1L = row[3]
                Mx1 = num
            if num < Mn1:
                Mn1L = row[3]
                Mn1 = num
        if row[1]=="2호선":
            if num > Mx2:
                Mx2L = row[3]
                Mx2 = num
            if num < Mn2:
                Mn2L = row[3]
                Mn2 = num
        if row[1]=="3호선":
            if num > Mx3:
                Mx3L = row[3]
                Mx3 = num
            if num < Mn3:
                Mn3L = row[3]
                Mn3 = num
        if row[1]=="4호선":
            if num > Mx4:
                Mx4L = row[3]
                Mx4 = num
            if num < Mn4:
                Mn4L = row[3]
                Mn4 = num
            

    print("*** Subway Report for Seoul on March 2023 ***")
    print()
    print("Line 1:")
    print("Busiest Station: {} ({})".format(Mx1L, Mx1))
    print("Least used Station: {} ({})".format(Mn1L, Mn1))
    print()
    print("Line 2:")
    print("Busiest Station: {} ({})".format(Mx2L, Mx2))
    print("Least used Station: {} ({})".format(Mn2L, Mn2))
    print()
    print("Line 3:")
    print("Busiest Station: {} ({})".format(Mx3L, Mx3))
    print("Least used Station: {} ({})".format(Mn3L, Mn3))
    print()
    print("Line 4:")
    print("Busiest Station: {} ({})".format(Mx4L, Mx4))
    print("Least used Station: {} ({})".format(Mn4L, Mn4))
    print()
 
    f.close()

if __name__ =="__main__":
    main()