import os 
from pathlib import Path 
### To extact project specific paths##
import logging 

logging.basicConfig(level=logging.INFO)

project_name="Ml-project001"

list_of_files =[
    ##".github/workflows/.gitkeep",
    f"src/{project_name}/__inti__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/dataingestion.py",
    f"src/{project_name}/components/datatransformation.py",
    f"src/{project_name}/components/modeltrainer.py",
    f"src/{project_name}/components/modelmonitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "main.py"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass 
        logging.info(f"Creating empty file :{filepath}")

    else:
        logging.info(f"{filename} is already exists")
