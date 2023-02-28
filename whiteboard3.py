"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels (but not y).

The input string will only consist of lowercase letters and/or spaces.

ex:
get_count('hello_world') => 3"""

def get_count(string):
    vowel_count = 0
    for char in string:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowel_count +=1
    return vowel_count

print(get_count('hello_world'))