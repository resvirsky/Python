import os, shutil
pastafonte = "C:/Users/renato/Desktop/Folder A"
pastadestino = "C:/Users/renato/Desktop/Folder B"

for file in os.listdir(pastafonte):
    print file
    fonte = os.path.join(pastafonte, file)
    dest = os.path.join(pastadestino, file)
    shutil.move(fonte, dest)
