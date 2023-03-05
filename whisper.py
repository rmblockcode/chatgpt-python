import whisper
import os
import openai

# EJEMPLOS CON LA API PUBLIC

# Repo github: https://github.com/openai/whisper

model = whisper.load_model("base")
result = model.transcribe("audio.wav")
result = model.transcribe("audio2.wav")
result = model.transcribe("audio3.mp3")
result = model.transcribe("audio_en.wav")
# print(result["text"])

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("audio3.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions(fp16=False)
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)

# EJEMPLO CON OPENAI API

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file = open("audio3.mp3", "rb")
# Transcript audio
transcript = openai.Audio.transcribe("whisper-1", audio_file)
# Translate audio to english
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript)
