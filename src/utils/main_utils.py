import os.path
import sys
import yaml
import base64

from src.exception import AppException
from src.logger import logging

##############################################################
# Reads a YAML file and returns its content as a dictionary.
##############################################################
def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise AppException(e, sys) from e
    

##############################################################
# Writes content to a YAML file
##############################################################
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write_yaml_file")

    except Exception as e:
        raise AppException(e, sys)
    

##############################################################
# Decodes a base64 string and writes it as an image file.
##############################################################
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./reports/prediction_results/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


##############################################################
# Encodes an image file into a base64 string.
##############################################################
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
