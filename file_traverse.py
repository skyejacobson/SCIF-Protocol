import os

def userdirectory():
    while True:
        global usr_direc
        usr_direc = input('Please enter a directory that you would like to search in. \nFor example: /Users/'
                          'bob/Desktop/\n')

        findDir = os.system('cd /;''find ' + usr_direc)
        try:
            os.system(findDir)
        except TypeError:
            pass
        os.system(findDir)
        if os.system(findDir) == TypeError:
            print('Incorrect or unknown directory. Please try again.')
            TypeError = False
            
    else:
        return usr_direc

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


# Try to avoid os.walk
# Use CD and LS type commands to run through directories.



# def userdirectory():
 #   usr_direc = input('Please enter a starting area that you would like to search in.')