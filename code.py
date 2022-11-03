import os
from pathlib import Path

Legend = {
	'Docutments':['.pdf', '.txt'. '.docx', '.csv'],
	'Pictures':['.png', '.jpg', '.jpeg', '.webp','.gif'],
	'Music':['.mp3', '.m4a', '.m4b'],
	'Video':['.mp4', '.vlc'. '.mkv']
}

def WhichDir(hint):
	for categ, extension in Legend.items():      # looks at the list of extens for each key from the dict 'Legend'
		for fileType in extension:									
			return categ if fileType == hint     # if the type(file) matches with any one in the list, it returns the 'destination directory'
    
def OrganiseDirectory():
  for item in os.scandir():
    if item.is_dir(): continue           # checks whether 'item' is a file or a folder. If latter, skips and picks up another item
  
  filePath = Path(item)
  fileType = filePath.suffix.lower()
  directory = pickDir(fileType)
  
  if directory == None: continue
  directoryPath = Path(directory)
'''
  if directoryPath.is_dir() != True:
    directoryPath.mkdir()
    filePath.rename(directoryPath.joinpath(filePath))'''
