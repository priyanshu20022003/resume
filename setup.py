from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "MACHINE LEARNING PROJECT"
VERSION = "0.0.1"
DESCRIPTION = "THIS IS OUR MACHINE LEARNING PROJECT IN MODULAR CODING"
AUTHOR_NAME = "PRIYANSHU"
AUTHOR_EMAIL = "bpriyanshu95@gmail.com"
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirement_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        requirement_list = requirements_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
            
    return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    url='https://www.python.org/sigs/distutils-sig/',
    packages=find_packages(),
    install_requires=get_requirement_list(),
)
