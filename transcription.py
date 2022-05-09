import os
import requests


def transcribe():
    while True:

        try:
            # 1 Get Audiofile
            print("type in the filename of the file in the directory 'Audios' of this i.e. 'Audio.m4a': ")
            name = input()
            filename = os.getcwd() + "/Audios/" + name

            print("The Audiofile " + filename + " is processed ... ")

            # 2 Upload Audiofile to AssemblyAI Server

            def read_file(file, chunk_size=5242880):
                with open(file, "rb") as _file:
                    while True:
                        data = _file.read(chunk_size)
                        if not data:
                            break
                        yield data

            api_key = "ef8e04f3a41f4af28ac8b884537b1a83"

            headers = {"authorization": api_key}
            response = requests.post("https://api.assemblyai.com/v2/upload",
                                     headers=headers,
                                     data=read_file(filename))

            audio_url = response.json()["upload_url"]
            print(audio_url + " " + "was uploaded ... ")

            # 3 Transcribe the Audiofile
            endpoint = "https://api.assemblyai.com/v2/transcript"

            print("Type in your language code further see https://docs.assemblyai.com/#supported-languages:")
            lang_code = input()

            json = {
                "audio_url": audio_url,
                "language_code": lang_code
            }

            headers = {
                "authorization": api_key,
                "content-type": "application/json"
            }

            transcript_input_response = requests.post(endpoint, json=json, headers=headers)
            # print(transcript_input_response.json())

            # 4 Retrieve Transcription Result
            transcript_id = transcript_input_response.json()["id"]
            # print(transcript_id)

            endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

            headers = {
                "authorization": api_key,
            }

            while True:

                transcript_output_response = requests.get(endpoint, headers=headers)

                if transcript_output_response.json()["status"] == "completed":
                    print("Transcription is finished \n")
                    print(transcript_output_response.json()["text"])
                    break
                else:
                    print("Process is " + transcript_output_response.json()["status"] + " ...")

            print("Do you want to continue? Type 'True' for Yes and type 'False' for No.")
            run = input()

            if run == "True":
                continue

            else:
                print("Program finished - until next time :)!.")
                break

        except:
            print("Ups, something went wrong. Start the program again and exactly follow the instructions :).")