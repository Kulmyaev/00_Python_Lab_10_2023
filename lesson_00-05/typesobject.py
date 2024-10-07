# int "integer" - целое число
# float Число с плавающей точкой (вещественные числа)
# str (от слова "string") Строка
# bool (от слова "boolean")Логический тип True False
# list Список
# dict (от слова "dictionary") Словарь
# tuple Кортеж
# set Множество
# file Файлы

# int "integer" - целое число
i: int = -7 # i: int - int
il: int = 1 # il: int - int
# float Число с плавающей точкой (вещественные числа)
f: float = 4.8
fl: float = 7.4
# str (от слова "string") Строка
s: str = 'Text'
sl: str = 'Hello text'
# bool (от слова "boolean")Логический тип True False
b: bool = True
bl: bool = False
# list Список
ls: list = [] #  Пустой список
lu: list = ['g','l','j','f']
lr: list = [1,2,3,4,5,6,7,8,9,10]
ld: list = ['c', 'p', ['text'], 4, 7.8, -8, i]
lf: list = [d * 3 for d in 'list'] #
lk: list = [b * 3 for b in 'list' if b !='i']
# dict (от слова "dictionary") Словарь
d: dict = {'dict': 1, 'dictionary': 2}
dl: dict = dict([(1,4), (5,7)])
# tuple Кортеж
name: str = 'Test'
sity: str = 'Msk'
# set Множество
st: set = set()
slr: set = set('hello')
stv: set = {'a','b','c','d','e'}
slg: set = {i ** 2 for i in range(20)} # генератор множеств
# file Файлы
fc = open('text.txt','wb')
