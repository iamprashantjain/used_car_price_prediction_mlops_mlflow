import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'pricePredictor'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Create directories and files efficiently
for filepath in list_of_files:
    filepath = Path(filepath)
    
    # Create the directory if it doesn't exist
    if filepath.parent != "":
        os.makedirs(filepath.parent, exist_ok=True)
        logging.info(f"Creating Directory: {filepath.parent}")

    # Check if the file exists and its size
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w"):
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath.name} already exists")
