# Example input() statement
s = input('Please enter a string: ')
s = s[::2]

# i = 0
# while i < len(s):
#     print(s[i].upper())
#     i += 2

for char in s:
    print(char.upper())