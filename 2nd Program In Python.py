#The Unnecessary Part Have Been Skipped (Basics Like Addding String Are Already Done previously)
#Now I Am Learning How Do We Know The Length Of A String?
Example="Hey This Is A String"
print(len(Example))#20 (Spaces Are Included In This)
#Indexing in Python Can Be Reffered To Assigining Numbers To your String(Or Position In Complex terms) For Eg:-
Buisness="I Am A Programmer"
print(Buisness[12])#Output=a
#Indexing Is A Process By Which You Can Acesses Part Of A String For Eg:-
print(Buisness[3: ]) 
#Escpecially In Python There Is Negitive Index+Slicing Which Start From the Opposite Direction Meaning s=-1 and B=-8
print(Buisness[-7:-1])#gramme
#functions of string
Naanu="human with A Brain That too A Big Brain"
print(Naanu.endswith("an"))#Endswith Function ( Know Wether Your value Ends With Specific Lettter Or Not (Boolean))
print(Naanu.capitalize())#capitalize Your Word (Made For Guys Like Me)
print(Naanu.replace("k","n"))#replacing Words / letters in a string
print(Naanu.find("B"))# Find The index Of The First Occurance of the Number(Why Tf Do They Use This?)
print(Naanu.count("Brain"))#Counting How Many Times You have used that word  These Were Some Examples But there are more
#Practicing Questions ( Dont Ask Me Why Am I Doing this In the Middle Of code Instead of End)
Naam=input("Please Enter Your Name:-")#length Of Name
print(len(Naam))
#2 Finding The Occurance Of Dollar 
Paisa="Here Comes the Money$$$$$$$$$$$$"
print(Paisa.count("$"))
Name="Tejas Reddy"#If Conditional Statement
if(Name=="Tejas Reddy"):
    print("SUPER")
Father="Venkata Shiva Reddy"#Use Of The Elif Conditional Statement
if(Father=="Archana Dt"):
    print("It's A Lie")
elif(Father=="Venkata Shiva Reddy"):
    print("Appa Nin Super")#this statement is printed in the terminal
#Use Of Else Statement
Hesaru="Archana Dt"
if(Hesaru=="Tejas Reddy V"):
    print("Nin Archana Alla")
else:
    print("Archana Mam Yelli Idare")
#PRACTICE QUESTIONS (#1)
Marks=int(input("What Is Your Marks:-"))
if(Marks>=90):
    Marks="A"
elif(Marks>=80 and Marks<90):
    Marks="B"
elif(Marks>=70 and Marks<80):
    Marks="C"
else:
    Marks="F"
print(("Dear Student Your Grade Is:-",Marks))
#Nesting(Adding A Conditional Statement In A Conditional Statement)
Age=int(input("What Is Your Age:-"))
if(int(Age>=18)):
    if(int(Age>=80)):
        print("You Are A Grandfather")
    else:
      print("Congrats! You Are An Adult,Now Enjoy The Pain")
else:
    print("ENJOY! You are still a kid")
#Practice problems
Num=int(input("Please Enter Your Number:-"))
remainder=Num % 2
if(remainder==0):
    print("Your Given Number is Even")
else:
    print("Your Given Number is ODD")
#Practice Problem 2
NumA=int(input("Please Enter the First Number:-"))
NumB=int(input("Please Enter the Second Number:-"))
NumC=int(input("Please Enter the Third Number:-"))
if(NumA>=NumB and NumA>=NumC):
    print("The Largest Number Is:-",NumA)
elif(NumB>=NumA and NumB>=NumC):
    print("The Largest Number Is :-",NumB)
elif(NumC>=NumA and NumC>=NumB):
    print("The Largest Number Is :-",NumC)
#Practice Problem 3
Num7=int(input("Please Enter Your Number:-"))
if(Num7%7==0):
    print("Your Number is Divisible By 7")
else:
    print("Your Number Is Not Divisible by 7")

