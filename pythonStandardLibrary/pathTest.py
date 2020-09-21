from pathlib import Path
# Path=(r"C:\Program Files")
# Path.home()
# path=Path("ecom/__init__py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# # file name without ext
# print(path.suffix)
# # file ext
# print(path.parent)
# # with name
# path=path.with_suff ix(".txt")
# print(path.absolute())


path=Path("ecom")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecom2")

a=path.iterdir()

print([x for x in a])
print([p for p in path.glob("*.py")])
# rglob with chidren also