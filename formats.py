import zipfile
import zlib
import os
file1 = zipfile.ZipFile("samples/sample1.zip", "w", zipfile.ZIP_STORED)
file2 = zipfile.ZipFile("samples/sample2.zip", "w", zipfile.ZIP_DEFLATED)
file1.write("test.txt")
file2.write("test.txt")
print os.path.getsize('samples/sample1.zip')
print os.path.getsize('samples/sample2.zip')
file1.close()
file2.close()