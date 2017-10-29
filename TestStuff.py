from io import RawIOBase
import os, re

#interesting - this works
filelocation = "C:\\Users\Dascham\Desktop\paris.mp3"
#os.startfile(filepath=filelocation)





with open(filelocation) as file:
    file.seek(1)
    data = file.read(10 - 1)
    print(data)


