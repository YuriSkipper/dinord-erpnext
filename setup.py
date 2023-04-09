from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dinord_erpnext_customization/__init__.py
from dinord_erpnext_customization import __version__ as version

setup(
	name="dinord_erpnext_customization",
	version=version,
	description="Different customizations",
	author="Dinord Yury Kovalenko",
	author_email="yukovalenko@dinord.ru",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
