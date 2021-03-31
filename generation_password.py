import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
n=0
#ввод данных
print('Сколько паролей нужно?')
num = int(input())
print('Какая длина пароля?')
length = int(input())
print('Включать ли цифры 0123456789?; д = да, н = нет')
digit = input()
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; д = да, н = нет')
upper = input()
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?; д = да, н = нет')
lower = input()
print('Включать ли символы !#$%&*+-=?@^_?; д = да, н = нет')
symbols = input()
print('Исключать ли неоднозначные символы il1Lo0O?; д = да, н = нет')
similar_symbols = input()

if digit=='д':
    chars+=digits
if upper=='д':
    chars+=uppercase_letters
if lower=='д':
    chars+=lowercase_letters
if symbols=='д':
    chars+=punctuation
def generate_password(length, chars):
    password=''
    text=list(chars)
    for i in range(length):
        password+=random.choice(text)
    return password

while n!=num:
    
    print(generate_password(length, chars))
    n+=1
#протестировать
#test complite
