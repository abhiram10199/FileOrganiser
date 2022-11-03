import os
from pathlib import Path

Legend = {
	'Docutments':['.pdf', '.txt', '.docx', '.csv'],
	'Pictures':['.png', '.jpg', '.jpeg', '.webp','.gif'],
	'Music':['.mp3', '.m4a', '.m4b'],
	'Video':['.mp4', '.vlc', '.mkv']
}

def WhichDir(hint):
    for categ, extension in Legend.items():  # looks at the list of extens for each key from the dict 'Legend'
        for fileType in extension:									
            if fileType == hint:             # if the type(file) matches with any one in the list, it returns the 'destination directory'
                return categ
    
def OrganiseDirectory():
  for item in os.scandir():
    if item.is_dir(): continue               # checks whether 'item' is a file or a folder. If latter, skips and picks up another item
    
    FilePath = Path(item)                    # gets the path of the file
    FileType = FilePath.suffix.lower()       # gets the type(file) from the extension
    Directory = WhichDir(FileType)           # assigns seatination directory to variable
    
    if Directory == None: 	             # if file extension isn't given in the Legend, skip
            continue
            
    DirectoryPath = Path(Directory)					 
    FilePath.rename(DirectoryPath.joinpath(FilePath))    # sends the item into proper directory
