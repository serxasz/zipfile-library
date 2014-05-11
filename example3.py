import zipfile
file = zipfile.ZipFile("sample.zip", "r")
info = file.getinfo("test.txt")
print info.filename
file.close()