from requests import get, post, delete

# 1 [Корректный] Просмотр всех пользователей
print(get('http://localhost:5000/api/v2/jobs').json())

# 2 [Корректный] Добавление новго пользователя
print(post('http://localhost:5000/api/v2/jobs', json={
    'id': 1,
    'job': 'Почистить зубы',
    'work_size': 3,
    'collaborators': '2, 3',
    'is_finished': False,
    'team_leader': 1}).json())

# 3 [Корректный] Просмотр одной конкретной работы
print(get('http://localhost:5000/api/v2/jobs/1').json())

# 4 [Корректный] Удаление одной конкретной работы
print(delete('http://localhost:5000/api/v2/jobs/1').json())

# 5 [Корректный] Просмотр всех пользователей
print(get('http://localhost:5000/api/v2/jobs').json())

# 6 [Некорректный] Удаление несуществующей работы
print(delete('http://localhost:5000/api/v2/jobs/11').json())

# 7 [Некорректный] Просмотр несуществующей работы
print(get('http://localhost:5000/api/v2/jobs/11').json())

# 8 [Некорректный] Неправильный тип данных в поле id
print(post('http://localhost:5000/api/v2/jobs', json={
    'id': 'a',
    'job': 'Почистить зубы',
    'work_size': 3,
    'collaborators': '2, 3',
    'is_finished': False,
    'team_leader': 1}).json())

# 9 [Некорректный] Удаление всех работ
print(delete('http://localhost:5000/api/v2/jobs').json())

# 10 [Корректный] Просмотр всех работ
print(get('http://localhost:5000/api/v2/jobs').json())
