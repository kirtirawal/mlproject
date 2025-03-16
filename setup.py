from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    HYPHEN_E_DOT = "-e ."
    
    requirements = []
    
    with open('requirements.txt') as file_obj:
        requirements =  file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Kirti Rawal',
    packaages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)