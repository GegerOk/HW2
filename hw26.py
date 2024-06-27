team1_num = '5'
team2_num = '6'
print ('"В команде Мастера кода участников: %s участников!"' % team1_num)
print ('"Итого сегодня в командах участников: %s и %s!"' % (team1_num, team2_num))
score_2 = 42
print('"Команда Волшебники данныъ решила задач {}!"' .format (score_2))
team1_time = 36030.4
team2_time = 18015.2
print('"Волшебники данных решили задачи за {}!"' .format(team2_time))
score_1 = 40
print(f'"Команды решили {score_1} и {score_2} задач!"')
challenge_result = 'Мастера кода'
print (f'"Результат битвы: победа команды {challenge_result}!"')
tasks_total = score_1 + score_2
time_total = team1_time + team2_time
time_avg = time_total // tasks_total
print (f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"')