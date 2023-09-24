from enum import Enum
from threading import Thread
from llama_cpp import Llama
from transformers import TextIteratorStreamer
from llama_chat_format import format_to_llama_chat_style







def init_auto_model_and_tokenizer(file_path,n_ctx:int=800):
    model = Llama(file_path, n_ctx=n_ctx)
    tokenizer = None
    return model, tokenizer


class run_ui:
    def __init__(self,model,is_chat_model:bool):
        super().__init__()
        self.model=model
        self.is_chat_model=is_chat_model
    def user(self,user_message, history):
          return "", history + [[user_message, None]]

    def bot(self,user_message):
        history = [["Hello", "Hi there! How can I help you?"], ["How are you?",
                                                                "I am Fine.How about You?"]]
        if self.is_chat_model:
            instruction = format_to_llama_chat_style(history)
            new_instruction=instruction+f"[INST]{user_message}[/INST]"
        else:
            new_instruction=user_message
        responsee = ""
        kwargs = dict(temperature=0.6, top_p=0.9)

        kwargs["max_tokens"] = 800
        chunck =self.model(prompt=new_instruction, echo=True, stop=["[/INST]","[INST]","<s>","</s>"],**kwargs)
        text = chunck['choices'][0]['text']
        responsee += text
        history.append([user_message,responsee])
        output=responsee.replace(f"{new_instruction}"," ")
        return output
    def run(self):
        user_input=input("Enter the message:")
        text=self.bot(user_message=user_input)
        print(f"Assistant: {text}")


def main(file_path):
    model, tokenizer = init_auto_model_and_tokenizer(file_path)
    while True:
        try:
            text=run_ui(model,is_chat_model=True)
            text.run()
        except Exception as e:
            print(e)
if __name__ == '__main__':
    file_path="llama2.gguf"
    main(file_path=file_path)
