import pandas as pd
import json

# Загружаем датафрейм
df = pd.read_csv('new_data.csv')

# songs_ed_sheeran = {} # определим словарь для сбора информации по певцу 
# songs_ed_sheeran['Ed Sheeran'] = [] # определим ключ словаря

# for i in range(len(df['Song'])): # задаем цикл для перебора строк в столбце названий песен при учете значений в столбце исполнителя
#     if df['Artist'][i] == 'Ed Sheeran': # задаем условие включения значения словаря
#         songs_ed_sheeran['Ed Sheeran'].append(df['Song'][i]) # вводим значение в словарь
    
#     arts = df['Artist'][i].split() # разбиваем слова ячейки в столбце исполнителя, если несколько певцов
    
#     if len(arts) > 2: # исключаем из расмотрения ячейки из двух элементов других исполнителей
#         for j in range(len(arts)-1): # запускаем цикл для перебора пар имя-фамилия исполнителя
#             var = [arts[j], arts[j+1]] # список пары слов ячейки
#             var = ' '.join(var) # формируем имя-фамилия исполнителя
#             if var == 'Ed Sheeran': # задаем условие включения значения словаря
#                 songs_ed_sheeran['Ed Sheeran'].append(df['Song'][i]) # вводим значение в словарь
#                 break # прерываем цикл, если исполнитель найден

# older_songs = []
# old_song_date = df['Release Date'][0]

# for i in range(len(df['Song'])): # задаем цикл для перебора строк в столбце названий песен при учете значений в столбце исполнителя
#     if df['Release Date'] > old_song_date:


import pandas as pd
# data = pd.read_json("sample.json")
df['timestamp'] = pd.to_datetime(df["Release Date"])
print(df['timestamp'].max())


# # выводим результат в фойл json
# with open('songs.json', 'w') as outfile:
#     json.dump(songs_ed_sheeran, outfile)
