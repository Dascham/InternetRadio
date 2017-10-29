from io import RawIOBase
import os, re

#interesting - this works
#filelocation = "C:\\Users\Dascham\Desktop\paris.mp3"
#os.startfile(filepath=filelocation)
number = 1
msg = "something"

msg = msg+str(number)
print(msg)

msg = msg.encode("ascii")
print(msg)
