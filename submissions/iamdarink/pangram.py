import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase) 
    return alphabet <= set(s.lower()) 

def pangram_checker(s):
    if is_pangram(s):
        words = s.split()  
        longest_word = max(words, key=len) 
        return longest_word
    else:
        return "Not a Pangram"

input = input("input: ")
output = pangram_checker(input)
print("Output:", output)
