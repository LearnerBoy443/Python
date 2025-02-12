#with open("weather_data.csv") as data_file:
#    data=data_file.readline()
#    print(data)


#    import csv 

#   with open("weather_data.csv") as data_file:
#        data=csv.reader(data_file)
#        print(data)
#       temperatures=[]
#        for row in data:
#       if row[1] !="temp":
#           temperatures.append(row[1])
        # print(row)
#    print(temperatures)

import pandas

data=pandas.read_csv("weather_data.csv")
print(data) 
print(data["temp"])   #particular coloumn is called a series and the whole rows and coloumns is dataframe

data_dict=data.to_dict() #list to dictionary conversion

print(data_dict)

series=data["temp"].to_list() #series to list 
print(series)
#total_temp=0
#for temp in series:
#    total_temp+=int(temp)
#avg_temp=total_temp/int(len(series))
#print(avg_temp)

total=sum(series)#sum of all integer in list
print(total)

avg_temp=total/len(series)

print(avg_temp)

print(data["temp"].mean()) #directly find mean

print(data["temp"].max())


#data from coloums
print(data["condition"])
print(data.condition)

#data from rows
print(data[data.day=="Monday"])

print(data[data.temp==data.temp.max()])
      
      
      
      
      
      
      
      
      
      
      