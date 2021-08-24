from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in loan_management/__init__.py
from loan_management import __version__ as version

setup(
	name="loan_management",
	version=version,
	description="Loan Management System",
	author="Akshaya Prisha",
	author_email="akshayaprishap@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
