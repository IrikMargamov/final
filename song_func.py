import pandas as pd
import json

def tree_song(data: list) -> list:
    
    years_songs: dict = {} # определим пустой словарь

    for i in range(len(data['Release Date'])): # запустим цикл для формирования дат в виде кода, составленного из составляющих чисел в виде: ггггммдд
        splt_date: list = data['Release Date'][i].split() # разбиение дат по делителю 
        splt_date: list = splt_date[2] + splt_date[1] + splt_date[0] # составление кода из чисел даты в виде: ггггммдд
        if splt_date in years_songs:                                 # проверка условия вхождения кода в библиотеку, добавление в библиотеку
            years_songs[splt_date] += data['Song'][i]
        years_songs[splt_date] = data['Song'][i]


    sorted_tuple = sorted(years_songs.items(), key=lambda x: x[0])
    # получили отсортированный список кортежей, отсортированных по первому значению
    
    years_songs = dict(sorted_tuple) # преобразовываем обратно в словарь
    list_songs = list(years_songs.values()) # переводим в список названия песен, отсортированных по времени выхода
    the_olderest_songs = [list_songs[0], list_songs[1], list_songs[2]] # составляем список трех самых старых песен

    return the_olderest_songs