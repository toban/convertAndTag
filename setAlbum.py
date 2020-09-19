import eyed3
import ffmpeg
from os import listdir
from os.path import isfile, join, splitext, basename


fileFormat = 'mp3'
album = 'KMPLX ACID 7'

def getFiles(mypath):
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith("." + fileFormat)]
	onlyfiles =  list(map(lambda x: mypath + '/' + x, onlyfiles))
	return onlyfiles

def tagFiles(files):
	for f in files:

		audiofile = eyed3.load(f)

		audiofile.tag.album = album

		audiofile.tag.save()


path = '/Users/toban/Desktop/KMPLX036/renderat/mp3'
files = getFiles(path)
files = tagFiles(files)
