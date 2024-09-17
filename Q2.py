import time
from PIL import Image

# Chapter 1: The Gatekeeper 
def chapter_1(): 
    print("*** Chapter 1: The Gatekeeper ***")      
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50
    if generated_number % 2 == 0:
        generated_number += 10

    print(f"Generated number: {generated_number}" + '\n')    
    img = Image.open("chapter1.jpg")  
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = min(r + generated_number, 255)
            g = min(g + generated_number, 255)
            b = min(b + generated_number, 255)
            pixels[x, y] = (r, g, b)
    
    img.save("chapter1out.jpg")
    red_sum = 0
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            red_sum += r

    print(f"Sum of all red pixels: {red_sum}" + "\n")
    return red_sum

# Chapter 2: The Chamber of Strings
def chapter_2():
    print("*** Chapter 2: The Chamber of Strings ***")

    string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
    number_string = ''.join([char for char in string if char.isdigit()])
    letter_string = ''.join([char for char in string if char.isalpha()])

    even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
    ascii_even_numbers = [ord(str(num)) for num in even_numbers]

    uppercase_letters = [char for char in letter_string if char.isupper()]
    ascii_uppercase_letters = [ord(char) for char in uppercase_letters]

    print(f"Number string: {number_string}" + "\n")
    print(f"Letter string: {letter_string}" + "\n")
    print(f"Even numbers (ASCII): {ascii_even_numbers}" + "\n")
    print(f"Uppercase letters (ASCII): {ascii_uppercase_letters}" + "\n")

def chapter_3():
    print("*** Chapter 2: Decoding ***")
    cipher_text = ("VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF "
                   "V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH "
                   "PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR "
                   "ZR NG ZL ORFG ZNEVYLA ZBAEBR")

    def decrypt(cipher_text, shift):
        print("By given shift 's' ")
        decrypted_message = []
        for char in cipher_text:
            if char.isalpha():
                shifted = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                decrypted_message.append(shifted)
            else:
                decrypted_message.append(char)
        return ''.join(decrypted_message)
   
    print("Try different shift values (1-25)")
    for s in range(1, 26):
        decrypted_message = decrypt(cipher_text, s)
        print(f"Shift {s}: {decrypted_message}")

if __name__ == "__main__":
    print("Chapter 1: The Gatekeeper")
    chapter_1()

    print("\nChapter 2: The Chamber of Strings")
    chapter_2()

    print("\nChapter 3: Decoding the Cryptogram")
    chapter_3()
