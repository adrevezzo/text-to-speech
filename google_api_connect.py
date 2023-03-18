from google.cloud import texttospeech
from google.oauth2 import service_account
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

class TextToSpeechGoogleAPI:
    def __init__(self, text_to_convert, output_filename) -> None:
        self.credentials = service_account.Credentials.from_service_account_info({
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
        self.text_to_convert = text_to_convert
        self.output_filename = output_filename
        self.client = self.create_client()
        self.in_synthesis = self.synthesis_input()
        self.voice = self.create_voice()
        self.audio_config = self.config_audio()

        self.output_file()
    
    def create_client(self):
        return texttospeech.TextToSpeechClient(credentials=self.credentials)

    def synthesis_input(self):
        return texttospeech.SynthesisInput(text=self.text_to_convert)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    def create_voice(self):
        return texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    def config_audio(self):
        return texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    def create_response(self):
        return self.client.synthesize_speech(
        input=self.in_synthesis, voice=self.voice, audio_config=self.audio_config
    )

    # The response's audio_content is binary.
    def output_file(self):
        with open(f"{self.output_filename}.mp3", "wb") as out:
            # Write the response to the output file.
            out.write(self.create_response().audio_content)
            print(f'Audio content written to file "{self.output_filename}.mp3"')