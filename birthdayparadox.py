"""Birthday Paradox Sim, by Al Sweigart
Edited by Khadijah Surratt https://github.com/deejuh719
The source code is available at https://nostarch.com/big-book-small-python-programming"""

import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(1990, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None to indicate no match.
    
    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday.
            
#Intro
print('''Birthday Paradox, by Al Sweigart
      Edited by Khadijah Surratt https://github.com/deejuh719
      The source code is available at https://nostarch.com/big-book-small-python-programming
      
      The birthday paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large.
      This program does a Monte Carlo simulation (repeated random simpulations) to explore the concept.
      (It's not truly a paradox, just a surprising result.)''')

#Set up a tuple of month names in order:
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

while True: # Keep asking until the user enters a valid amount.
    print('How many birthdays should I generate? (Max 500)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 500):
        numBDays = int(response)
        break # User has entered a valid amount.
    print('Please enter a number between 1 and 100.')

# Generate and display the birthdays:
print('Here are ', numBDays, ' birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match.
match_count = 0 # Initializing birthday match counter

match = getMatch(birthdays) # Calling the getMatch function to check for matching birthdays

if match:
    match_count += 1 # Incrementing the birthday match counter

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print(match_count, 'other person has a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0 # How many simulations had matching birthdays in them.
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, ' simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')
print()

# Display simulation results:
probability = round(simMatch / 100_000 * 500, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a ', probability, '% chance of')
print('having a matching birthday in their group.')
if probability <= 30:
    print('That\'s a low probability of having a matching birthday.')
elif probability <= 50:
    print('That\'s a pretty decent probability of having a matching birthday.')
elif probability <= 80:
    print('That\'s a high probability of having a matching birthday.')
else:
    print('That\'s a lot of matching birthdays!')
print()