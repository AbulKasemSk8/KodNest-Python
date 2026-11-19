#write you code here
percentage = int(input("Enter percentage:"))
activebacklog = int(input("Enter no. of backlogs: "))

if percentage >=60 and activebacklog == 0:
    print("Egligible to apply for placement drive!")
else:
    print("ineglibile")