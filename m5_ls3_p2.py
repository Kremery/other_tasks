''' list of files and directories in the specified path
'''

from pathlib import Path

path = input("Input the path in the format: 'Disk:\directory' ")
current_dir = Path(path)
for current in current_dir.iterdir():
	print(current)
print('\nAbove is a list of files and directories.') 