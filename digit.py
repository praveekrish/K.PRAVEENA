# your code goes here
def Counting(number):
Count = 0
while(number > 0):
number = number // 10 
Count = Count + 1
print("\n number of digit number = %d" %Count)
Counting(1234)
