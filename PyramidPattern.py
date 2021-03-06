#Patterns can be printed in python using simple for loops. First outer loop is used to handle number of rows and Inner nested loop is used to handle the number
#of columns. Manipulating the print statements, different number patterns, alphabet patterns or star patterns can be printed.

n=int(input("Enter a number:"))
for i in range(n):
  #for printing space 
    for j in range(n-i-1):
        print(" ", end=" ")
   #for printing stars
    for k in range(2*i+1):
        print("*", end=" ")
    print()
    
 #Another Approach: 
#Using List in Python 3, this could be done in a simpler way
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	myList = []
	for i in range(1,n+1):
		myList.append("*"*i)
	print("\n".join(myList))

# Driver Code
n = 5
pypart(n)

