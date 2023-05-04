#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv

def main():
    f2 = open('q4.csv')
    data = csv.reader(f2)
    header = next(data)
    
    linelist = []
    busylist = []
    busystationlist = []
    leastlist = []
    leaststationlist = []
    count = -1
    
    for row in data:
        if not(row[1] in linelist) and (len(linelist) == 4):
            break
        for i in range(-3, -1):
            if row[i] == "":
                row[i] = "empty"
            else:
                row[i] = int(row[i])
        if not(row[1] in linelist):
            count += 1
            linelist.append(row[1])
            busylist.append(0)
            busystationlist.append("")
            leastlist.append(10000000)
            leaststationlist.append("")
            if row[-3] != "empty" and row[-2] != "empty":
                if busylist[count] < (row[-3] + row[-2]):
                    busylist[count] = row[-3] + row[-2]
                    busystationlist[count] = row[-4]
                if leastlist[count] > (row[-3] + row[-2]):
                    leastlist[count] = row[-3] + row[-2]
                    leaststationlist[count] = row[-4]
        else:
            if row[-3] != "empty" and row[-2] != "empty":
                if busylist[count] < (row[-3] + row[-2]):
                    busylist[count] = row[-3] + row[-2]
                    busystationlist[count] = row[-4]
                if leastlist[count] > (row[-3] + row[-2]):
                    leastlist[count] = row[-3] + row[-2]
                    leaststationlist[count] = row[-4]
    
    print("*** Subway Report for Seoul on March 2023***")
    for i in range(0, 4):
        print("Line %d"%(i+1))
        print("Busiest Station: %s (%d)"%(busystationlist[i], busylist[i]))
        print("Least Used Station: %s (%d)\n"%(leaststationlist[i], leastlist[i]))
    
    f2.close()



if __name__ == "__main__":
    main()


# In[ ]:




