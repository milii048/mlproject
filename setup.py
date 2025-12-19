from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
  with open(file_path, 'r') as file_obj:
    requirements=file_obj.read().splitlines()
    if '-e .' in requirements:
      requirements.remove('-e .')
  return requirements

setup(
  name='mlproject',
  version='0.0.1',
  author='Milind',
  author_email='milind.brt@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
)
