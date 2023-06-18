import pyttsx3 
import speech_recognition as sr  
import datetime 
import webbrowser 
import os
import pywhatkit
import shutil  
import subprocess
import time 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Mam !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Mam !")

	else:
		speak("Good Evening Mam !")

	assname =("Jarvis 1 point o")
	speak("I am your Assistant")
	speak(assname)
	

def username():
	speak("What should i call you Mam")
	uname = takeCommand()
	speak("Welcome Miss")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("################################".center(columns))
	print("Welcome Ms.", uname.center(columns))
	print("################################".center(columns))
	
	speak("How can i Help you, Mam")
print("You can use the keywords to do opeartions with voice commmands\nwikipedia\nopen google\nopen youtube\nopen code\nopen stack overflow \nplay music\nwrite a note\nshow note\ncurrent time\ndon't listen\nexit")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in') # convert the audio input to text english-india
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query
if __name__ == '__main__':
	clear = lambda: os.system('cls') #This code will only be executed if the file is run directly as a script, not if it is imported as a module.
	
	
	# clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()
		
		if "wikipedia" in query:
			webbrowser.open("wikipedia.com")
   
		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stack overflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			music_dir = 'C:\\Users\\user\\Music\\Songs'
			songs = os.listdir(music_dir)
			print(songs)
			random = os.startfile(os.path.join(music_dir, songs[0]))

		elif 'current time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Mam, the time is {strTime}")

		
		elif 'open code' in query:
			speak("Here you go for path of the code file")
			codepath="C:\\Users\\user\\AppData\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\Visual Studio Code"
			os.startfile(codepath)
			
		
		elif "who i am" in query:
			speak("If you talk then definitely your human.")
   
		elif 'how are you' in query:
			speak("I am fine, Thank you")



		elif 'shutdown system' in query: # Windows command that shuts down the system immediately without prompting the user for confirmation.
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f') #shutdown / p /f command in windows to shutdown the system

		elif "open map" in query:
			query = query.replace("open map", "")
			location = query
			speak("Here go for the map")
			speak(location)
			
			webbrowser.open("https://www.google.com/maps/@18.8181772,76.7698374,7z")

		elif "write a note" in query:
			speak("What should i write, Mam")
			note = takeCommand()
			file = open('punam.txt', 'w')
			speak("Mam, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("%H:%M:%S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note) 
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("punam.txt", "r")
			print(file.read())
			# speak(file.read(6))				
        
		elif "send message " in query:
			pywhatkit.sendwhatmsg('+919999999999', 'How are you', 15, 17)

		elif "don't listen" in query or "stop listening" in query:
			speak("I am in sleep mode good night")
			time.sleep(10)
			print(10)
   
		elif 'exit' in query:
			speak("Thanks for giving me your time ")
			exit() 


