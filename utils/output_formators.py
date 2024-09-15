import os
import json
import time
import aiohttp
import asyncio
import requests
import argparse
import threading
import subprocess
import nest_asyncio
import pandas as pd
from tqdm import tqdm
from flask_cors import CORS  # Import CORS
from flask import jsonify, request, Response, stream_with_context, Flask
from prettytable import PrettyTable

from pathlib import Path
from typing import List, Dict, Any, Optional

from lightrag.core.generator import Generator
from lightrag.core.component import Component
from lightrag.components.model_client import OllamaClient

import global_variables
from global_types import RepositoryMetadata, Contributor

from constants import (
    ignore_list_folder_structure,
    specific_ignores_api,
    api_ignore_extensions,
    extensions,
    frameworks_extensions,
    tools_extensions,
)

from endpoints.github_metadata import (
    github_metadata_endpoint,
    github_metadata_endpoint_handler,
)
from endpoints.clone_github import clone_repo_endpoint, clone_repo_endpoint_handler
from endpoints.folder_structure import (
    folder_structure_endpoint,
    folder_structure_dict_endpoint,
    folder_structure_endpoint_handler,
)
from endpoints.ollam_check import ask_question
from endpoints.project_installation_guide import project_installation_guide
from endpoints.project_image import get_project_icon
from endpoints.project_name import get_project_name
from endpoints.project_badge import get_project_badges
from endpoints.project_languages import get_project_languages
from endpoints.project_overview import project_overview
from endpoints.project_key_feature import project_key_feature
from endpoints.project_api import get_api_references, update_https_requests_endpoint
from endpoints.project_contibuting import contributing_guide
from endpoints.project_contibutors import project_contributors
from endpoints.project_license import project_license
from endpoints.summary_generation import (
    summary_generation,
    file_summary_generation,
    summary_generation_handler,
    summary_generation_handler_stream,
)

from utils.save_dataframe_to_excel import save_dataframe_to_excel
from utils.handle_metadata_and_clone import handle_metadata_and_clone
from utils.llama_configurations import get_description_data, model
from utils.check_new_repo_request import check_new_repo_requent
