# Morse Code Challenge
For this challenge, you will be required to build a Morse code encryptor and decrypter. You can use any langauge of your choosing 
to complete the challenge.

Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, 
called dots and dashes, or dits and dahs. Morse code is named after Samuel Morse, one of the inventors of the telegraph.

You can find a table of Morse code characters here:
https://morsedecoder.com/

Please note that for the purpose of this exercise, where there is a space between words, you should use "/" to separate words in your
encrypted Morse code.
Eg. HELLO WORLD --->  .... . .-.. .-.. --- / .-- --- .-. .-.. -..


------------------------------------------
STAGE 1
------------------------------------------
For the first step we would like you to create a function/method that encodes a sentence with words in all caps into morse code. For the
function to be valid, you should have the following examples correctly encoded (please note all inputs and outputs are strings):

"CHALLENGE" --> "-.-. .... .- .-.. .-.. . -. --. ."
"HELP ME !" --> ".-..-. .... . .-.. .--. / -- . / -.-.-- .-..-."
"JOHN, THAT'S MY NAME" --> ".-..-. .--- --- .... -. --..-- / - .... .- - .----. ... / -- -.-- / -. .- -- . .-..-."

------------------------------------------
STAGE 2
------------------------------------------
For the second step, we would like you to create a function/method that decodes Morse Code into sentences with upper case.
This satge will be considered finished if the following inputs and outputs work correctly:

"-.-. .... .- .-.. .-.. . -. --. ." --> "CHALLENGE" 
".-..-. .... . .-.. .--. / -- . / -.-.-- .-..-." --> "HELP ME !"
".-..-. .--- --- .... -. --..-- / - .... .- - .----. ... / -- -.-- / -. .- -- . .-..-." --> "JOHN, THAT'S MY NAME"

-----------------------------------------
STAGE 3
-----------------------------------------
We would like you to include a menu that allows a user to select whether they want to encode or decode and then take a user
input and use the relevant function. The menu should look as follows:

Please select an option by entering the menu number:
1. Encrypt to Morse Code
2. Decrypt from Morse Code
0. Exit

