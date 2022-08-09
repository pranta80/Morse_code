from replit import clear

def get_morse(input_string):
    morse_code_dict = {
        'a': '._',
        'b': '_...',
        'c': '_._.',
        'd': '_..',
        'e': '.',
        'f': '..-.',
        'g': '__.',
        'h': '....',
        'i': '..',
        'j': '.___',
        'k': '_._',
        'l': '._..',
        'm': '__',
        'n': '_.',
        'o': '___',
        'p': '.__.',
        'q': '__._',
        'r': '._.',
        's': '...',
        't': '_',
        'u': '.._',
        'v': '..._',
        'w': '.__',
        'x': '_.._',
        'y': '_.__',
        'z': '__..',
        '1': '.____',
        '2': '..___',
        '3': '...__',
        '4': '...._',
        '5': '.....',
        '6': '_....',
        '7': '__...',
        '8': '___..',
        '9': '____.',
        '0': '_____'
    }

    output = ''

    for letter in input_string:
        morse_code = morse_code_dict.get(letter.lower())
        output = output + morse_code + ' '
    return output


is_on = True

while is_on:
    clear()
    input_string = input("Give a string: ")
    output_string = get_morse(input_string)
    print(f"Given string in morse code: {output_string}")
    cont = input("Want to try again? 'y' for yes, 'n' for exit: ")
    if cont == 'n':
        is_on = False
