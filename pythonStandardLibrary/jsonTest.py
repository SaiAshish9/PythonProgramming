import json
from pathlib import Path

# a=[
#     {0:"1",1:"2"}
# ]
#
# b=json.dumps(a)
# print(b)
# Path("a.json").write_text(b)

data=Path("a.json").read_text()
print(json.loads(data),json.loads(data)[0]['0'],end='')