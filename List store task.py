#Task
#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

words=["Kenya", "Uganda", "Tanzania", "Rwanda"]

#using the list comprehension to create a new list with words having an odd number of character
odd_length_word=[word for word in words if len(word)%2!=0]

#Print the words with odd  numbers of characters
print("words with odd  numbers of characters: ",odd_length_word)