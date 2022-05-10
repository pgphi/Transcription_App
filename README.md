# Transcription_App
***
This application transcribes audio files (from audio --> to text).

Author: Philipp Ganster

Version: 1.0

for further information read the AssemblyAI docs: https://docs.assemblyai.com/
***

# How you start this application

1) Pull the directory
2) install the necessary requirements in this directory
3) navigate to this directory and type in the command line: <b>python3 main.py</b> to start the program

# Logic-Flow of this application

    1) (Before starting the program) Save your raw audio file in the "Audios" folder
    2) *Starting the program ...*
    3) Type in the name of the audio file (saved in the "Audios" folder)
    4) *Audio file gets uploaded to the AssemblyAI server - this may take a while depending on the size of the file ... *
    5) Type in the language of the audio file, you want to transcribe i.e. "en" for englisch or "de" for german
    6) *audio file is processed/transcribed - this may take a while depending on the size of your file ... *
    7) Finished Transcription is outputed in the terminal
    8) If you want to transcribe another audio file type in "True" otherwise type in "False" to stop the application
