import subprocess

#  subprocess.call
# .run .check_call check_output
# .Popen

completed=subprocess.run(["python","randTest.py"],capture_output=True,text=True)

print("args",completed.args)
print("returncode",completed.returncode)
print("stderr",completed.stderr)
print("stdout",completed.stdout)