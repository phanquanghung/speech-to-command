import torch
from transformers import pipeline

import sys
sys.path.append(".")
from utils.prompts import *

# device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model():
    # load model
    pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-alpha", torch_dtype=torch.bfloat16, device_map='auto')

    # I use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
    messages = [
        {
            "role": "system",
            "content": COMMAND_PROMPT,
        },
        {"role": "user", "content": "Test message"},
    ]

    return pipe, messages

def text_to_command(pipe, messages, text):
    # add text to messages user content
    messages[1]["content"] = text

    # format messages
    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    # generate response
    outputs = pipe(prompt, max_new_tokens=32, do_sample=True, temperature=0.1, top_k=50, top_p=0.95)

    # return assistant response
    return outputs[0]["generated_text"].split("<|assistant|>")[1].split("</s>")[0].strip()