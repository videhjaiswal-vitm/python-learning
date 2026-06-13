'''
A Sequence is an ordered collection of items where each element is associated with a specific integer index.
Types of Built-in Sequences
1.List
2.Tuple
3.String
4.Range()
=============
List:It is a sequence which is used to store bulk amount of hetergenous(different type of data) data which is given by integer index from 0 to n-1 where n is length of list.
Note:It is mutable(changable) in nature.
Syntax:
In C,
int arrname[5] = {10,20,30,40,50}
===========
In Python,
listname = [e1,e2,........en]
'''
stud_marks = [45,56,67,78,98]
#+ve index     0  1  2  3  4 
#-ve index    -5 -4 -3 -2 -1          
print(stud_marks)
print("Datatype is:",type(stud_marks))
print("============")

#Length of a stud_marks
print("Length of a stud_marks:",len(stud_marks))
print("============")

#access single data
print("stud_marks[2]:",stud_marks[2])
print("stud_marks[-2]:",stud_marks[-2])
print("============")

#access all data with +ve index
#range(5):0 1 2 3 4
for index in range(len(stud_marks)):
    print("Index:",index,"Marks:",stud_marks[index])
print("============")

#access all data with -ve index
#                 (-4,0)
for index in range(-(len(stud_marks)),0):
    print("Index:",index,"Marks:",stud_marks[index])
print("============")

#access all data without index
for data in stud_marks:
    print(data)
print("==========")

#find max and min in list
stud_marks=[67,34,89,78,56,33]
max=stud_marks[0] #67
min=stud_marks[0] #67
for index in range(len(stud_marks)):
    #  67<89
    #  89<33
    if max<stud_marks[index]:
        max=stud_marks[index] #89
    #  67>34 
    #  34>33   
    elif min>stud_marks[index]:
        min=stud_marks[index] #33
print("Maximum is:",max,"Minimum is:",min)

print("=========")

'''
Sorting:Arrange list elements in ascending or descending order.
'''
stud_marks=[67,34,89,78,56,33]
for a in range(len(stud_marks)):
    for b in range(a+1,len(stud_marks)):
       #67>34
       #[34,67,89,78,56,33]
       #34>33
       #[33,67,89,78,56,34]
       #First Iteration
       #67>56
       #[33,56,89,78,67,34]
       #56>34
       #[33,34,89,78,67,56]
       #Second Iteration
       #89>78
       #[33,34,78,89,67,56]
       #78>67
       #[33,34,67,89,78,56]
       #67>56
       #[33,34,56,89,78,67]
       #Third Iteration
       #89>78
       #[33,34,56,78,89,67]
       #78>67
       #[33,34,56,67,89,78]
       #Fourth Iteration
       #89>78
       #[33,34,56,67,78,89]
       if stud_marks[a]<stud_marks[b]:
          temp=stud_marks[a]
          stud_marks[a]=stud_marks[b]
          stud_marks[b]=temp 
print(stud_marks)
print("==================") 

cricket_player=["Kapil Dev","Sachin Tendulkar","M.S Dhoni","Virat Kohli"]

for index in range(len(cricket_player)):
    print("Index:",index,"Player:",cricket_player[index])
print("==================") 

#add a new player
cricket_player.append("Rohit Sharma")
cricket_player.append("K.L Rahul")
for index in range(len(cricket_player)):
    print("Index:",index,"Player:",cricket_player[index])
print("==================") 

#add a player at particular position
cricket_player.insert(1,"Virendra Shewag")
for index in range(len(cricket_player)):
    print("Index:",index,"Player:",cricket_player[index])
print("==================") 

#remove a player 
cricket_player.remove("Virendra Shewag")
for index in range(len(cricket_player)):
    print("Index:",index,"Player:",cricket_player[index])
print("==================") 

#remove a last player
player_name=cricket_player.pop()
print(player_name)
for index in range(len(cricket_player)):
    print("Index:",index,"Player:",cricket_player[index])
print("==================") 

#remove a player at particular index
player_name = cricket_player.pop(2)
print(player_name)
for index in range(len(cricket_player)):
    print("Index:",index,"Player:",cricket_player[index])
print("==================") 

#update a player
cricket_player[2]="K.L Rahul"
for index in range(len(cricket_player)):
    print("Index:",index,"Player:",cricket_player[index])
print("==================") 



















