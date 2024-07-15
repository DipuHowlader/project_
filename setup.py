from setuptools import find_packages, setup
from typing import List


E_dot = '-e .'

def read(fname)->List[str]:
    '''     
        this function will reutrn the list of requirements
    '''
    requirements = []
    with open(fname) as file_obj:
        requirements = file_obj.readlines()
    requirements = [req.replace('\n', "") for req in requirements]

    if E_dot in requirements:
        requirements.remove(E_dot)

    return requirements

setup(
    name = "ml_projects",
    version = "0.0.1",
    author = "dipu",
    author_email = "dipuhowlader33@gmail.com",
    description = ("My first ML Project"),
    license = "BSD",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=find_packages(),
    install_requires = read('requirements.txt')
)