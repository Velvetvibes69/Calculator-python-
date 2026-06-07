def add(P,Q):
    #This function is used to add 2 numbers
    return P+Q
def subract(P,Q):
    #This function is used to subract 2 numbers
    return P-Q
def multiply(P,Q):
    #This function is used to multiply 2 numbers
    return P*Q
def divide(P,Q);
    #This function is used for dividing 2 numbers
    return P/Q

#Now we will take input from the user
print("Please seclect the operetion:") 
print("a. Add")
print("b. Subract")
print("c. Multiply")
print("d. Divide")
 
choice = input("Please enter choice (a/b/c/d/): ")

num_1= int(input("Please enter the first number: "))
num_2= int(input("Please enter the second number: "))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", subract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("Invalid input")