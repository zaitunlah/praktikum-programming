import os
os.system('clear')

a = True

while a:
    jawab = input('Apakah Ingin Lanjutkan? (y/n)')
    if jawab == 'y':
        print('Terima Kasih')
        a = True
    elif jawab == 'n':
        os.system('clear')
        print('Sampai Jumpa :D')
        a = False
    else:
        print('Jangan Aneh deh:)')
        a = True

