import os
os.system('clear')

a = True
limit = 5
i = 0               # 1.2.3....limit

while a:
    i += 1   # i = i + 1
    print(f'Menjalankan Program {limit + 1 - i}')
    if i == limit:
        a = False
        print('Program berhenti di sini!')
    else:
        a = True

# while a:
#     i = i+1
#     if i <= limit:
#         print('Menjalankan Program!')
#         a = True
#     else:
#         a = False

