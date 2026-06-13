'''
os :It is a build system specific module which is used to provide system related specifications, like current working directory, create/remove directory.
'''
from os import * 
print("Current Working Directory:",getcwd())

#create directory
# mkdir("sample")

#change directory
#chdir("sample")

print("Current Working Directory:",getcwd())

rmdir("sample")