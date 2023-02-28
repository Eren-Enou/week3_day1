#Given two strings, write a function that returns true if they are anagrams of each other and false otherwise.
#An anagram is a word, phrase, or name formed by rearranging the letters of another word.

s1 = "anagram"
t1 = "nagaram"
# Output:
# True

s2 = "rat"
t2 = "car"
#Output:
# False

s3 = "stops"
t3 = "pots"
#Output:
# False

def anagram_check(s1, s2):
    dict1 = {}
    dict2 = {}

    for char in s1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1

    for char in s2:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1
            
    if dict1 == dict2:
        return True
    else:
        return False
    
print(anagram_check(s1,t1))
print(anagram_check(s2,t2))
print(anagram_check(s3,t3))