#-------------------------------------------------------------------------------
# Name:        automation
# Purpose:
#
# Author:      dan
#
# Created:     02/02/2021
# Copyright:   (c) dan 2021
# Licence:     
#-------------------------------------------------------------------------------

inport os
from datetime import date
import pandas as pd

data_location = 'Docs/Receipts'
file_list = []
for file in os.listir(data_location):
    file_list.append(file)

data = {'file_name' : file_list }
file_df = pd.DataFrame(data)
new_file_directory = 'Docs/Processed'
today = date.today()
file_df.to_excel(new_file_directory + 'receipts_sum -' + str(today) + '.xlsx' )

for file in os.listdir(data_location):
    os.rename(data_location + file, new_file_directory + file )

string_to_find = 'Dan'
directory_to_search = 'Docs/Processed'
dan_docs = []
for file in os.listdir(directory_to_search):
    with open(directory_to_search + file) as f:
        dan_docs.append(file)

print(dan_docs)
