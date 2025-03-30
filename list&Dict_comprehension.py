import random
no=[1,2,3]
new_list=[n+1 for n in no]
print(new_list)

name="Abhirup"
list=[letters for letters in name]
print(list)

list1=[n*2 for n in range(1,5)]
print(list1)

names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
short_names=[n for n in names if len(n)<5]
cap_names=[x.upper() for x in names if len(x)>5]
print(short_names)
print(cap_names)

new_dict={x:random.randint(1,100) for x in names}
print(new_dict)

dict={student:score for (student,score) in new_dict.items() if score>=60}
print(dict)

student_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}

#Looping through dictionaries:

for (key,value) in student_dict.items():
    print(value)
    
import pandas

student_data_frame=pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
for (index,row) in student_data_frame.iterrows():
    if row.student =="Angela":
        print(row.score)