import subprocess
import threading
from flask import Flask
from utils.llama_configurations import ollama


from github_metadata import github_metadata_endpoint
from clone_github import clone_repo_endpoint
from folder_structure import folder_structure_endpoint
from ollam_check import ask_question
from summary_generation import summary_generation, stream_data
from project_image import get_project_icon
from project_name import get_project_name
from project_badge import get_project_badges
from project_languages import get_project_languages
from project_overview import project_overview


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/github_metadata", methods=["GET"])
def github_metadata_endpoint_main():
    return github_metadata_endpoint()


@app.route("/clone_repo", methods=["POST"])
def clone_repo_endpoint_main():
    return clone_repo_endpoint()


@app.route("/folder_structure", methods=["GET"])
def folder_structure_endpoint_main():
    return folder_structure_endpoint()


@app.route("/ask", methods=["POST"])
def ask_question_endpoint_main():
    return ask_question()


@app.route("/summary_generation", methods=["GET"])
def summary_generation_endpoint_main():
    return summary_generation()


# @app.route("/summary_generation", methods=["GET"])
# def summary_generation():
#     return stream_data()


@app.route("/project_icon", methods=["GET"])
def get_project_icon_endpoint_main():
    return get_project_icon()


@app.route("/project_name", methods=["GET"])
def get_project_name_endpoint_main():
    return get_project_name()


@app.route("/get_project_badges", methods=["GET"])
def get_project_badges_endpoint_main():
    return get_project_badges()


@app.route("/get_project_languages", methods=["GET"])
def get_project_languages_endpoint_main():
    return get_project_languages()


@app.route("/project_overview", methods=["GET"])
def project_overview_endpoint_main():
    return project_overview()


if __name__ == "__main__":
    # Ensure the model is pulled when the server starts
    subprocess.run(["ollama", "pull", "llama3.1:8b"], check=True)
    ollama_thread = threading.Thread(target=ollama)
    ollama_thread.start()

    app.run(port=5001, debug=True)
