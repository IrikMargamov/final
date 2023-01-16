import pandas as pd
import json
import artist_func

'''
Код для выборки из базы данных произведений Ed Sheeran
'''
# Загружаем датафрейм
df = pd.read_csv('new_data.csv')

# запускаем функцию поиска песен, которые исполнял Ed Sheeran
new_data: list = artist_func.artist_sheeran(df)  

# выводим результат в файл json
with open('songs1.json', 'w') as outfile:
    json.dump(new_data, outfile)
