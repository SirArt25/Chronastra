# Chronastra

Chronastra is a web application designed to assist you in organizing and scheduling your tasks."

## Overview

Chronastra demonstrates a basic conversational interface using [Python](https://www.python.org/) and
[Langchain](https://www.langchain.com/) framework for the creation of applications using large language models.

## Installation

1. Clone the repository:

    ```
    git clone git@github.com:SirArt25/Chronastra.git
    ```

2. Install the required dependencies:

   ```
    pip3 install pipreqs
    pipreqs --force
    pip3 install -r requirements.txt
   ```
    ---
    **NOTE** 

    - Please use Python 3.10 for ChatMate.
    
    - That if you use a virtual environment (venv), you should add the venv directory to the ignore list in the pipreqs command.
    ---
## Usage

1. Run the web app:

    ```
    streamlit run chronastra.py
    ```

2. Start interacting with the chatbot through the command-line interface, and view the results on the calendar page

## Features

- Basic conversational interface
- Responds to predefined prompts
- Minimalistic design
- Day/month/year view of the calendar.

## UML Diagram

To view the UML diagram of the project, please follow these steps:

1. Install PlantUML:

    ```
    pip3 install plantuml
    ```
   
2. Generate PNG from project.puml

    ```
    python3 -m plantuml uml-diagrams/chronastra.puml
    ```
After following these steps, you should have a PNG image generated 
from the project.puml file, 
which contains the UML diagram of the project. 
You can then view this image to understand the project's
structure and relationships.

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.