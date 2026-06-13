fo = open("C:\\Data_VidehSir\\HTMLAssignment\\video.mp4","rb")    
bdata = fo.read()
#print("Binary data:",bdata)
path=fo.name
print("File path:",path)
print("================")
listpath = path.split("\\")
print(listpath)
print("================")
filename = listpath[len(listpath)-1]
print("File Name:",filename)

fo=open(filename,"wb")
fo.write(bdata)
print("copy content successfully")



