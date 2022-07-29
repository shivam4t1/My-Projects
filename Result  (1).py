students_roll = [1,2,3,4,5,6,7,8,9,10]
students_marks = {1:84 , 2:76 , 3:98 , 4:72 , 5:87 , 6:93 , 7:81 , 8:65 , 9:73 , 10:88}

while True:
    roll = int(input("\n Enter your Roll no  :- "))
    
    if roll in students_roll:
        print("\nWelcome ")
        pass
        break
    else: 
        print("\nUnregistered User !!!")

a = roll
c = students_marks[a]

max_marks = max(students_marks.values())
min_marks = min(students_marks.values())

while True:
     b = int(input("\nWhat do you wanna check ? \n1 = Highest marks in your class \n2 = Lowest marks in your class\n3 =Your marks \n4 = Exit \n"))
     
     if b == 3:
        print("\nYour marks is : ",c)
     elif b == 1:
        print("\nHighest Marks in your class is :  ",max_marks)
     elif b == 2:
        print("\nLowest marks in you class is : ",min_marks)
     elif b == 4:
         break
     else:
         print("\nInvalid operation")
        
