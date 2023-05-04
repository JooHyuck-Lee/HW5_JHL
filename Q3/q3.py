#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

def main():
    f2 = open('q3.csv')
    data = csv.reader(f2)
    header = next(data)
    
    linetype = ["1호선", "2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선", "9호선"]
    linelist = []
    numlist = []
    count = -1
    for row in data:
        
        if row[-3] == "":
            row[-3] = "empty"
        else:
            row[-3] = int(row[-3])
        if not(row[1] in linelist) and (row[1] in linetype):
            count += 1
            linelist.append(row[1])
            numlist.append(0)
            if row[-3] != "empty":
                numlist[count] += row[-3]
        elif (row[1] in linetype):
            if row[-3] != "empty":
                numlist[count] += row[-3]

    print("*** Subway Report for Seoul on March 2023 ***")
    print("1st Busiest Line: %s (%d)"%(linelist[numlist.index(max(numlist))], max(numlist)))
    linelist.pop(numlist.index(max(numlist)))
    numlist.pop(numlist.index(max(numlist)))
    print("2nd Busiest Line: %s (%d)"%(linelist[numlist.index(max(numlist))], max(numlist)))
    linelist.pop(numlist.index(max(numlist)))
    numlist.pop(numlist.index(max(numlist)))
    print("1st Least Used Line: %s (%d)"%(linelist[numlist.index(min(numlist))], min(numlist)))
    linelist.pop(numlist.index(min(numlist)))
    numlist.pop(numlist.index(min(numlist)))
    print("2nd Least Used Line: %s (%d)"%(linelist[numlist.index(min(numlist))], min(numlist)))
    linelist.pop(numlist.index(min(numlist)))
    numlist.pop(numlist.index(min(numlist)))
          
    f2.close()



if __name__ == "__main__":
    main()


# In[ ]:




