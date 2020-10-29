import subprocess
list_files = subprocess.run(["make"])
print("The exit code was: %d" % list_files.returncode)

