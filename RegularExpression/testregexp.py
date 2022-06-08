import re

with open('file2.txt') as file:string=file.read()
pattern=r'([0-9]+\.){3}([0-9]+)'     # Ip address Regex 
pattern=r''     # Ip address Regex 
matches=re.finditer(pattern,string)
# matches=pattern.finditer(string)


for match in matches:
    print(match.group())