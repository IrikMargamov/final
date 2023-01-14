import csv


with open('spotify_songs_top_100.csv') as f:
        data = csv.reader(f)

        print(date_corrector(data))