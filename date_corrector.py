import csv

# Функция получает данные с неодинаково оформленными датами и приводит к одному виду.
def corrector(data: any) -> list: 
    
    table_months = {   # библиотека месяцев
        'January'   : '01',
        'February'  : '02',
        'March'     : '03',
        'April'     : '04',
        'May'       : '05',
        'June'      : '06',
        'July'      : '07',
        'August'    : '08',
        'September' : '09',
        'October'   : '10',
        'November'  : '11',
        'December'  : '12'
        }

    row: any = next(data) # задаем условие начала работы цикла
    date_ind: any = row.index('Release Date') # задаем столбец, в котором введены форматируемые данные
    lst: list = [row] # вводим список для записи данных с датами в едином формате
        
    
    for row in data: # цикл для перебора строк данных с форматируемыми датами
        new_date: any = row[date_ind].split() # вывод значения даты данной строки
        
        if len(new_date) < 2: # для форматирования дат, оформленных с разделителем "точка"
            new_date: any = row[date_ind].split('.')
        
        if len(new_date[0]) < 2: # если дата состоит из одной цифры
            new_date[0] = '0' + new_date[0] # добавляем спереди цифру 0
                
        if len(new_date[2]) < 4: # если число года состоит из двух цифр
            new_date[2] = '20' + new_date[2] # добавляем спереди цифры 2 и 0
        
        new_date[1] = table_months[new_date[1]] # с помощью библиотеки table_months меняем названия месяцев на числовой код

        row[date_ind]: any = ' '.join(new_date) # присвоение ячейке с датой значения в нужном формате
        lst.append(row) # добавление отформатированной строки в заданный список

    return lst
