from pathlib import Path
from zipfile import ZipFile

# zip=ZipFile("files.zip","w")
# with ZipFile("files.zip","w") as zip:
#     for path in Path("ecom").rglob("*.*"):
#         zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info=zip.getinfo("ecom/__init__.py")
    print(info.file_size)
    print(info.compress_size)
