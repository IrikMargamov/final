import csv


def date_corrector(data):
    
    row = next(data)
    date_ind = row.index('Release Date')
        
    for row in data:
        new_date = row[date_ind].split()
        new_date = '.'.join(new_date)
    
    return new_date


