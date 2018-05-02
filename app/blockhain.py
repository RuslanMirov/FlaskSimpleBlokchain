# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:04:58 2018

@author: Ruslan
"""

# Создаем цепочку транзакций
# Сохраняем блоки в папке blocks
# Записываем хеш
# Проверям хеш на целостность 

import json
import os
import hashlib
# путь к файлу
blockchain_dir = os.curdir + '/blocks/'
    
# вычислить хэш
def get_hash(filename):
    # параметр rb для чтения бинарных данных
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()
# получить список файлов(блоков)
def get_files():
    # возвращает список файлов и дерикторий
    files = os.listdir(blockchain_dir)
    # переводим в int для сортировки, так как os.listdir
    # сортирует так 1,10,11,2,3,4,5,6,7,8,9 единицы всегда первые
    # кроме того int нужен будет для инкремента
    return sorted([int(i) for i in files])

# проверка целостности
def check_integrity():
    files = get_files()
    results = []
    # Получаем файлы с хешем начиная со второго файла так как
    # генезис блок не содержит хеш
    for file in files[1:]:
        h = json.load(open(blockchain_dir + str(file)))['hash']
        
        prev_file = str(file - 1)
        
        actual_hash = get_hash(str(file - 1))
        
        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Hacked'
        #print('block {} is: {}'.format(prev_file, res))
        results.append({'block': prev_file, 'result': res})
        
    return results
       
    

# создать блок
def write_block(name, amount, to_whom, prev_hash=""):
    files = get_files()
    
    last_file = files[-1]
    
    filename = str(last_file + 1)
    
    prev_hash = get_hash(str(last_file))
    
    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}
    
    with open(blockchain_dir + filename, 'w') as file:
        #сохраняем данные в файл
        json.dump(data, file, indent=4, ensure_ascii=False)
    

def main():
    write_block('Jack',100,'Mila')    
    pass


if __name__ == '__main__':
    main()
