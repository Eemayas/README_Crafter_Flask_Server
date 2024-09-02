from flask import Flask, request, jsonify
from lightrag.core.generator import Generator
from lightrag.core.component import Component
from lightrag.core.model_client import ModelClient
from utils.llama_configurations import model

app = Flask(__name__)

# Template for the QA model
qa_template = r"""<SYS>
You are a helpful assistant.
</SYS>
User: {{input_str}}
You:"""


# Define the SimpleQA class
class SimpleQA(Component):
    def __init__(self, model_client: ModelClient, model_kwargs: dict):
        super().__init__()
        self.generator = Generator(
            model_client=model_client,
            model_kwargs=model_kwargs,
            template=qa_template,
        )

    def call(self, input: dict) -> str:
        return self.generator.call({"input_str": str(input)})

    async def acall(self, input: dict) -> str:
        return await self.generator.acall({"input_str": str(input)})


simple_qa = SimpleQA(**model)


def ask_question():
    # Extract the question from the POST request
    question = request.json.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Generate the answer using the SimpleQA component
        answer = simple_qa.call({"input_str": question})
        return jsonify({"question": question, "answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
