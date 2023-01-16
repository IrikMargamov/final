import pandas as pd
import json

'''
функция для выборки произведений Ed Sheeran
'''
def artist_sheeran(data: list) -> any:
    

    songs_ed_sheeran: dict = {} # определим словарь для сбора информации по певцу 
    songs_ed_sheeran['Ed Sheeran'] = [] # определим ключ словаря

    for i in range(len(data['Song'])): # задаем цикл для перебора строк в столбце названий песен при учете значений в столбце исполнителя
        if data['Artist'][i] == 'Ed Sheeran': # задаем условие включения значения словаря
            songs_ed_sheeran['Ed Sheeran'].append(data['Song'][i]) # вводим значение в словарь
        
        arts = data['Artist'][i].split() # разбиваем слова ячейки в столбце исполнителя, если несколько певцов
        
        if len(arts) > 2: # исключаем из расмотрения ячейки из двух элементов других исполнителей
            for j in range(len(arts)-1): # запускаем цикл для перебора пар имя-фамилия исполнителя
                var = [arts[j], arts[j+1]] # список пары слов ячейки
                var = ' '.join(var) # формируем имя-фамилия исполнителя
                if var == 'Ed Sheeran': # задаем условие включения значения словаря
                    songs_ed_sheeran['Ed Sheeran'].append(data['Song'][i]) # вводим значение в словарь
                    break # прерываем цикл, если исполнитель найден
    
    return songs_ed_sheeran