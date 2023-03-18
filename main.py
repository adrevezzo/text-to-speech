from google_api_connect import TextToSpeechGoogleAPI

text = input("Enter what you would like to convert to speech:\n")
filename = input("Enter the name of the output file:\n")

TextToSpeechGoogleAPI(str(text), str(filename))