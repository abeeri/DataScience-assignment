name = input("Enter your name: ") 
salary = float(input("Enter your monthly salary: ")) 
expenses = float(input("Enter your monthly expenses: ")) 
 
remaining = salary - expenses 
 
print("\n----- Monthly Report -----") 
print("Name:", name) 
print("Salary:", salary) 
print("Expenses:", expenses) 
print("Remaining Amount:", remaining) 
 
if remaining > 2000: 
    print("Excellent! You are saving a good amount.") 
elif remaining > 0: 
    print("Good. You still have some money left.") 
else: 
    print("Warning! Your expenses are higher than your salary.") 
