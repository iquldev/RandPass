import random as r

def password(symbols, lenght):
    pw = []
    for i in range(lenght):
        pw.append(r.choice(symbols))
    message = '*' * len(pw)
    with open('password.txt', 'a') as f:
        f.write(''.join(pw) + '\n')
    print('-----------------------------\n'
          'Пароль', ''.join(message), 'cохранен в password.txt!\n'
          '-----------------------------')

if __name__ == '__main__':
    symb = input('Использовать специальные символы? (Y/n): '.strip()) or 'y'
    nums = input('Использовать цифры? (Y/n): '.strip()) or 'y'
    lenght = int(input('Длина пароля: '))
    symbols = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if symb == 'y':
        symbols.extend(list('!@#$%^&*()_+'))
    if nums == 'y':
        symbols.extend(list('0123456789'))
    password(symbols, lenght)