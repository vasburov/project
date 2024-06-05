"""
projekt1.py: první projekt do Engeto Online Python Akademie 🤩

author: Vasyl Burov
email: vasylburov@gmail.com
discord: vasylburov
"""

import sys

# Function to terminate program
def terminateProgram(errorMessage):
  print(errorMessage)
  sys.exit(errorMessage)

# Valid credentials
userCredentials = {
    "ann": "pass123",
    "bob": "123",
    "liz": "pass123",
    "mike": "password123"
}

# Create divider
diviiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiider = "-" * 40

# Prompt user for username and password
userName = input("username: ")
userPassword = input("password: ")

# Check user input for exceptions
try:
  userCredentials[userName]
except:
  terminateProgram("unregistered user, terminating the program..")

# Check user credentials
if userCredentials[userName] == userPassword:
  print(diviiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiider)
  print(f"Welcome to the app, {userName}!")
else:
  terminateProgram("unregistered user, terminating the program..")

# Load texts
TEXTS = ['''
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
textCount = len(TEXTS) # Count texts

# Prompt user to select text
print(f"We have {textCount} texts to be analyzed.")
print(diviiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiider)
textChoice = input("Enter a number btw. 1 and " + str(textCount) + " to select: ")

# Check user input
if int(textChoice) not in range(1, textCount + 1):
  terminateProgram("invalid choice, terminating the program..")

# Clean the original text
# Replace technical symbols \n with spaces
# Remove commas and full stops
tmpText = TEXTS[int(textChoice)-1]
tmpText = tmpText.replace("\n", " ")
tmpText = tmpText.replace(",", "")
tmpText = tmpText.replace(".", "")

# Split word forms and add to list
wordForms = tmpText.split(" ")

# Remove empty values from the list
while "" in wordForms:
  wordForms.remove("")

# Create counters
wordsTitlecase = 0
wordsUppercase = 0
wordsLowercase = 0
wordsStrange = 0
numbersCount = 0
numbersSum = 0
wordFormLengths = []
wordFormLengthsFreqs = []

# Iterate through word forms
for wordForm in wordForms:

  # select words
  if wordForm.isalpha():

    # title case
    if wordForm.istitle():
      wordsTitlecase += 1

    # upper case
    if wordForm.isupper():
      wordsUppercase += 1

    # lower case
    if wordForm.islower():
      wordsLowercase += 1

  # select numbers
  elif wordForm.isdigit():

    # count
    numbersCount += 1

    # sum up
    numbersSum += int(wordForm)

  # Add word length to calculate frequencies
  wordFormLengths.append(int(len(wordForm)))

# Calculate word length frequencies
for length in range(1, int(max(wordFormLengths))+1):
  wordFormLengthsFreqs.append(wordFormLengths.count(length))

# Max frequency to format output
maxFreq = max(wordFormLengthsFreqs)

# Print the results
print(diviiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiider)
print(f"""There are {len(wordForms)} words in the selected text.
There are {wordsTitlecase} titlecase words.
There are {wordsUppercase} uppercase words.
There are {wordsLowercase} lowercase words.
There are {numbersCount} numeric strings.
The sum of all the numbers {numbersSum}""")
print(diviiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiider)
print(f"LEN|{'OCCURENCES':^{maxFreq + 2}}|NR.")
print(diviiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiider)
for length, freq in enumerate(wordFormLengthsFreqs):
  freqStars = "*" * freq
  print(f"{length + 1:>3}|{freqStars:<{maxFreq}}  |{freq}")