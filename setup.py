
from setuptools import find_packages, setup

version = "0.0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="DEFACTO_84K_SEGMENTACION",
    version=version,
    description="DEFACTO_84K_SEGMENTACION",
    long_description=long_description,
    url="https://github.com/Gradiant/ai-dataset-DEFACTO_84K_SEGMENTACION",
    author="Gradiant",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
)