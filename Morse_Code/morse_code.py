chars = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",	
    "O": "---",	
    "P": ".--.",	
    "Q": "--.-",	
    "R": ".-.",
    "S": "...",	
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    ".": ".-.-.-",
    ",": "--..--",	
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",	
    ":": "---...",
    ";": "-.-.-.",	
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    "\"": ".-..-.",	
    "$": "...-..-",	
    "@": ".--.-.",
    "¿": "..-.-",
    "¡": "--...-"
}

# convert input sring to a list
def to_list(string):
    list1=[]
    list1[:0]=string
    return list1

# STAGE 1
def to_morse(str_in):
    str_in = to_list(str_in)
    res = []

    for s in str_in:
        if s == " ":
            res.append("/")    
        else:
            res.append(chars[s])
    return ' '.join(res)

# STAGE 2
def from_morse(str_in):
    str_in = str_in.split(" ")
    res = []

    for item in str_in:
        if item == "/":
            res.append(" ")
        else:
            l =list(chars.keys())[list(chars.values()).index(item)]
            res.append(l)

    return ''.join(res)

menu = f'''
Please select an option by entering the menu number:
1. Encrypt to Morse Code
2. Decrypt from Morse Code
0. Exit
'''
# MENU
try:
    user_input = int(input(menu))
except ValueError:
    print("No valid integer! Please try again ...")

if user_input == 1:
    morse_ = input("Enter Message To Encrypt: \n")
    print(to_morse(morse_.upper()))
elif user_input == 2:
    morse_ = input("Enter Message To Decrypt: \n")
    print(from_morse(morse_.upper()))
elif user_input == 0:
    print("\nNo mmessage to translate\nGood Bye!")
else:
    print("ERROR: Invalid Option")
