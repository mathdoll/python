__author__ = 'Rinisha'
__date__ = '3/25/2016'


lettersForDecoding = {
    ".-":"A",
    "-...":"B",
    "-.-.":"C",
    "-..":"D",
    ".":"E",
    "..-.":"F",
    "--.":"G",
    "....":"H",
    "..":"I",
    ".---":"J",
    "-.-":"K",
    ".-..":"L",
    "--":"M",
    "-.":"N",
    "---":"O",
    ".--.":"P",
    "--.-":"Q",
    ".-.":"R",
    "...":"S",
    "-":"T",
    "..-":"U",
    "...-":"V",
    ".--":"W",
    "-..-":"X",
    "-.--":"Y",
    "--..":"Z",
    "-----":"0",
    ".----":"1",
    "..---":"2",
    "...--":"3",
    "....-":"4",
    ".....":"5",
    "-....":"6",
    "--...":"7",
    "---..":"8",
    "----.":"9",
    ".-.-.-":".",
    "--..--":":",
    "---...":":",
    "..--..":"?",
    ".----.":"'",
    "-....-":"-",
    "-..-.":"/",
    ".-..-.":"?",
    ".--.-.":"@",
    "-...-":"="
    }
lettersForEncoding = {
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
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "?": ".-..-.",
    "@": ".--.-.",
    "=": "-...-",
    " ": "/"
    }

def split(text, delimiter):
    words = text.split(delimiter)
    return words

CHARACTER_DELIMITER = " "

while (True):
    choice = raw_input("1. to encode, 2. to decode, 3. to exit")

    if choice == "1":
        translationToMorse = raw_input("What would you like to translate?")
        translationToMorse = translationToMorse.upper()
        buffer = ""
        for char in translationToMorse:
            buffer += lettersForEncoding[char]
            buffer += CHARACTER_DELIMITER

        print(buffer)

    elif choice == "2":
        translationToEnglish = raw_input("What would you like to translate?")
        '''translation = translation.upper()'''
        buffer= ""
        mywords = split(translationToEnglish, CHARACTER_DELIMITER)
        for word in mywords:
            if word == " " or word == "":
                continue
            try :
                buffer += lettersForDecoding[word]
            except KeyError :
                print("BAD INPUT")
                exit(0)
        print(buffer)
    else:
        print ("thank you")
        exit(0)