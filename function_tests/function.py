
import sys

print(sys.version)



lower_bound= int(input("Enter lower range: "))
upper_bound = int(input("Enter upper range: "))

print("Prime numbers between range",lower_bound,"and",upper_bound,"are:")

for num in range(lower_bound,upper_bound + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

#count(num)