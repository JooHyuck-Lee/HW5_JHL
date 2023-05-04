#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv

def main():
    f1 = open('q2.csv')
    data = csv.reader(f1)
    header = next(data)

    maxDiffDay = ""
    maxDiffTemp = -999
    minDiffDay = ""
    minDiffTemp = 999

    for row in data:
        for i in range(-2, 0):
            if row[i] == "":
                row[i] = "empty"
            else:
                row[i] = float(row[i])
        if row[-1] != "empty" and row[-2] != "empty":
            if row[-1] - row[-2] > maxDiffTemp:
                maxDiffDay = row[0]
                maxDiffTemp = row[-1] - row[-2]
            if row[-1] - row[-2] < minDiffTemp:
                minDiffDay = row[0]
                minDiffTemp = row[-1] - row[-2]


    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperature Variation: %s"%(maxDiffDay))
    print("Maximum Tempterature Difference: %.1f Celcius"%(maxDiffTemp))
    print("Day with the Smallest Temperature Variation: %s"%(minDiffDay))
    print("Minimum Tempterature Difference: %.1f Celcius"%(minDiffTemp))

    f1.close()
    
    
    
if __name__ == "__main__":
    main()


# In[ ]:




