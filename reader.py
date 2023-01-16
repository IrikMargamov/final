import csv
import date_corrector

# открываем для чтения файл с данными
with open("spotify_songs_top_100.csv") as f:
    data: any = csv.reader(f)

# запускаем функцию корректировки дат
    new_data: list = date_corrector.corrector(data)        

# открываем файл для записи полученных после работы функции данных
with open('new_data.csv', 'w', newline='') as f:
    writer: any = csv.writer(f)
    writer.writerows(new_data)
    
    