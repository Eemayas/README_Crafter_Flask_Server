import os
import subprocess
from lightrag.components.model_client import OllamaClient

# Create the model selection
model = {"model_client": OllamaClient(), "model_kwargs": {"model": "llama3.1:8b"}}

collab = 0


def ollama():
    """
    Start the Ollama API server in a separate thread with appropriate environment settings based on the execution context.

    The function sets environment variables for the Ollama server and starts the server using the `subprocess.Popen` method.
    It configures the server to listen on different hosts based on whether the script is running in a Colab environment or not.

    Environment Variables:
    - 'OLLAMA_HOST': The address and port on which the Ollama server will listen.
    - 'OLLAMA_ORIGINS': The allowed origins for requests to the Ollama server.

    If running in a Colab environment, the server is set to listen on '0.0.0.0:11434'. Otherwise, it listens on '127.0.0.1:11434'.

    Note:
    - Ensure that the `ollama` command is available in the system path for `subprocess.Popen` to work correctly.
    - This function will not block the main thread as it runs the server in a separate thread.

    Returns:
    None
    """
    if collab:
        os.environ["OLLAMA_HOST"] = "0.0.0.0:11434"
        os.environ["OLLAMA_ORIGINS"] = "*"
        subprocess.Popen(["ollama", "serve"])
    else:
        os.environ["OLLAMA_HOST"] = "127.0.0.1:11434"
        os.environ["OLLAMA_ORIGINS"] = "*"
        subprocess.Popen(["ollama", "serve"])


def get_description_data(description):
    """
    Retrieve data from the description object if it has a `data` attribute.

    Parameters:
    description (object): The object from which to retrieve the data. This can be any object that may or may not have a `data` attribute.

    Returns:
    str: The data from the `description` object if it exists, otherwise the original description.
    """
    if hasattr(description, "data"):
        return description.data
    return description


def is_empty_or_error(description):
    """
    Check if the description is empty or contains an error message.

    Parameters:
    description (str): The description string to check for emptiness or error messages.

    Returns:
    bool: True if the description is empty or contains an HTTP 401 error message, otherwise False.
    """
    description_str = (
        get_description_data(description).strip()
        if isinstance(description, str)
        else ""
    )
    return not description_str or "HTTP error 401" in description_str
