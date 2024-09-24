import random
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = map(lambda x,y: x==y,first, second)
print(list(result))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        name = file_name
        file = open(name,'w',encoding='utf-8')
        # file.write()
        for line in data_set:
            file.write(f'{line} \n')
        file.close()
        return file_name
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:

    def __init__(self,*words):
        self.words = words

    def __call__(self):
        elem = random.choice(self.words)
        return elem

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())