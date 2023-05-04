#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

def main():
    f1 = open('2022_Seoul_Temp.csv')
    data = csv.reader(f1)
    header = next(data)

    days = 0
    avgTempSum = 0.0
    lowTempSum = 0.0
    highTempSum = 0.0

    for row in data:
        days += 1
        for i in range(-3, 0):
            if row[i] == "":
                row[i] = "empty"
            else:
                row[i] = float(row[i])
                if i == -3:
                    avgTempSum += row[i]
                elif i == -2:
                    lowTempSum += row[i]
                elif i == -1:
                    highTempSum += row[i]

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: %.2f Celcius"%(round((avgTempSum / days),2)))
    print("Average Minimum Temperature: %.2f Celcius"%(round((lowTempSum / days),2)))
    print("Average Maximum Temperature: %.2f Celcius"%(round((highTempSum / days),2)))

    f1.close()
    
    


if __name__ == "__main__":
    main()




# In[ ]:




