from setuptools import setup, find_packages

with open("requirements.txt","r") as f:
	requirements = f.readlines()

with open("README.md","r") as f:
	readme = f.read()

setup(
	name = "mlds6_project",
	version = "1.0.0",
	author = "Diego A. Lizarazo, David Castañeda, Luis A. Duque",
	author_email = "imdlizarazo@gmail.com",
	packages = find_packages(),
	install_requires = requirements,
	long_description = readme,
	long_description_content_type = "text/markdown",
	description = "Tablero para MLDS6",
	license = "MIT",
	url = "https://github.com/dalzoj/mlds6_project"
)