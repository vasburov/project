"""
projekt1.py: Textový analyzátor

author: Vasyl Burov
email: vasylburov@gmail.com
discord: vasylburov
"""

import sys

# Function to terminate the program
def terminateProgram(errorMessage):
  sys.exit(errorMessage)

# Valid user credentials
users = {
    "ann": "pass123",
    "bob": "123",
    "liz": "pass123",
    "mike": "password123"
}

# Prompt user for username and password
userName = input("username:")
userPassword = input("password:")

try: # Check the user input for exceptions
  users[userName]
except:
  terminateProgram("unregistered user, terminating the program..")

if users[userName] == userPassword: # Check the user credentials
  print("----------------------------------------")
  print(f"Welcome to the app, {userName}!")
else:
  terminateProgram("unregistered user, terminating the program..")

# Load the texts to analyse
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Prompt the user for a text number selection
print(f"We have {len(texts)} texts to be analyzed.")
print("----------------------------------------")
textChoicePrompt = "Enter a number btw. 1 and " + str(len(texts)) + " to select: "
textChoice = input(textChoicePrompt)

try: # Check the user input for exceptions
  int(textChoice) in range(1, len(texts) + 1)
except:
  terminateProgram("invalid choice, terminating the program..")

if not (int(textChoice) in range(1, len(texts) + 1)): # Check if the text exists
  terminateProgram("invalid choice, terminating the program..")

# Clean the original text and convert it into a list
tmpText = texts[int(textChoice) - 1]
tmpText = tmpText.replace("\n", " ") # Replace \n with spaces
tmpText = tmpText.replace(",", "") # Remove commas
tmpText = tmpText.replace(".", "") # Remove full stops
tmpText = tmpText.strip() # Remove the leading and ending spaces
wordForms = tmpText.split(" ") # Split word forms and add them to a list

# Analyse word forms and calculate statistics
wordsTitle = 0
wordsUpper = 0
wordsLower = 0
numbersCount = 0
numbersSum = 0
wordFormLongest = len(max(wordForms, key=len)) # The longest word form
wordFormFrequency = [0] * (wordFormLongest + 1) # List for statistics (from 1)

for wordForm in wordForms:
  if wordForm.isalpha(): # Words
    if wordForm[0].istitle(): # Title case
      wordsTitle += 1
    if wordForm.isupper(): # Upper case
      wordsUpper += 1
    if wordForm.islower(): # Lower case
      wordsLower += 1
  elif wordForm.isdigit(): # Numbers
    numbersCount += 1 # Count
    numbersSum += int(wordForm) # Sum up
  wordFormFrequency[len(wordForm)] += 1 # Count the word lengths frequencies

# Print the results
print("----------------------------------------")
print(f"There are {len(wordForms)} words in the selected text.")
print(f"There are {wordsTitle} titlecase words.")
print(f"There are {wordsUpper} uppercase words.")
print(f"There are {wordsLower} lowercase words.")
print(f"There are {numbersCount} numeric strings.")
print(f"The sum of all the numbers {numbersSum}")

maxWordFrequency = max(wordFormFrequency) # Max frequency to format the output
print("----------------------------------------")
print(f"LEN|{'OCCURENCES':^{maxWordFrequency + 2}}|NR.")
print("----------------------------------------")
for wordLength, wordFrequency in enumerate(wordFormFrequency[1:], start = 1):
  graphStars = "*" * wordFrequency
  print(f"{wordLength:>3}|{graphStars:<{maxWordFrequency + 2}}|{wordFrequency}")