import os


def findFile():
    what_file = input('Please enter a file that you would like to search for:\n\n')
    tcmd = os.system('find ' + what_file)
    print(tcmd)


findFile()

