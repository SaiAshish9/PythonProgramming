import sqlite3
import json
from pathlib import Path

a=json.loads(Path("a.json").read_text())
with sqlite3.connect("db.sqlite3") as conn:
     # command="INSERT INTO A VALUES(?,?)"
     # for b in a:
     #     conn.execute(command,tuple(b.values()))
     # conn.commit()
    command="select * from A"
    cursor=conn.execute(command)
    print(cursor.fetchall())