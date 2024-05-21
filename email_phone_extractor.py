# Finds phones and email addresses on the clipboard 
'''
HIGH LEVEL PROGRAM FLOW 
* Get the text off the clipboard. 
* Find all the phone number and email address in the text.
* Pass them onto the clipboard 
'''

'''
PROGRAM PSEUDOCODE 
* Use the pyperclip module to copy and paste strings.
* create two regexes, one for matching phone numbers and one for matching
  email addresses 
* Find all the matches, not just the first match of both regexes
* Neatly format the matched strings into a single strings to paste.
* Display some kind of text if no matches where found in the text. 
'''

# Program Code 
# Import necessary module 
import pyperclip, re

# Step one: Create a regexe for phone numbers 
phoneRegex = re.compile(r'''(
  (\d{3}|\(\d{3}\))?          # Area code 
  (\s|-|\.)?                  # Separator 
  (\d{3})                     # First three digit 
  (\d|-|\.)                   # separator 
  (\d{4})                     # last 4 digits
  (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension 
)''', re.VERBOSE)


# TODO: Create email regex 
# Create a regex or email addresses 
emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+             # character class for username 
  @                             # @ symbol 
  [a-zA-Z0-9.-]+                # character class for domain name 
  (\.[a-zA-Z0{2,4}])            # character class of dot-something 
  )''', re.VERBOSE)

# TODO: Find matches in clipboard text 
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
  phoneNum = '-'.join([groups[1], groups[3], groups[5]])
  if groups[8] != '':
    phoneNum += 'x' + groups[8]
  matches.append(phoneNum)
  
for groups in emailRegex.findall(text):
  matches.append(groups[0])  

# TODO: copy results to the clipboard 
if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print('copied to clipboard: ')
  print('\n'.join(matches))
else:
  print('No phone numbers or email addresses found.')
