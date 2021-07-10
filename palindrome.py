def palindrome(word):
    if len(word)<2: return 'true'
    if word[0]!=word[-1]: return 'false'
    return palindrome(word[1:-1])

word = 'racecar'
print(palindrome(word))
