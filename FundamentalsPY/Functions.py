import math      # INCLUDE A LIBRARY

#FORMAT TO 2 DIGITS IN FLOAT NUMBER
a = 1.5446532454
print(f"a = {a:.2f}")

#ROUND TO UPPER INT
a = math.ceil(a)
print(a)

# ASCII TABLE MANIPULATE CHAR TO INT AND INT TO CHAR
print(f"Print char from ASCII table - {chr(97)}")
a = "a"
print(f"Print number from char in ASCII table - {ord(a)}")

# LOOP THROUGH LIST 1
my_list = ["dog", "cat", "fish"]
for element in my_list:
    print(element, end=" ")
print()
# LOOP TROUGH LIST 2
my_list = ["dog", "cat", "fish"]
for index in range(len(my_list)):
    print(my_list[index], end=" ")
print()
# LIST COMPREHANTION HARD METHOD // FIND A WORD IN A LIST OF STRINGS
new_list = ["baba e gotina", "desi e gotina", "dqdo e gotin", "tin e gotin"]
word = "desi"
print(list(string for string in new_list if word in string))











