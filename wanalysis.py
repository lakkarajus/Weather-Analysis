'''
# -*- coding: utf-8 -*-
# Author rao Lakkaraju     07-19-2023
# Read the Dupage weather file (data collected at Ohare Airport) 
# input file is comma separated value (csv) file 
# The Climate data file is downloaded from NOAA (National center for Environmental Info.

# 1. Read the file
# 2. Clean the data
# 3. The cleaned csv data file is used for processing
# 4. From the first data line extract Station name where the data is collected
# 5. From the second line Extract Month and temparature 
# 6. Check the temparature for characters and remove them and convert to integer
# 7. Read all the records in the file and Collect temparatures for each month.
# 8. Process for the maximum and min temps for all the months.
# 9. Finish and plot the values.

'''

import matplotlib.pyplot as plt
import pandas as pd
import csv

def char_check (chars):
# This function strips all characters from string chars(numbers)    
   
    if not chars.isdecimal() :
        chars = chars.strip('abcdefghijklmnopqrstuvwxyz')
        chars = chars.strip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        chars = chars.strip('"')
    return chars      

######    Record Count in a file
def count_records(filename):
    with open(filename, 'r') as file:
        count = sum(1 for _ in file)
    return count    

####### The file cleaning functionsare created by ChatGpt
def has_blank_or_null_values(record):
    return any(value == '' or value is None for value in record.values())

def eliminate_blank_and_null_records(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        header = reader.fieldnames
        data = list(reader)

    filtered_data = [record for record in data if not has_blank_or_null_values(record)]

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(filtered_data)

def plot_graphs (station_name,year,months,maxtemps,mintemps) :
    # Make Plots
    # First Plot
    year = str(year)
    print (' Year = ',year)
    plt.plot(months,maxtemps,'ro--',lw=1,label='Max Temps')
    plt.plot(months,mintemps,'bo--',lw=1,label='Min Temps')
    
    plt.title(Station_name)
    plt.xlabel('Monthly temparatures in year '+ year)
    plt.ylabel('Temparature in F')
    plt.text(2,-10,'Monthly Temps for the year '+ year,size=10,color='m')
    plt.legend(loc=2,fontsize="small")
    plt.axis([-1,13,-20,100])
#    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13],['JAN','FEB','MAR','APR','MAY','JUN',
#    'JUL','AUG','SEP','OCT','NOV','DEC',' '])
    plt.yticks([-10,0,10,20,30,40,50,60,70,80,90,100,110])
    plt.show()

    # Second Plot
    plt.bar(months,maxtemps,color='r',label='Max Temp')
    plt.bar(months,mintemps,color='b',label='Min Temp')
    plt.plot(months,maxtemps,'ro--',linewidth=2.0)
    plt.plot(months,mintemps,'bo--',linewidth=2.0)

    plt.title(Station_name)
    plt.xlabel('Monthly temparatures in year '+ year)
    plt.ylabel('Temparature in F')
    plt.text(1,-10,' Monthly Temps for the year ' + year,size=10,color='m')
    plt.legend(loc=2,fontsize="small")
    plt.axis([-1,13,-10,110])
#    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13],[' ','JAN','FEB','MAR','APR','MAY','JUN',
#    'JUL','AUG','SEP','OCT','NOV','DEC',' '])
    plt.yticks([-20,-10,0,10,20,30,40,50,60,70,80,90,100])
    plt.show()

    return


# ********* Program Starts **********

# Initialize arrays 
temps,tempavgs,tempmaxs,tempmins,months,maxtemps,mintemps = [],[],[],[],[],[],[]
tempdates, maxdates, mindates = [],[],[]
monthsa = []
monthsalpha = ['JAN','FEB','MAR','APR','MAY','JUN',
'JUL','AUG','SEP','OCT','NOV','DEC']
total_records = 0 

# Processing the Weather data csv file obtained from NOAA.

#my_file = open('ohare2017B.csv','r')
#my_file = 'ohare2022.csv'
#my_file = 'dallas2022.csv'
#my_file = 'ohare2023.csv'
my_file = 'seattle2022.csv'

input_file =  my_file         
print('my-file = ',my_file)
output_file = 'cleaned_file.csv'
eliminate_blank_and_null_records(input_file, output_file)    

record_count = count_records(my_file)
print('\n','Input file',my_file,'has',record_count,'records')
filename = 'cleaned_file.csv' 
record_count = count_records(filename)
print(f"After Cleaning the file '{filename}' has {record_count} records.")      



# Read the first line in the file which is the table header
# Extract Station ID and Station Name 
my_file = open('cleaned_file.csv','r')  # start processing the cleaned file

header = my_file.readline()
print('\n','header = ',header)

h = header.split(',')
h = [item.strip('"') for item in h]
print('header line = ', h)    

# Read the first data line and extract Station name, Month, Day and date 
line1 = my_file.readline() # Read the first data line
print('First data line = ', line1)

line1 = line1.strip('"\n')
x = line1.split(',')
x = [item . strip('"') for item in x]

Station_name = x[1]+x[2]
dt =  x[3].split('-')  
year = dt[0]
month = dt[1]
date = dt[2] 
print ('year= ', year,'month= ',month,'date = ',date)

oldmonth = month

# Change temp value to integer and store the temperature

if not x[4] == ' ' or x[4] is None :
    print('x[4] = ', x[4], 'x[5] = ',x[5],'x[6] = ', x[6])
    tempavg = x[4]
    tempmax = x[5]
    tempmin = x[6]



    tempavg = char_check(tempavg) 
    tempmax = char_check(tempmax) 
    tempmin = char_check(tempmin) 


    tempavg = int(tempavg)
    tempmax = int(tempmax)
    tempmin = tempmin.strip('"\n')
    tempmin = int(tempmin)


    tempavgs.append(tempavg)
    tempmaxs.append(tempmax)
    tempmins.append(tempmin)
    tempdates.append(date)
    
else :
    print('\n','\n','\n')
    print('Weather analysis for the year ', year)
    print('Station ID =  ',x[0],'\nStation Name = ',x[1],x[2])

# Read the input file line by line
index = -1
for lines in my_file:
    lines = lines.strip('"\n')
    
    
    x = lines.split(',')
    x = [item . strip('"') for item in x]
    
    dt = x[3].split('-')  
    year  = dt[0]
    month = dt[1]
    date  = dt[2]
    
    tempavg = x[4]
    tempmax = x[5]
    tempmin = x[6]
    if not x[4] == '  ' or None :    
        tempavg = int(tempavg)
        tempmax = int(tempmax)
        tempmin = int(tempmin)
    else :   
        tempavg = int(tempavg)
        tempmax = int(tempmax)
        tempmin = int(tempmin)
    
    
    
  
    if month == oldmonth : # accumulate temparatures for the month
       
       tempavgs.append(tempavg) 
       tempmaxs.append(tempmax)
       tempmins.append(tempmin)
       tempdates.append(date)
      
    else:
        
       months.append(oldmonth) # calculate the max and min temperatures for the month 
  
       print('\nmonths = ',months)
       print('temp Avg = ', tempavgs) 
       print('temp Max = ', tempmaxs)
       print('temp Min = ', tempmins)
       print('temp dat = ', tempdates)
       print('max dates + ',maxdates)
       
       oldmonth = month
       maxtemps.append(max(tempmaxs))    # Find Max temparature for the month and append
       mintemps.append(min(tempmins))    # Find Min temparature for the month and append
       maxdates.append(tempdates[tempmaxs.index(max(tempmaxs))])
       mindates.append(tempdates[tempmins.index(min(tempmins))])
     
       print('max temps = ', maxtemps)
       print('maxdates = ', maxdates)
       print('min temps = ', mintemps)
       print('min dates = ', mindates)
     
       
       
       #  Initilize temperatures arrays for a new month
       tempavgs,tempmaxs,tempmins = [],[],[]
       
       tempavgs.append(tempavg) 
       tempmaxs.append(tempmax)
       tempmins.append(tempmin)
       tempdates.append(date)
            
    index = index + 1
    
my_file.close()

# file is processed. Append the final month's data 
total_records = index + 2
print ('Total Records in the file = ', total_records,'\n')    

months.append(oldmonth)  
maxtemps.append(max(tempmaxs))
mintemps.append(min(tempmins))    
maxdates.append(tempdates[tempmaxs.index(max(tempmaxs))])
mindates.append(tempdates[tempmins.index(min(tempmins))])

for item in months:
    monthsa.append(monthsalpha[int(item)-1])
 
monthsalpha = monthsa    
print('tempdates = ', tempdates)
print('months = ',months)
print('Months = ', months)
print('Monthsalpha = ', monthsalpha)
print ('\nMax Temperatures = ', maxtemps)
print ('Max Temp Dates = ', maxdates)
print('\nMin Temparatures = ',mintemps)
print ('Min Temp Dates = ', mindates)

i = 0
print('\n   Date & Time  ', 'Max & Min Temps')

for each_month in months:
    datetime1 = year + monthsalpha[i] + maxdates[i]
    datetime2 = year + monthsalpha[i] + mindates[i]
    print(str(i+1).rjust(2),datetime1,'--',maxtemps[i],',',
    str(mintemps[i]).rjust(3),datetime2)
    i =i + 1
    
#   Plot Graphs
plot_graphs (Station_name,year,months,maxtemps,mintemps)
bin_edges = ([10,80,100])

# Third Plot from a Data Frame ---- creat a data frame from a table Dictionary
weather_data ={
   'Month' : monthsalpha,
   'Max_Temp' : maxtemps,
   'DateMax' : maxdates,
   'Min_Temp' : mintemps,
   'DateMin' : mindates}
df = pd.DataFrame(weather_data)

# Arrange the columns in the way you want
df = pd.DataFrame(weather_data,columns=['Month','Max_Temp','DateMax','Min_Temp','DateMin'])
df=df.set_index('Month')
#df.plot()

print('\n',df)
ax=df.plot()
ax.set_title(Station_name)
ax.set_xlabel('Monthly temparatures in year '+ year)
ax.set_ylabel('Teperature in F')
plt.bar(monthsalpha,maxtemps)

df = df.T  # Transpose Index
print('\n',df)

print('End of the Program')

