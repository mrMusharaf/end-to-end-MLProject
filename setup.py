from setuptools import find_packages, setup
from typing import List

Hyphen_e_Dot = "-e ."
def get_requirements(file_path:str)-> List[str]:
    #This function will return the list of the requirements
    requirements = []
    
    with open(file_path) as file_obj:
        
        requirements = file_obj.readlines()
        
        requirements = [req.replace("\n"," ") for req in requirements]
        
        if Hyphen_e_Dot in requirements:
            requirements.remove(Hyphen_e_Dot)
    return requirements



    
    
    
setup(
    
    name= 'mlproject',
    version='1.0',
    author='mrMusharaf',
    author_email='musharafhere@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)