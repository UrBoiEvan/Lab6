

# Evan Harden's Awesome encoder
def encode(password):
    encoded_list = []
    encoded_pw = ''
    for i in password:
        encoded_list.append(str(int(i) + 3))
    for i in encoded_list:
        encoded_pw += i[-1]
    return encoded_pw

def decode(encoded_pw1): # Decoder Function -- Blake Coppens
    
    if len(encoded_pw1) > 8:
        print("Error! User password is longer than 8 digits.\nShortening to 8 digits...")
        encoded_pw = encoded_pw1[:8] #shortens the length
    decoded_pw = ''
    for i in encoded_pw1: 
        convertednum = int(i)-3 #Makes sure that the length stays at most 8 digits.
        if convertednum <0:
            if convertednum == -3:
                convertednum = 7
            elif convertednum == -2:
                convertednum = 8
            elif convertednum == -1:
                convertednum = 9
        decoded_pw += str(convertednum)
    return decoded_pw

        
    

def menu(): #Menu function
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def main(): #Main function
    while True:
        menu()
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        if option == 2:
            encodedPass = input('Please enter your password to decode:')
            decoded_password = decode(encodedPass)
            print('Your password has been decoded and stored!')
        if option == 3:
            break


if __name__ == '__main__': #Unit test
    main()
