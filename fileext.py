filename = input("Input the filename : ")

fileext = filename.split('.')

print("The extension of the file is : ",repr(fileext[-1]))