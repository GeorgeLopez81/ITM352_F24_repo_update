# My variables
age = int(input("Enter your age: "))    
is_tuesday = input("Is it Tuesday? (yes/no): ").lower() == 'yes'  
is_matinee = input("Is it a matinee? (yes/no): ").lower() == 'yes'  

# normal price
price = 14

#conditions 
if is_matinee:
    
    if age >= 65:
        price = 5  
    else:
        price = 8  
elif age >= 65:
    
    price = 8
elif is_tuesday:
    
    price = 10


print(f"Age: {age}, Tuesday: {is_tuesday}, Matinee: {is_matinee}")
print(f"Movie price: ${price}")
