from google_api_connect import TextToSpeechGoogleAPI
from pdfreader import read_pdf




invalid= True
while invalid:
    choice = input("Pick text input method (1 or 2):\n1. Manually Enter Text\n2. Input path to pdf file\n")
    if choice not in (str(1), str(2)):
        print("\nInvalid choice. Try again\n")

    else:
        invalid = False

if choice == str(1):
    text = input("Enter what you would like to convert to speech:\n")
else:
    input_pdf = input("Enter the file name containing the text:\n")
    text = read_pdf(input_pdf)

filename = input("Enter the name of the output file:\n")

TextToSpeechGoogleAPI(str(text), str(filename))