input_text='HeLLo woRLd'

swap_char=''
for char in input_text:
    if char.isupper():
        swap_char +=char.lower()
    elif char.islower():
        swap_char += char.upper()
    elif char.isspace():
        swap_char += char
print(swap_char)