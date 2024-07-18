# Super Pythagorean Side Calculator 3000

## Overview
The **Super Pythagorean Side Calculator 3000** is a Python program designed to calculate the length of a side of a right triangle using the Pythagorean theorem. This tool is especially useful for solving problems involving right triangles where one side and the hypotenuse are known.

## Purpose
The purpose of this program is to find the length of a missing side of a right triangle using the Pythagorean theorem. This theorem states that in a right triangle, the square of the length of the hypotenuse (c) is equal to the sum of the squares of the lengths of the other two sides (a and b). The formula is expressed as:
\[ a^2 + b^2 = c^2 \]

## How to Use the Program
1. **Input the Length of One Side:**  
   When prompted, enter the length of one of the sides of the right triangle (not the hypotenuse).
   
2. **Input the Length of the Hypotenuse:**  
   When prompted, enter the length of the hypotenuse (the side opposite the right angle).

3. **View the Result:**  
   The program will calculate and display the length of the missing side using the formula:
   \[ \text{side} = \sqrt{c^2 - b^2} \]
   
4. **Exit the Program:**  
   After displaying the result, the program will thank you for using the Super Pythagorean Side Calculator 3000.


## Code Explanation
The program begins by displaying a welcome message and instructions. It then prompts the user to input the lengths of one side and the hypotenuse of the right triangle. Using these inputs, the program calculates the length of the missing side with the formula:
\[ \text{calculated\_side} = \sqrt{\text{hypotenus}^2 - \text{given\_side}^2} \]

Finally, the program displays the calculated length and thanks the user for using the program.

## Dependencies
This program requires Python 3 to run. It uses basic input/output functions and mathematical operations provided by the standard Python library.
