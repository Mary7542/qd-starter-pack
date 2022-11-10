#Write a software that verifies if a number is present in a pre-defined array.
#Output example:
#Insert number 3
#The number 3 is [not] present in the array.

i=0
N=[3,4,5,1,2,6,7,9,13,0]

x=int(input("Insert a number: ")) 

while (i<10): 
    if x==N[i]: 
        print("We found it! The number is in the "+str(i)+" position.")
        print(N)
        break
    else: 
        i+=1
        if i==10: 
            print("Sorry, the number isn't in the array.")
        



