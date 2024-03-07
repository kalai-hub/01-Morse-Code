a_z = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]

while True:
    text = input("Enter a word to convert: ").upper()
    text_morse_code = ''
    for letter in text:
        try:
            i_index = a_z.index(letter)
            text_morse_code += morse_code[i_index] + ' '
        except ValueError:
            text_morse_code += letter + ' '

    print(text_morse_code)