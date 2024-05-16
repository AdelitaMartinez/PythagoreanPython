# PythagSide.py
# Programmer: Adelita Martinez (amartinez1013@gmail.com)
# date: 16 May 2024
# Purpose: Find the length of the side of a right triangle
# using the pythagorean formuola

# Display a header explaining the program 
# \n gives you a line break
print('Welcome to Super Pythagorean Side Calculator 3000!')
print('The best Pythagorean Side Calculator in the multiverse! \n')
print('Use this program to calculate the length of the side of a right triange')
print('given the length of one side of the hypotenus.\n')

# Get length of one size from the user
given_side = float(input('Please enter the length of the given side in inches: '))

# Get length of the hypotenuse (opposite side from right angle)
hypotenus = float(input('Please enter the length of the hypotenus in inches: '))

# Calculate the length of the side

# Formula:
  # a**2 + b**2 = c**2 (** = squared)
  # a**2 = c**2 - b**2
  # a = (c**2 - b**2)**0.5

calculated_side = (hypotenus**2 - given_side**2)**0.5

print('\nThe length of the calculated side is',calculated_side)

# Display results

#Thank user for using program (Goodbye message)
print('\nThank you for using super side calculator 3000!')