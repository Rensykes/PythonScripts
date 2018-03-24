import pafy

#first sudo pip install --upgrade youtube_dl
#and [sudo] pip install pafy



#careful when you type the path. Be sure that there are not blank spaces after the path.

def dl_video(video, path = None):
	stream = video.getbest("mp4", ftypestrict = False) #get a video stream. Preferred extension = mp4 but can return a different extension if quality is better
	path = path + "." #useful to check if the user has typed something as path
	if path == ".": #if path = "." means that user didnt type a path
		path = path + "/" + video.title + "." + stream.extension #just add name of the file and extension
		filename = stream.download(path) 
	else: #user typed a path
		path = path[:-1] + "/" + video.title + "." + stream.extension #a little bit tricky: remove last char from string path (the . placed at row 9) -> add name of the file
		filename = stream.download(path)
	print("File downloaded at: " + path + "\n")


def dl_audio(video, path = None):
	streamlist = video.audiostreams #get a list of all audiostreams available for the video
	dictionary = dict()
	for stream in streamlist: #for each stream in streamlist
		if int(str(stream).split("@")[1][:-1]) >= 128: #if its bitrate is > 128 (NB: each entry is written as audio@extension:bitratek)
			d = {str(stream).split("@")[0].split(":")[1] : int(str(stream).split("@")[1][:-1])} #create new dictionary that has extension as key and bitrate as value
			dictionary.update(d) #add the entry to dictionary

	#personal order of preference: each of these is at least 128kbps Bitrate (radio quality)
	#if extension is key of dictionary -> get the stream
	if "mp3" in dictionary:
		stream = video.getbestaudio("mp3")
	elif "m4a" in dictionary:
		stream = video.getbestaudio("m4a")
	elif "wav" in dictionary:
		stream = video.getbestaudio("wav")
	else:
		stream = video.getbestaudio()
	path = path + "." #useful to check if the user has typed something as path
	if path == ".": #if path = "." means that user didnt type a path
		path = path + "/" + video.title + "." + stream.extension #just add name of the file and extension
		filename = stream.download(path) 
	else: #user typed a path
		path = path[:-1] + "/" + video.title + "." + stream.extension #a little bit tricky: remove last char from string path (the . placed at row 37) -> add name of the file
		filename = stream.download(path)
	print("File downloaded at: " + path + "\n")
	

def dl_both(video, path = None):
	dl_audio(video, path)
	dl_video(video, path)



url = input("Insert youtube video url: ")
v = pafy.new(url) #creates an instance of Pafy
value = input("Do you want the video or the audio? 1: Video, 2: Audio, 3: Both >>")
path = input("Insert the path >> ")


#Print informations about the video
print("General Informations: \n \n ")
print("Title: ")
print(v.title + "\n")
print("Duration: ")
print(v.duration + "\n")
print("Rating: ")
print(str(v.rating) + "\n")
print("Author: ")
print(v.author + "\n")
print("Length: ")
print(str(v.length) + "\n")
print("Keywords: ")
print(v.keywords)


result = {
	"1": dl_video,
	"2": dl_audio,
	"3": dl_both
}[value](v, path) #use of dictionary as a Switch / Case in order to Invoke functions







