''' list of files and directories of the current directory
'''

from pathlib import Path

current_dir = Path('.')
for current in current_dir.iterdir():
	print(current)
print('\nAbove is a list of files and directories.') 