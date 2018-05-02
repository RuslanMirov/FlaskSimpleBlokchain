# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:46:55 2018

@author: Ruslan
"""

from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
import blockhain  



app = Flask(__name__)  

# Вывод главной страницы с формой ввода на ней
@app.route('/', methods=['POST', 'GET'])
def index():
    # Если пользователь шлет POST запрос запиысваем данные с формы
    # и передаем их методу write_block из скрипта blochain
    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']
        
        blockhain.write_block(name=lender, amount=amount, to_whom=borrower) 
        # обновляем страницу с помощью редиректа
        return redirect(url_for('index'))
    # Рендеринг главной страницы
    return render_template('index.html')

# Проверка блоков на целлостность
@app.route('/checking', methods=['GET'])
def check():
    # Получаем информацию о целлостности блоков из функции check_integrity скрипта blockhain
    results = blockhain.check_integrity()
    
    
    # передаем информацию в шаблон index в переменной res
    return render_template('index.html', res=results)
  
    

if __name__ == '__main__':
   app.run(debug=True)

  
    