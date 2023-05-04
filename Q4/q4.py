def main():
    import csv
    f = open('202303_Seoul_Subway.csv', 'r', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data)


    Mx1 = 0
    Mx1L = ""
    Mn1 = 99999999
    Mn1L = ""
    Mx2 = 0
    Mx2L = ""
    Mn2 = 99999999
    Mn2L = ""
    Mx3 = 0
    Mx3L = ""
    Mn3 = 99999999
    Mn3L = ""
    Mx4 = 0
    Mx4L = ""
    Mn4 = 99999999
    Mn4L = ""

# row[1] 호선
# row[4] 승차객수 
    for row in data:
        if row[1]=="1호선":
            if int(row[4]) > Mx1:
                Mx1L = row[3]
                Mx1 = int(row[4])
            if int(row[4]) < Mn1:
                Mn1L = row[3]
                Mn1 = int(row[4])
        if row[1]=="2호선":
            if int(row[4]) > Mx2:
                Mx2L = row[3]
                Mx2 = int(row[4])
            if int(row[4]) < Mn2:
                Mn2L = row[3]
                Mn2 = int(row[4])
        if row[1]=="3호선":
            if int(row[4]) > Mx3:
                Mx3L = row[3]
                Mx3 = int(row[4])
            if int(row[4]) < Mn3:
                Mn3L = row[3]
                Mn3 = int(row[4])
        if row[1]=="4호선":
            if int(row[4]) > Mx4:
                Mx4L = row[3]
                Mx4 = int(row[4])
            if int(row[4]) < Mn4:
                Mn4L = row[3]
                Mn4 = int(row[4])
            

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