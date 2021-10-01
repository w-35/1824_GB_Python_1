duration = int(input('Введите значение в секундах '))
# пользователь ввел значение

print('вы ввели', duration, 'сек')

#считаем дни, часы, минуты, секунды (остатки от дел. и цел.)
day = duration // 86400
hours = (duration // 3600) % 24
minutes = (duration // 60) % 60
seconds = duration % 60

if duration < 3600:
    print('это ', minutes, 'минут', seconds, 'секунд')
elif duration >3600 and duration < (24*3600):
    print('это ', hours, 'часов', minutes, 'минут', seconds, 'секунд')
else:
    print('это ', day, 'дней', hours, 'часов', minutes, 'минут', seconds, 'секунд')



