from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    HYPHEN_E_DOT = '-e .'
    Requirements=[]
    with open(file_path) as file_obj:
        Requirements=file_obj.readlines()
        Requirements=[req.replace("/n","") for req in Requirements]

        if HYPHEN_E_DOT in Requirements:
            Requirements.remove(HYPHEN_E_DOT)

    return Requirements

setup(
name='E-2-EMLPROJECT',
version='0.0.1',
author='Megha',
author_email='meghakansal1201@gmail.com',
packages=find_packages(),
install_requires=get_requirements('Requirements.txt')

)