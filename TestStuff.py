from io import RawIOBase
import os, re

#interesting - this works
filelocation = "C:\\Users\Dascham\Desktop\paris.mp3"
#os.startfile(filepath=filelocation)





with open(filelocation) as file:
    file.seek(1)
    data = file.read(10 - 1)
    print(data)


>>>>>>> dbc04e8e6d3c8c6c5560d445530af7f9edec3000
