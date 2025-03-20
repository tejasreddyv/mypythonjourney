#Understanding Lists In Python
Family=["Tejas Reddy v","Venkatashiva Reddy","Archana Dt",14,48,42,"Respectively"]
#Now I Will Replace The Respectively With Just Empty Space
Family[6]="   "
#Used Indexing Of Lists To Replace An Element With Other
print(Family)
#List Slicing
Numbers=[77,99,66,67,69,60]
print(Numbers[3:6])#90 to 60 # Same Rules As Str Slicing
print(Numbers[-5: ])#Negitive Slicing
#Functions Of List 
List=([24,234,797,477,666])
List.append(777)#Appends(ADDS)Your desired element to the list
List.sort()#SORTS IN ASCENDING ORDER
print(List)
List.sort(reverse=True)#SORTS IN DESCENDING ORDER
print(List)
List.insert(2,999)#Replaces a index
List.remove(777)#Removes A Element's First Occurance
List.pop(4)#Removes The Number At The Index Specified
print(List)
#Using Tuple Functions To Find Out Number Of Persons Who Ordered Dosa
inp=(str(input("Please Enter The Orders Reiceved Today:-")))
print(str(inp.count("Dosa")))
#Question using Lists To Store Top 3 Movies Of User In A List(Practice Problem:-1)
Maggie=[]
mv1=input("PLEASE ENTER THE FIRST MOVIE:-")
mv2=input("PLEASE ENTER THE SECOND MOVIE:-")
mv3=input("PLEASE ENTER THE THIRD MOVIE:-")
Maggie.append(mv1)
Maggie.append(mv2)
Maggie.append(mv3)
print(Maggie)
#Writing A Program To Check If A List Has A Palindrome To Avoid Errors (Example Not As An Actual)(Problem 2)
Palin=["AB,BA,BA,AB"]
New_Palin=Palin.copy()
New_Palin.reverse()
if(New_Palin==Palin):
    print("YOU CAN CONTINUE")
else:
    print("Sorry An Error Occured Return And Try Again But This Time Try To Avoid Palindromes")
#Finding No Of Students With Grade A (Problem 3)
Lichu=["A","B","B","A","A","C","F","F"]
print(Lichu.count("A"))
#Thanks For Having A Look At My Code