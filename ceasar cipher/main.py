

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88   ''')

print()
def encode(message, shift):
    code_m = []
    message = message.lower()

    for char in message:
        if char in alpha:
            j = alpha.index(char)
            code_m.append(alpha[(j+shift)  % len(alpha)])
        else:
            code_m.append(char)

    encoded = "".join(code_m)

    print(f"Here's the encoded result: {encoded}")

    
def decode(prompt, shifting):

    code = []
    prompt = prompt.lower()

    for char in prompt:
        if char in alpha:
            j = alpha.index(char)
            code.append(alpha[(j-shifting)  % len(alpha)])
        else:
            code.append(char)

    decoded = "".join(code)

    print(f"Here's the decoded result: {decoded}")





while True:
    start_message = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    start_message = start_message.lower()

    if(start_message == 'encode'):
        input_mess = input("Type your message: \n")
        input_shift = int(input("Type the shift no: \n"))

        encode(input_mess, input_shift)

    elif(start_message == 'decode'):
        input_mess = input("Type your message to decode: \n")
        input_shift = int(input("Type the shift no: \n"))

        decode(input_mess, input_shift)
    else:
        print("Invalid prompt!")
    
    decision = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if decision!='yes':
        print("GoodBye")
        break

    

