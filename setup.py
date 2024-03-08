from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'
def get_requirements():
    with open('requirements.txt', 'r') as file:
        if 'HYPEN_E_DOT' in file.read():
            return file.read().replace('HYPEN_E_DOT', '').splitlines()
        return file.read().splitlines()
setup(
    name="SPE_Project",
    version="0.1",
    author="Samith10",
    author_email="samithabesinghe1999@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)