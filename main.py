

# Evan Harden's Awesome encoder
def encode(password):
    encoded_list = []
    encoded_pw = ''
    for i in password:
        encoded_list.append(str(int(i) + 3))
    for i in encoded_list:
        encoded_pw += i[-1]
    return encoded_pw



def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def main():
    while True:
        menu()
        option = int(input('Please enter an option: '))
        if option == 1:
            input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
        if option == 2:
            # FIX ME: add decoder function
            print('')
        if option == 3:
            break


if __name__ == '__main__':
    main()
