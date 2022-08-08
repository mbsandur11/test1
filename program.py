import os
import shutil
import time

file = open("text.txt", "w") 
file.write("Your text goes here") 
file.close() 
'r' open for reading (default)
'w' open for writing, truncating the file first
'x' open for exclusive creation, failing if the file already exists
'a' open for writing, appending to the end of the file if it exists
