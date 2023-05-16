import os
import openai


class OpenAI:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        openai.api_key = self.api_key

        self._promot = ''
        self._chat_content = []
        self.model = "gpt-3.5-turbo"

    def set_promot(self, input):
        
        self._promot = input
        msg = {"role": "system", "content": input}
        if len(self._chat_content) == 0:
            self.add_new_data_to_chat(msg)
        else:
            self._chat_content[0] = msg
        

    def run_chat(self, data):
        msg = {"role": "user", "content": data}
        self.add_new_data_to_chat(msg)

        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=self.get_chat_history(),
        )
        resp = completion.choices[0].message
        self.add_new_data_to_chat(resp)
        return resp

    def add_new_data_to_chat(self, data):
        self._chat_content.append(data)

    def get_chat_history(self):
        return self._chat_content
