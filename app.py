from flask import Flask, request
from ai import OpenAI

app = Flask(__name__)
openai = OpenAI()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    return openai.run_chat(data['content'])

@app.route('/promot', methods=['POST'])
def promot():
    data = request.json
    openai.set_promot(data['content'])
    return "all set"


if __name__ == '__main__':

    app.run()


