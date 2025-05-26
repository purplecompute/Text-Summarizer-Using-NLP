# importing the necessary libraries.
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')   # Configuring the logging module to display the time and the message.

project_name = "textSummarizer"   # Declaring the project name.

# Creating a variable to store the list of files that need to be created.
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]

# Looping through the list of files and creating the files.
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)   # This function splits the path into two parts, the directory and the filename.

    if filedir != "":   # If filedir is not empty
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it does not exist.
        logging.info(f"Creating directory:{filedir} for the file {filename}")   # Logging the creation of the directory.
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
        
  
    
    