from google.cloud import texttospeech
from google.oauth2 import service_account
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

credentials = service_account.Credentials.from_service_account_info({
  "type": env.get("TYPE"),
  "project_id": env.get("PROJECT_ID"),
  "private_key_id": env.get("PRIVATE_KEY_ID"),
  "private_key": env.get("PRIVATE_KEY"),
  "client_email": env.get("CLIENT_EMAIL"),
  "client_id": env.get("CLIENT_ID"),
  "auth_uri": env.get("AUTH_URI"),
  "token_uri": env.get("TOKEN_URI"),
  "auth_provider_x509_cert_url": env.get("AUTH_PROVIDER_X509_CERT_URL"),
  "client_x509_cert_url": env.get("CLIENT_X509_CERT_URL")
})



client = texttospeech.TextToSpeechClient(credentials=credentials)

synthesis_input = texttospeech.SynthesisInput(text="Hello World")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')