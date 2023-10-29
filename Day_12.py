#Homework1
def swap_case(s):
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#Homework2
words = ["cat", "car", "code", "home", "learn", "fun", "job", "love", "friend", "zoo", "enjoy", "happiness", "family", "goal", "desire"]

# Input the letter to filter
letter = input("Enter a letter: ")

# Initialize an empty list to store filtered words
filtered_words = []

# Loop through the words and check if the letter is in each word
for word in words:
    if letter in word:
        filtered_words.append(word)

# Output the filtered words
for word in filtered_words:
    print(word)
