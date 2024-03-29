import os

def userdirectory():
    while True:
        usr_direc = input('Please enter a directory that you would like to search in. \nFor example: /Users/'
                          'bob/Desktop/\n')

        if os.path.exists(usr_direc):
            return usr_direc
        else:
            print('Incorrect or unknown directory. Please try again.')

def what_file():
    usr_exten = input('Please enter what file types would you like to search for.\n')

    return usr_exten



def printer(usr_direc, usr_exten):
    print(usr_direc, usr_exten)
    for root, dirs, files in os.walk(usr_direc):
        for file in files:
            if file.endswith(usr_exten):
                print(file)
                import time
                time.sleep(0.5)
                return file
            if file == " ":
                print('If nothing is showing up that means that there are no files with that extension. Please close\n'
                    /  ' the program and try again')

printer(userdirectory(), what_file())
