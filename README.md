
<p align="center">
    <img src="./README-Crafter.png" width="200" style="border-radius: 20px;" />
</p>
            

<p align="center">
    <h1 align="center">README_Crafter_Flask_Server</h1>
</p>
            

<p align="center">
  <img src="https://img.shields.io/github/license/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="license">
  <img src="https://img.shields.io/github/last-commit/Eemayas/README_Crafter_Flask_Server?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
  <img src="https://img.shields.io/github/languages/top/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="repo-top-language">
  <img src="https://img.shields.io/github/languages/count/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="repo-language-count">
  <img src="https://img.shields.io/github/actions/workflow/status/Eemayas/README_Crafter_Flask_Server/build.yml?branch=main&style=flat&color=0080ff" alt="build-status">
  <img src="https://img.shields.io/github/issues/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="open-issues">
  <img src="https://img.shields.io/github/forks/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="forks">
  <img src="https://img.shields.io/github/stars/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="stars">
  <img src="https://img.shields.io/github/issues-pr/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="pull-requests">
  <img src="https://img.shields.io/github/contributors/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="contributors">
  <img src="https://img.shields.io/github/commit-activity/m/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="commit-activity">
  <img src="https://img.shields.io/github/languages/code-size/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="code-size">
  <img src="https://img.shields.io/github/repo-size/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="repo-size">
  <img src="https://img.shields.io/github/downloads/Eemayas/README_Crafter_Flask_Server/total?style=flat&color=0080ff" alt="downloads">
  <img src="https://img.shields.io/github/v/release/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="release-version">
  <img src="https://img.shields.io/codecov/c/github/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="coverage">
  <img src="https://img.shields.io/snyk/vulnerabilities/github/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="security">
  <img src="https://img.shields.io/website?style=flat&color=0080ff&url=https%3A%2F%2Fexample.com" alt="performance">
  <img src="https://img.shields.io/github/commit-activity/y/Eemayas/README_Crafter_Flask_Server?style=flat&color=0080ff" alt="activity">

</p>
    

<p align="center">
    <em>Constructed using the following tools and technologies:</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
  <img src= "https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" alt="Jupyter Notebook">
  <img src="https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white" alt="Flask">
</p>

# Project Overview
This project is a web application that coordinates the retrieval of GitHub metadata, cloning of repositories, and generation of project summaries. The application provides various endpoints for interacting with GitHub, including retrieving repository metadata, cloning repositories, and generating folder structure data for projects. It also includes utility functions for handling Llama configurations and saving pandas DataFrames to Excel files. The project uses Flask as the web framework, AIOHTTP and Requests for making HTTP requests, Pandas for data manipulation, and PrettyTable for displaying tabular data. Key features of the project include its ability to generate summaries based on project metadata and files, retrieve various project information, and handle Llama configurations.

# Table of Content

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Install Dependencies](#step-2-install-dependencies)
  - [Running the Project](#running-the-project)
    - [Step 1: Activate Virtual Environment](#step-1-activate-virtual-environment)
    - [Step 2: Run the Server](#step-2-run-the-server)
  - [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
    - [Contributing Guidelines](#contributing-guidelines)
- [Contributors](#contributors)
- [License](#license)

# Key Features

- **GitHub Endpoints**: Handles interactions with GitHub, such as retrieving metadata and cloning repositories.
- **Project Summary Generation**: Generates project summaries based on metadata and files.
- **Project Information Endpoints**: Provides endpoints for retrieving various project information, including name, icon, badges, languages, and key features.
- **Llama Configuration Handling**: Utilizes utility functions to handle Llama configurations.
- **Utility Functions**: Includes functions like saving dataframes to Excel files, handling metadata and cloning repositories.


# Folder Structure

<pre style="background-color: #f0f0f0; padding: 15px; border-radius: 5px;"><code>
<a href="./" style="color: #000; text-decoration: none;">README_Crafter_Flask_Server</a>/
├── <a href=".gitignore" style="color: #000; text-decoration: none;">.gitignore</a>
├── <a href="app.py" style="color: #000; text-decoration: none;">app.py</a>
├── <a href="constants.py" style="color: #000; text-decoration: none;">constants.py</a>
├── <a href="endpoints/" style="color: #000; text-decoration: none;">endpoints</a>/
│   ├── <a href="endpoints/clone_github.py" style="color: #000; text-decoration: none;">clone_github.py</a>
│   ├── <a href="endpoints/folder_structure.py" style="color: #000; text-decoration: none;">folder_structure.py</a>
│   ├── <a href="endpoints/github_metadata.py" style="color: #000; text-decoration: none;">github_metadata.py</a>
│   ├── <a href="endpoints/ollam_check.py" style="color: #000; text-decoration: none;">ollam_check.py</a>
│   ├── <a href="endpoints/project_api.py" style="color: #000; text-decoration: none;">project_api.py</a>
│   ├── <a href="endpoints/project_badge.py" style="color: #000; text-decoration: none;">project_badge.py</a>
│   ├── <a href="endpoints/project_contibuting.py" style="color: #000; text-decoration: none;">project_contibuting.py</a>
│   ├── <a href="endpoints/project_contibutors.py" style="color: #000; text-decoration: none;">project_contibutors.py</a>
│   ├── <a href="endpoints/project_image.py" style="color: #000; text-decoration: none;">project_image.py</a>
│   ├── <a href="endpoints/project_installation_guide.py" style="color: #000; text-decoration: none;">project_installation_guide.py</a>
│   ├── <a href="endpoints/project_key_feature.py" style="color: #000; text-decoration: none;">project_key_feature.py</a>
│   ├── <a href="endpoints/project_languages.py" style="color: #000; text-decoration: none;">project_languages.py</a>
│   ├── <a href="endpoints/project_license.py" style="color: #000; text-decoration: none;">project_license.py</a>
│   ├── <a href="endpoints/project_name.py" style="color: #000; text-decoration: none;">project_name.py</a>
│   ├── <a href="endpoints/project_overview.py" style="color: #000; text-decoration: none;">project_overview.py</a>
│   └── <a href="endpoints/summary_generation.py" style="color: #000; text-decoration: none;">summary_generation.py</a>
├── <a href="global_types.py" style="color: #000; text-decoration: none;">global_types.py</a>
├── <a href="global_variables.py" style="color: #000; text-decoration: none;">global_variables.py</a>
├── <a href="output/" style="color: #000; text-decoration: none;">output</a>/
│   ├── <a href="output/Car-Race-Game_summary.xlsx" style="color: #000; text-decoration: none;">Car-Race-Game_summary.xlsx</a>
│   ├── <a href="output/Daraz_Scraper_api_reference_data.xlsx" style="color: #000; text-decoration: none;">Daraz_Scraper_api_reference_data.xlsx</a>
│   └── <a href="output/Daraz_Scraper_summary.xlsx" style="color: #000; text-decoration: none;">Daraz_Scraper_summary.xlsx</a>
├── <a href="prompts.toml" style="color: #000; text-decoration: none;">prompts.toml</a>
├── <a href="README.md" style="color: #000; text-decoration: none;">README.md</a>
├── <a href="Readme_Flask_Server.ipynb" style="color: #000; text-decoration: none;">Readme_Flask_Server.ipynb</a>
├── <a href="ReadMe_Generators%20(before%20adding%20comments).ipynb" style="color: #000; text-decoration: none;">ReadMe_Generators (before adding comments).ipynb</a>
├── <a href="ReadMe_Generators.ipynb" style="color: #000; text-decoration: none;">ReadMe_Generators.ipynb</a>
├── <a href="requirement.txt" style="color: #000; text-decoration: none;">requirement.txt</a>
├── <a href="shieldsio_icons.json" style="color: #000; text-decoration: none;">shieldsio_icons.json</a>
└── <a href="utils/" style="color: #000; text-decoration: none;">utils</a>/
    ├── <a href="utils/check_new_repo_request.py" style="color: #000; text-decoration: none;">check_new_repo_request.py</a>
    ├── <a href="utils/handle_metadata_and_clone.py" style="color: #000; text-decoration: none;">handle_metadata_and_clone.py</a>
    ├── <a href="utils/llama_configurations.py" style="color: #000; text-decoration: none;">llama_configurations.py</a>
    ├── <a href="utils/output_formators.py" style="color: #000; text-decoration: none;">output_formators.py</a>
    └── <a href="utils/save_dataframe_to_excel.py" style="color: #000; text-decoration: none;">save_dataframe_to_excel.py</a>
3 directories, 36 files
</code></pre>


# Getting Started

Welcome to the README Crafter Flask Server installation guide! This guide will walk you through the process of setting up and running the project on your local machine.

## Prerequisites

Before installing, ensure you have the following:

* Python 3.8 or higher (download from [here](https://www.python.org/downloads/))
* pip (Python package manager) installed
* Flask (download from [here](https://flask.palletsprojects.com/en/2.0.x/installation/))

**Optional Dependencies:**

* Docker (for running the project in a container)

## Setup Instructions
### Step 1: Clone the Repository

Open your terminal and run:
```bash
git clone https://github.com/Eemayas/README_Crafter_Flask_Server.git
```

### Step 2: Install Dependencies

Navigate to the project directory and install the required packages using pip:
```bash
cd README_Crafter_Flask_Server
pip install -r requirements.txt
```
This will install all the necessary dependencies, including Flask and other required libraries.

## Running the Project
----------------------

### Step 1: Activate Virtual Environment

To ensure a clean and isolated environment for your project, we recommend using a virtual environment. You can create one using:
```bash
python -m venv env
```
Activate the environment with:
```bash
source env/bin/activate
```

### Step 2: Run the Server

Navigate to the project directory and run:
```bash
python app.py
```
This will start the Flask development server.

## Troubleshooting
------------------

If you encounter any issues during installation or running the project, refer to the following troubleshooting guide:

* **Dependency Issues:** Check if all dependencies are installed correctly. You can do this by running `pip list` and verifying that all required packages are listed.
* **Server Not Running:** Ensure the server is started with the correct command (`python app.py`). Also, check for any syntax errors in your code by running `python -m py_compile app.py`.
* **Connection Issues:** Verify that your firewall settings allow incoming connections on port 5000 (the default Flask development server port).

By following these steps and troubleshooting tips, you should be able to successfully install and run the README Crafter Flask Server project.

# Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/Eemayas/README_Crafter_Flask_Server/pulls)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Eemayas/README_Crafter_Flask_Server/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/Eemayas/README_Crafter_Flask_Server/issues)**: Submit bugs found or log feature requests for README_Crafter_Flask_Server.

### Contributing Guidelines

1. **Fork the Repository**:
    - Start by forking the project repository to your GitHub account.
2. **Clone the Repository**:
    - Clone your forked repository to your local machine using the command:
    ```sh
    git clone https://github.com/your-username/README_Crafter_Flask_Server.git
    ```
    - Replace ``your-username`` with your GitHub username.
3. **Create a New Branch**:
    - Create a new branch for your changes using the command:
    ```sh
    git checkout -b your-branch-name
    ```
4. **Make Your Changes**:
    - Edit, add, or delete files as needed. Ensure your changes align with the project's contribution guidelines.
5. **Commit Your Changes**:
    - Stage your changes and commit them with a descriptive message:
      ```bash
      git add .
      git commit -m "Your descriptive message"
      ```
6. **Push Your Changes:**
    - Push your branch to your forked repository:
      ```bash
      git push origin your-branch-name
      ```
7. **Create a Pull Request (PR):**
    - Go to the original repository on GitHub and click “Compare & pull request.” Provide a clear description of the changes and submit the PR.

Once your PR is reviewed and approved, it will be merged into the main branch.


# Contributors

| Avatar | Contributor | GitHub Profile | No of Contributions |
|:--------:|:--------------:|:----------------:|:-------------------:|
| <img src='https://avatars.githubusercontent.com/u/100434825?v=4' width='40' height='40' style='border-radius:50%;'/> | Eemayas | [@Eemayas](https://github.com/Eemayas) | 35 |

        


# License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

