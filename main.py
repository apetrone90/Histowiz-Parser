from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from Functions import number_parser,imagetagParser
import pandas as pd
import os


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
name, extension = os.path.splitext(filename)

## Import Data File ##
if extension == '.csv':
    data = pd.read_csv(filename)
elif extension == '.xlsx':
    data = pd.read_excel(filename)
else:
    print('Unrecgonized file type!')
    print(f'Filetype ends in : {extension}')

## Remove Control Samples ##
data = data[data['Image Tag'].str.contains("control") == False]

## Parse Image tag for raw animal number ##
imagetagParser(data)

#Refine animal number for vlookup with number_parser function
data['Animal Number'] = data['Animal Number Raw'].apply(lambda x: int(number_parser(x)))

#Ask user for columns of interest #
print(data.columns)
user = [str(x) for x in input('Enter Column Names that Contain Requested Data. /n(Note: Please separate multiple entries with a comma): ').split(',')]
output_col_list = ['Animal Number']
for x in user:
    output_col_list.append(x)
df = data[output_col_list]

#Write data to output.xlsx file #
df.to_excel('output.xlsx')
print(f'Finished exporting data from column {user} for file: {name+extension}')



