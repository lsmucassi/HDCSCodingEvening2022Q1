# Disarium Challenge

A Disarium is defined as a number whose:

Sum of its digits powered with their respective position is equal to the original number

Your Task:

You are totally obsessed with whether a number is a Disarium or not. You have such a compelling desire to fulfil the Disarium itch
that you refuse to read any non-disarium numbered pages in any given book. 

You now, however, have 2 problems:

Your teacher just assigned you to read your textbook from page n to page m
You suffered a head injury during martial arts training that has caused you a mild case of amnesia and you have forgotten how to 
programmatically determine how to determine if a page number is a disarium number or not.

You need to identify all of the disarium within an inclusive range of n through m.

Examples of a disarium:

89 = 8^1 + 9^2

135 = 1^1 + 3^2 + 5^3

518 = 5^1 + 1^2 + 8^3


-------------
Requirements:
-------------

You will need to create a function named findDisarium() that takes the first page number and the last page number (adhere
to you the code languages naming convention for functions).
The function will then output all of the disarium numbers in that range in a string with each number 
separated by a pipe with a space on either side.

Examples:
--------

Input                      | Output
------------------------------------------------
findDisarium(1, 600)       --> "1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 89 | 135 | 175 | 518"
findDisarium(50, 2000)     --> "89 | 135 | 175 | 518 | 598 | 1306 | 1676"
findDisarium(150, 3000000) --> "175 | 518 | 598 | 1306 | 1676 | 2427 | 2646798"
findDisarium(-6, 200)      --> "Please enter valid page numbers"


If you complete the challenge in time, you can also create unit tests for the cases above to ensure that your code runs as expected.