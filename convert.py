import eyed3
import ffmpeg
from os import listdir
from os.path import isfile, join, splitext, basename


fileFormat = 'aif'
targetFormat = 'mp3'
album = 'KMPLX036'
isVa = True

def getFiles(mypath):
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith("." + fileFormat)]
	onlyfiles =  list(map(lambda x: mypath + '/' + x, onlyfiles))
	return onlyfiles

def convertFiles(files):
	converted = []
	for f in files:
		pre, ext = splitext(f)
		stream = ffmpeg.input(f)
		stream = ffmpeg.output(stream, pre + '.mp3', audio_bitrate='320k')
		stream.run()
		converted.append(pre + '.mp3')
	return converted

def replaceAndTrim(input):
	return input.replace('_', ' ').strip()

def tagFiles(files):
	for f in files:
		filename = basename(f).replace('.' + targetFormat, '')
		name_title_parts = filename.split('-')
		number = name_title_parts[0]
		name = replaceAndTrim(name_title_parts[1]).title()
		title = replaceAndTrim(name_title_parts[2]).capitalize()
		print(name)
		print(title)
		audiofile = eyed3.load(f)
		audiofile.tag.artist = name
		audiofile.tag.album = album
		audiofile.tag.album_artist = "Various Artists"
		audiofile.tag.title = title
		audiofile.tag.track_num = number
		audiofile.tag.save()


path = '/Users/toban/Desktop/KMPLX036/renderat'
files = getFiles(path)
files = convertFiles(files)
tagFiles(files)