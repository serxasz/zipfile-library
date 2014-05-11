import zipfile
file = zipfile.ZipFile("sample.zip", "r")
file.extract("test.txt");
file.close()