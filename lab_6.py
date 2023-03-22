# Hannah Sater

def main_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def encode(user_input):
    user_password = []
    user_password[:0] = user_input
    encoded_password = ''
    for i in user_input:
        if i == '0':
            encoded_password = encoded_password + '3'
        if i == '1':
            encoded_password = encoded_password + '4'
        if i == '2':
            encoded_password = encoded_password + '5'
        if i == '3':
            encoded_password = encoded_password + '6'
        if i == '4':
            encoded_password = encoded_password + '7'
        if i == '5':
            encoded_password = encoded_password + '8'
        if i == '6':
            encoded_password = encoded_password + '9'
        if i == '7':
            encoded_password = encoded_password + '0'
        if i == '8':
            encoded_password = encoded_password + '1'
        if i == '9':
            encoded_password = encoded_password + '2'
    return encoded_password


# Riley Jacobs
def decode(encoded_password):
    original_password = ""
    for digit in encoded_password:
        original_digit = (int(digit) - 3) % 10
        original_password += str(original_digit)
    return original_password


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
