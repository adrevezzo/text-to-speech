from google_api_connect import TextToSpeechGoogleAPI

text = input("What enter what you would like to convert:\n")

TextToSpeechGoogleAPI(str(text), "next_file")