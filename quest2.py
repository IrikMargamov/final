import pandas as pd
import json
import song_func

# Загружаем датафрейм
df = pd.read_csv('new_data.csv')

# запускаем функцию поиска трех самых старых песен
new_data: list = song_func.tree_song(df) 

# выводим результат в фойл json
with open('songs2.json', 'w', newline=None) as outfile:
    json.dump(new_data, outfile)
