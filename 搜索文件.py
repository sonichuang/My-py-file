import os

def findfile(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            print('%s\%s' % (root, name))

path = input('Input the root you want to start finding:')
name = input('Input the file name:')
findfile(name, path)
        
