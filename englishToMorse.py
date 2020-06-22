# Morse Code Translater
def englishToMorse(s): # Function to convert English letters to Morse
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                        'C':'-.-.', 'D':'-..', 'E':'.', 
                        'F':'..-.', 'G':'--.', 'H':'....', 
                        'I':'..', 'J':'.---', 'K':'-.-', 
                        'L':'.-..', 'M':'--', 'N':'-.', 
                        'O':'---', 'P':'.--.', 'Q':'--.-', 
                        'R':'.-.', 'S':'...', 'T':'-', 
                        'U':'..-', 'V':'...-', 'W':'.--', 
                        'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                        '1':'.----', '2':'..---', '3':'...--', 
                        '4':'....-', '5':'.....', '6':'-....', 
                        '7':'--...', '8':'---..', '9':'----.', 
                        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                        '?':'..--..', '/':'-..-.', '-':'-....-', 
                        '(':'-.--.', ')':'-.--.-'} 
    # Separating letter with spaces and words with tabs
    ans = []
    for i in s:
        if i.upper() not in MORSE_CODE_DICT:
            return -1
        if i == " ":
            ans.append('\t') 
        else:
            ans.append(MORSE_CODE_DICT[i.upper()])
    letters = ' '.join(ans)
    return letters

# Error Handling for the choice
while True:
    try:
        choice = int(input("Enter\n1 for Morse to English\n2 for English to Morse\n"))
        if choice == 1 or choice == 2:
            break
        else:
            print('Error!!')
    except ValueError:
        print("Oops, you must enter either 1 or 2")

# Driver for English to Morse
if choice == 2:
    x = None
    while True:
        s = input("Please enter the String: ")
        x = englishToMorse(s)
        if x != -1:
            break
        else:
            print("Error!!!")
    print(f"The Morse Code is : {x}" )
