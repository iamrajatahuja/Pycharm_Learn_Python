# RegEx - re module is present in python
import re
from re import match

#re.search(regex-pattern,string)
# returns match object if found else return None

message = "The current Python version is 3.13.563 Other previous version are 3.12,3.11,3.10"

match_obj = re.search("13",message)
print(match_obj)
print(message[32:34])

#meta characters []

match_obj = re.search("[0-9][0-9][012345]",message)
print(match_obj)

# . (wildcard) matches any character except new line character\n
match_obj = re.search("[0-9].[0-9][012345]",message) #Here . is any character
print(match_obj)


match_obj = re.search("[0-9][.][0-9]",message) #Here . is exact match .
print(match_obj)

# r"" - raw string , in which escape sequences are ignored and treated as normal char
# [A-Z][a-z]

s1 = "P\nyt hon is \n a Programming language.com 9898989 ph-1234567890, ph-9876543212452323 current Version is python3.13 ok"
pat = r"[a-z][a-z]"
match_obj = re.search(pat, s1)
print(match_obj)

# \d and \D
# \d is one digit character
# \D is one non-digit character

pat = r"[a-z][a-z]\d"
match_obj = re.search(pat, s1)
print(match_obj)

pat = r"[a-z][a-z]\D"
match_obj = re.search(pat, s1)
print(match_obj)

# \s and \S
# \s matches \n,\t,\s any space character

pat = r"[a-z]\s"
match_obj = re.search(pat, s1)
print(match_obj)

# \S exactly opposite of \s
pat = r"[a-z][a-z]\S"
match_obj = re.search(pat, s1)
print(match_obj)

# \w matches [a-z], [A-Z], _(underscore) and [0-9]
pat = r"\w[a-z][a-z]"
match_obj = re.search(pat, s1)
print(match_obj)

# \W matches opposite of \w

#Quantifiers +,*,?,{n}

# {n}
pat = r"[A-Z][a-z]{4}"
match_obj = re.search(pat, s1)
print(match_obj)

pat = r"[a-z]{3,8}"
match_obj = re.search(pat, s1)  #matches min 3 small chars or max 8 small chars
print(match_obj)

# + -> matches 1 or more previous characters
pat = r"[a-z]+"
match_obj = re.search(pat, s1)

# ? -> matches 0 or 1 previous character
pat = r"[A-Z][a-z]?"
match_obj = re.search(pat, s1)
print(match_obj)

# * -> matches 0 or more previous character
pat = r"[A-Z][a-z]*"
match_obj = re.search(pat, s1)
print(match_obj)

# ^ caret -> matches beginning of previous character
pat = r"^[a-z]{3}"
match_obj = re.search(pat, s1)
print(match_obj)

# $ dollar -> matches last of previous character
pat = r"[a-z]{2}$"
match_obj = re.search(pat, s1)
print(match_obj)

# () grouping - exact match
pat = r"(com)"
match_obj = re.search(pat, s1)
print(match_obj)

pat = r"[com]" #any character match c or o or m
match_obj = re.search(pat, s1)
print(match_obj)

# | or character
pat = r"(hel|com)"
match_obj = re.search(pat, s1)
print(match_obj)


#######################################

# match() function checks in the beginning

pat = r"[a-z]{3}"
match_obj = re.match(pat, s1)
print(match_obj)

# findall() gives a list all matched patterns

pat = r"[0-9]{10,}" #10 or more digits
match_obj = re.findall(pat, s1)
print(match_obj)

# \b word boundary for exact match

pat = r"\b[0-9]{7,10}\b" #matches with exactly 7 or 10 digit number
match_obj = re.findall(pat, s1)
print(match_obj)

# finditer() brings span/index as well
pat = r"\b[0-9]{7,10}\b" #matches with exactly 7 or 10 digit number as \b is in start and end
match_obj = re.finditer(pat, s1)
print(match_obj)
for matches in match_obj:
    print(matches)

# sub() replaces the string with pattern

s2 = "Sunday, Monday, Sunday, Saturday"
print(s2)
pat = r"S[a-z]+"
replacement = "Friday"

result = re.sub(pat, replacement, s2)
print(result)

# If we want to use one pattern regularly, we should use re.compile(pattern) function for optimization

############################################
# Finding valid emails from a text file student_details.txt

with open("student_details.txt", "rt") as fh:
    data = fh.read()

pattern = r"\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][a-z]{2,}\b"
match_obj = re.finditer(pattern, data)

for matches in match_obj:
    print(matches)
