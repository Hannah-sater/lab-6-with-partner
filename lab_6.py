# Hannah Sater

def main_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()

def encode(user_input):



if __name__ == '__main__':
    main_menu()
    print('Please enter an option: ', end='')
    option = str(input())
    while '1' <= option <= '3':
        if option == '1':
            print('Please enter your password to encode: ', end='')
            original_password = str(input())
            print('Your password has been encoded and stored!')
            print()
            main_menu()
            print('Please enter an option: ', end='')
            option = str(input())
        if option == '2':
            encoded_password = encode(original_password)
            print('The encoded password is', encoded_password, ', and the original password is', original_password, '.')
            print()
            main_menu()
            print('Please enter an option: ', end='')
            option = str(input())
        if option == '3':
            break



