from infer import llm_infer, whisper_infer
from utils import record

file_path = "audio/output.wav"

def init():
    global llm, messages, whisper
    llm, messages = llm_infer.load_model()
    whisper = whisper_infer.load_model()


def run():
    global llm, messages, whisper

    # record audio
    record.rec(file_path)

    # transcribe audio
    text = whisper_infer.speech_to_text(whisper, file_path)
    print('TRANSCRIPTION:',text)

    # command

    # if text does not contain any character, return empty string
    if text == "" or text.isspace():
        print('COMMAND:','no command')
        return ""
    else:
        command = llm_infer.text_to_command(llm, messages, text)
        print('COMMAND:',command)
        
        return command
