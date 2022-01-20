# Assignment2
Name=input(f"Enter Name : ")
Age=int(input(f"Enter Age : "))
Qualification=input(f"Enter Qualification : ")
Address=input(f"Enter Address : ")
Salary=int(input(f"Enter Salary : "))
Family=int(input(f"Enter number of family members : "))

about=[Name,Age,Qualification,Address,Salary,Family]

for details in about:
  print(details,end="--")