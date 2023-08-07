# Anagram Check: Write a Python function that checks whether two given words are anagrams.
# Input: "cinema", "iceman"
# Output: "True"

str1 = "abce"
str2 = "cdbo"
sorted_str1 = ''.join(sorted(str1))
sorted_str2 = ''.join(sorted(str2))

print("This is Anagram" if sorted_str1==sorted_str2 else "This is not  Anagram")


    
