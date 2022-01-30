lookup = 'twitter'
user="mehuljindal18.txt"
with open(user) as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            print ('found at line:', num )   
