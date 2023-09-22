# Input phrase
phrase = input()

# Split the input phrase into words
words = phrase.split()

# Initialize an empty string to store the acronym
acronym = ""

# Iterate through the words and construct the acronym
for word in words:
    if word[0].isupper():
        acronym += word[0] + "."

# Print the acronym with periods
print(acronym)
