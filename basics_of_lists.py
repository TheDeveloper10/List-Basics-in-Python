'''
If you are a developer who wants to learn Python and has learned another language before
than this script will help you a lot!

The aim of this script is to show in the shortest way possible the basics of lists in Python.
It shows all of their functionalities. It also aims to make the learning processes easier.

If you're going to use this script to learn the lists in Python I suggest you:
1. Compile it and look in the result
2. Read it line by line
3. Clone it and experiment by yourself


Note: The list here consists of strings and most of the methods
for lists work for both numeric/string lists.
'''

# Creating a list
courses = ['Math', 'Physics', 'Programming', 'Chemistry', 'Art']

# Printing the size of a list
print(len(courses))
print('\n\n')

# Indices
print(courses[0]) # Prints first element
print(courses[-1]) # Prints last element
print(courses) # Prints all elements
print('\n\n')

# Slicing
print(courses[0:3]) # Prints (Math, Physics, Programming)
print(courses[:3]) # Prints exactly the same as 0:3 (Math, Physics, Programming)
print(courses[1:3]) # Prints (Physics, Programming)
print(courses[2:]) # Prints everything after second element
print('\n\n')

# Sorting/Reversing a list
courses.sort() # sorts the list in ascending order
print(courses)
courses.sort(reverse=True) # sorts the list in descending order
print(courses)
courses.reverse() # reverses the list
print(courses)
sorted_courses = sorted(courses) # Sorts the input array and returns it. *Doesn't affect the input array*
print(sorted_courses)
print('\n\n')

# Appending/Inserting/Removing element from a list
courses.append('Biology') # Appends 'Biology' in the end of the list
print(courses)
courses.insert(1, 'Python') # Inserts 'Python' in the between first and second element
print(courses)
courses.remove('Chemistry') # Removes 'Chemistry' from the list
print(courses)
print('\n\n')

# Extending a list (inserting another list)
new_courses = ['C++', 'C#', 'Java']
courses.extend(new_courses) # Extends the list with another list(appends each element from the input array to the other one)
print(courses)

'''
You can also use courses.append(new_courses) or courses.insert(2, new_courses) to append/insert a list to another list
but the result will NOT look like this:
['Art', 'Python', 'Math', 'Physics', 'Programming', 'Biology', 'C++', 'C#', 'Java']
It will look like this:
['Art', 'Python', 'Math', 'Physics', 'Programming', 'Biology', ['C++', 'C#', 'Java']]
It inserts/appends the list as a value not as multiple values.
'''
print('\n\n')

# Basic functionalities
print(min(courses)) # Prints the minimum element of the list(in this case: 'Art', it is based on the alphabet)
print(max(courses)) # Prints the maximum element of the list(in this case: Python, it is based on the alphabet)
print('\n\n')

# Numeric Lists
int_list = [10, 3, 72, 81, 5, 6, 101]
print(min(int_list)) # Prints the minimum element of the list(in this case: 3)
print(max(int_list)) # Prints the maximum element of the list(in this case: 101)
print(sum(int_list)) # Prints the sum of all elements in a list(works for numeric lists only!)




'''
▁▂▅▆▇ 📲 Social Media and Contacts -> Follow me for more cool stuff 📲 ▇▆▅▂▁
	🚀 GitHub:     https://github.com/TheDeveloper10
	📒 Instagram:  https://www.instagram.com/thedeveloper10/
	💎 Twitter:    https://twitter.com/the_developer10
	📌 YouTube:    https://www.youtube.com/channel/UCwO0k5dccZrTW6-GmJsiFrg
	📘 Facebook:   https://www.facebook.com/VicTor-372230180173180
	🚵 LinkedIn:   https://www.linkedin.com/company/65346254
	➡ Website:    https://thedevelopers.tech/
'''
