
#program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string,
# except with the words in backwards order

sampleText = str(input("Enter some words , atleat 10: \n"))

sampleList = sampleText.split()
reversedList = sampleList[::-1]

print(reversedList)