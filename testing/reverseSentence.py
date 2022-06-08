# PROBLEM
# Given a string of words, reverse all the words
# e.g
# 'This is the Best' returns 'Best the is This'

# '   space here' or 'space here   ' returns 'space here'

def reversal(str1):
    words=str1.split()
    reverse=' '.join(words[::-1])
    
    return reverse

 

word1="This is the Best"

print(reversal(word1)) 