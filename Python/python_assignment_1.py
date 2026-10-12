# ----1. String Concatenation----

string_1 = "Hello "

string_2 = input("Enter your Name: ")

string_3 = ", welcome to Python programming"

output = string_1 + string_2 + string_3

print(output)


# 2. String Slicing and Indexing:

print(output[0])  # First character
print(output[-1])  # Last character
print(output[:5])  # First 5 characters
print(output[-11:])  # Last 11 characters
print(output[::-1])  # Reversed string
print(output[28:34])  # Python


# # 3. String Methods:

strM = "Python beginner tutorial"
print(strM.upper())  # Convert to uppercase
print(strM.lower())  # Convert to lowercase
print(strM.title())  # Convert to title case
print(strM.count("t"))  # Count occurrences of 't'
print(strM.replace('Python', 'Machine Learning'))  # Replace 'Python' with 'Machine Learning'

#Tuples (Creation, Modification and Access) :

a = (10,20,30)
b = (40,50,60)

t_combine = a + b

print(t_combine) 
print(t_combine*3) 
print(t_combine[2])  
print(t_combine[:3]) 
print(t_combine[-3:]) 

