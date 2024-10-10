number = int(input("Enter a number: "))
odd_numbers = [num for num in range(1, number) if num % 2 != 0]
even_numbers = [num for num in range(1, number) if num % 2 == 0]
print(f"Odd numbers: {odd_numbers}")
print(f"Even numbers: {even_numbers}")

fruits = ["apple", "banana", "cherry", "orange"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(f"Capitalized fruits: {capitalized_fruits}")