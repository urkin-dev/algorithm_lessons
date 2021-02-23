import sys
from os import listdir


def getListInput(count):
    """ Find the input file with certain count of values in input direcory and return a list from this file """
    files = listdir('inputs/')
    sortfile = ''

    for f in files:
        filecount = f.split('.')[0].split('_')[1]
        if (int(filecount) == int(count)):
            sortfile = f

    if (sortfile == ''):
        print("There's not such file in the directory")
        sys.exit()

    with open('inputs/' + sortfile) as f:
        list = f.readlines()[1:][0]
        list = list.split(' ')[:-1]

    list = [int(i) for i in list]

    return list
