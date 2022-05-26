'''
Identify all of the disarium within an inclusive range of n through m.

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
'''

def find_disarium(n: int, m:int) -> str:
    disariums = []

    if type(n) == int and type(m) == int:
        if n > 0 and m > 0:
            # swap numbers if n is greater than m
            if n > m:
                n, m = m, n

            # iterate through the range of pages
            for num in range(n, m + 1):
                # the length of the current dogit to be used to keep track of the position of digits
                num_count = len(str(num))
                sum_disa = 0  
                x = num

                # iterate through each page number's length
                while (x != 0) :
                    # get the digit from the rightside of the current number
                    right_digit = x % 10
                    # apply the power to the right digit using it's current position
                    sum_disa = int(sum_disa + right_digit**num_count)
                    # move position backward
                    num_count = num_count - 1
                    x = x // 10
                    
                if sum_disa == num :
                    disariums.append(str(sum_disa))

        else:
            return "Please enter valid page numbers"
    else:
        return "Please enter valid page numbers"
    
    return " | ".join(disariums)

# TEST
print(find_disarium(1, 600))          # "1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 89 | 135 | 175 | 518 | 598"
print(find_disarium(50, 2000))        # "89 | 135 | 175 | 518 | 598 | 1306 | 1676"
print(find_disarium(150, 3000000))    # "175 | 518 | 598 | 1306 | 1676 | 2427 | 2646798"
print(find_disarium(6000, 200))       # "518 | 598 | 1306 | 1676 | 2427"
print(find_disarium(-6, 200))         # "Please enter valid page numbers"
print(find_disarium("150", 3000000))  # "Please enter valid page numbers"
print(find_disarium(-6, "200"))       # "Please enter valid page numbers"
print(find_disarium(150.0, 300))      # "Please enter valid page numbers"