# # ---List (Creation, Modification and Access)----
# # 1. List Creation:

# age_list = [24, 25, 26, 27, 28]

# name_list = ['keerthana', 'shakeera', 'archana',"sakthi", 'arun']

# print(name_list)

# # 2. List Operations / Modifications:

# name_list.append('Yazhini')
# print(name_list)

# age_list.insert(2, 30)
# print(age_list)

# name_list.remove('Yazhini')
# print(name_list)

# age_list.pop()
# print(age_list)

# age_list.extend([29, 30, 26])
# print(age_list)

# age_list.sort(reverse=True)
# print(age_list)


# print(max(age_list))  # Maximum age
# print(min(age_list))  # Minimum age
# print(sum(age_list))  # Sum of ages

# # 3. Accessing List Elements:
# print(name_list[0])  # First name   
# print(name_list[-1])  # Last name
# print(name_list[2:5])  # Names from index 2 to 4
# print(name_list[::-1])  # Names in reverse order

# #Dictionary (Creation, Modification and Access):

# student_marks = {
#     "keerthana": 85,        
#     "shakeera": 90,
#     "archana": 95,
#     "sakthi": 80,
#     "arun": 88}

# print(student_marks['keerthana'])

# student_marks['Janani'] = 80  

# print(student_marks)

# student_marks['sakthi'] = 99

# print(student_marks.keys())  # Get all keys
# print(student_marks.values())  # Get all values 
# print(student_marks.items())  # Get all key-value pairs
 
# #Sets (Operations):
# # {}
# # set()


# my_set = set(['a','e','i','o','u','a','a','i'])

# print(my_set)  

# try:
#     my_set[4] = 's'  
# except TypeError as e:
#     print("Error:", e)


# set1 = {1, 3, 5, 7, 9}
# set2 = {2, 3, 5, 8, 10}


# print(set1 | set2)       
# print(set1 & set2) 

# print(set1.union(set2))
# print(set1.intersection(set2))


# 1. Prompt the user for input

score = float(input("Enter your score (0 to 10): "))

if score < 0 or score > 10 :
    print("Invalid score! Please enter a value between 0 and 10.")
elif score > 7:
    print("Above Average: Excellent work! Keep up the great performance.")
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve your performance, consistent practice will lead to better results.")