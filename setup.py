from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    requirement_list:List[str] = []

    """
    Write a code to read requirements.txt file and append each requireements in requirement_list variable.
    
    """
    return requirement_list


setup(

    name="sensor",
    version="0.0.1",
    author="ganesh",
    author_email="ganeshkumarjasti19@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)

