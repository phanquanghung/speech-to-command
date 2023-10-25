import whisperx

# audio_file = "audio/output.wav"

device = "cuda" 
compute_type = "float16" # change to "int8" if low on GPU mem (may reduce accuracy)
batch_size = 16 # reduce if low on GPU mem

def load_model():
    return whisperx.load_model("base.en", device, compute_type=compute_type, language="en")

def speech_to_text(model, audio_file):
    audio = whisperx.load_audio(audio_file)
    result = model.transcribe(audio, batch_size=batch_size)

    # if model doest not recognize any speech, return empty string
    if len(result["segments"]) == 0 or result["segments"][0]["text"] == "No active speech found in audio":
        return ""
    else:
        return result["segments"][0]["text"]