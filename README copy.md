# ai-assisted-coding-cherry

## Instructions

Please fill your api_key in the **example_api_key.json**, and rename the file "**api_key.json**". The original file is under the gitignore list, in order to avoid leakage.

If this step is done performed correctly, the app will not work.

## Setup and Installation

* **With devcontainer** : If you are using Visual Studio Code with the Remote - Containers extension, you can automatically set up your development environment by opening the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS) and selecting `Remote-Containers: Reopen in Container`. This will build a Docker container, as defined in the `.devcontainer` configuration. Remember to install the extra libraries with `pip install -r requirements.txt`. 
* **With requirements.txt** : For a more traditional setup, or if you are not using Visual Studio Code, you can create a virtual environment using `python -m venv venv`, and activate it. Then, please install the required packages with `pip install -r requirements.txt` to mirror the project's dependencies.

## Introduction

ReTeach is a cutting-edge tool designed to assist teachers in analyzing and categorizing classroom transcripts. The system intelligently labels each statement in a transcript, aiding teachers in understanding and improving their instructional methods. This update focuses on enhancing the efficiency and accuracy of labeling teacher-student interactions in classroom sessions.

## Repo description

This repository is the nexus where artificial intelligence meets coding, streamlining the development process through automation and intelligent insights.

### Key Components

* **.devcontainer** : For a consistent and replicable development environment, the `.devcontainer` directory includes configuration files for Visual Studio Code's Development Containers feature. This setup ensures that any developer can quickly spin up a Docker container with the same settings, extensions, and toolchain as the original development environment.
* **ai_assisted_coding_cherry** : Central to our project, this directory holds the AI-powered modules meticulously crafted and exported using `nbdev`.
* **nbs** : The `nbs` folder contains Jupyter notebooks which serve as the foundation for our modules, blending code with narrative to document the development process thoroughly.
* **data** : This directory is stocked with test samples and AI-processed examples, acting as a testing ground for module functionality.
* **app.py** : The Gradio interface is launched via this script, providing an accessible, interactive front end for our application.
* **api_key.json** : Users must generate a personal `api_key.json` file containing their API key. This measure is crucial for secure API interactions, as the repository's `.gitignore` file omits the actual key to prevent unauthorized scraping. User could rename the `example_api_key.json as api_key.json` after filling the api_key in the file.
* **plot.png** : A visual representation of model accuracy, showcasing the effectiveness of our AI modules.
* **README.md** : This markdown file offers a comprehensive overview of our project and can be repurposed within the Gradio interface for user guidance.
* **requirements.txt** : Essential to replicating the Python environment, `requirements.txt` lists all the necessary packages. To install them, simply run `pip install -r requirements.txt` in your shell.

Embark on a journey with AI Assisted Coding Cherry to enhance your development process, harnessing the power of AI to elevate your coding capabilities.

## Data Structure

* **CSV Files** : Each file represents a classroom session transcript.
* **Columns** :
  * **Text** : Contains statements made by the teacher.
  * **Labels** : Classifies each statement into categories (OTR, PRS, REP, NEU).
* **Initial State** : Some CSVs may start with only the transcribed text column, requiring label assignment.

## User Interface Details

### 1. Select API Key Page

* **Functionality** : Choose between a personal or default OpenAI API key.
* **Usage** : Enter and submit the API key, enabling access to GPT-3.5-turbo for transcript processing.

### 2. Overview Page

* **Components** :
  * Detailed explanation of ReTeach's functionality.
  * Video tutorial for navigating and utilizing the app effectively.

### 3. AI-Assisted Labeling Page

* **Process** :
  * Upload CSV file(s) containing classroom transcripts.
  * Click "Process" to initiate AI-assisted labeling.
* **Output** :
  * Display of a dataframe with original text and AI-generated labels (OTR, PRS, REP, NEU).
  * Confidence scores for each label (1.0 for pre-labeled entries).
  * Download link for the processed file, indicating AI involvement.

### 4. Chat with Chatbot Interface

* **Functionality** :
  * Text box for user queries or prompts.
  * Submit button for AI response generation.
  * Option to upload CSV files for transcript-related inquiries.

### 5. AI Assisted in the Loop Page

* **Workflow** :
  * Upload CSV and select batch size.
  * Start interactive labeling with "Begin to label."
  * Label initial batch; subsequent batches are predicted based on these inputs.
  * Option to correct or accept AI predictions for each batch.
  * Generate and display an accuracy plot after processing multiple batches (>2 batch accuracy check after the first untracked accuracy, because the first batch is labeled by user).
* **Output** :
  * An accuracy plot showcasing the labeling algorithm's performance.
  * Download link for the accuracy plot.
  * Download link for the processed csv file.

## Conclusion

ReTeach revolutionizes the way educational transcripts are analyzed and categorized, offering teachers a powerful tool for self-assessment and improvement. By leveraging AI for efficient transcript labeling, ReTeach helps educators focus more on teaching strategies and student engagement, thus enhancing the overall educational experience.
