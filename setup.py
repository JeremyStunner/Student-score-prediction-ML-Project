from setuptools import find_packages,setup
from typing import List

p_key = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of required packages'''
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if p_key in requirements:
            requirements.remove(p_key)

        return requirements

setup(
name= 'mlproject',
version= '0.0.1',
author= 'jeremy',
author_email= 'engrjeremystunner@gmail.com',
packages= find_packages(),
install_requires= get_requirements('requirements.txt')
)