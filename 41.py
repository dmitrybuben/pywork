# 41.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные: 
# 12W1B12W3B24W1B14W

init_str = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'        # запись исходной строки в файл 
data = open('input_41.txt', 'w')
data.write(init_str)
data.close

path = 'input_41.txt'          # чтение строки из файла и запись в переменную
data = open(path, 'r')
work_str = data.read()
data.close

def compress(work_str):     # сжатие строки
    res_str = ''
    count = 1
    for e in range(len(work_str)-1):
        if work_str[e+1] == work_str[e]:
            count += 1
        else:
            res_str += str(count) + work_str[e]
            count = 1
    res_str += str(count) + work_str[e]
    return res_str

with open('compressed_41.txt', 'w') as data:        # запись сжатой строки в файл
    data.write(compress(work_str))
    

with open('compressed_41.txt','r') as data:         # считывание сжатой строки в переменную
    comp_str = data.read()

def decompress(comp_str):                           # восстановление сжатой строки
    decomp_str = ''
    char_qty = ''
    for i in range(len(comp_str)):
        if comp_str[i].isdigit():
            char_qty += comp_str[i]
        else:
            decomp_str += comp_str[i]*int(char_qty)
            char_qty = ''
    return decomp_str

with open('decompressed_41.txt', 'w') as data:      # запись восстановленной строки в файл
    data.write(decompress(comp_str))
