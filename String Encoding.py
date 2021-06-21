'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def ceaser(text,key):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)+key-65) % 26+ 65)  
        elif(char.islower()):
            result+=chr((ord(char)+key-97) % 26+ 97)
        elif(char.isdigit()):
            result+=chr((ord(char)+key-48) % 10 +48)
        elif(char =="-"):
            result+="-"
        elif(char.isspace()):
            result+=" "
    return result
text=input()
key=int(input())
print(ceaser(text,key))
