team1_num = 5
team2_num = 6
score_1 = 40 #мастера кода
score_2 = 42 #волшебники данных
team1_time = 1552.512
team2_time = 2153.31451

#побеждает та команда, которая решила больше задач за меньшее время
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print('В команде Мастера кода участников: %d !' % team1_num)
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print( "Волшебники данных решили задачи за {} с !".format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {score_2 + score_1} задач, в среднем по {(team1_time + team2_time) / (score_2 + score_1)} на задачу!.')
