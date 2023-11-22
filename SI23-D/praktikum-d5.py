import os
os.system('clear')

a = True
i = 0
limit = 10

while a:
    i +=1         #i = i+1
    if i <= limit:
        print('Selamat Bergabung',limit + 1 -i)
    else:
        print('Program berhenti di sini !!!!!!!')
        a = False
