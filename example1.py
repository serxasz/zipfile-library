import zipfile
file = zipfile.ZipFile("sample.zip", "a")
file.write("test.txt")
print file.read("test.txt")
file.close()