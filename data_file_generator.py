# You can run this program to generate a data file with all the phone numbers and contact names.
# Please Note - This Program will overwrite a file if the mentioned filename already exists.

import csv
from collections import OrderedDict

filename = input('Filename : ')

with open(f'{filename}.csv', 'w') as data_file:
        fieldnames = ['name', 'contact_number']
        csv_writer = csv.DictWriter(data_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        num_rows = int(input('Number of rows : ')) # Number of entries you want to have in the file.
        row = OrderedDict()
        for n in range(num_rows):
            for field in fieldnames:
                row[field] = input(f'{field} : ')
            csv_writer.writerow(row)



