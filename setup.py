from setuptools import setup,find_packages
from typing import List 


HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    """
    This Function will return the list of requirements 

    """
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements] ## to remove next line scenario requirements.txt

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup (
name='ML-Project01',
version="0.0.1",
author='AbhishekHaveri',
author_email='abhishekghaveri@gmail.com',
packages=find_packages(),
install_requires =get_requirements('requirements.txt')

)