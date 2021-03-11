try:
    import os
except ImportError:
    print("Error: Please install os module")

File_name = input("File name: ")

try:
    File_open = open(File_name + ".bin", 'rb')
except:
    File_open = open(File_name, 'rb')

File = File_open.read()

try:
    Save = open(File_name + ".zip", 'xb')
except:
    Save = open(File_name + ".zip", 'wb')

Save.write(File)

File_open.close()
os.remove(File_name + ".bin")
Save.close()