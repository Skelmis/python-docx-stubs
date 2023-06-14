from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
    long_description = fh.read()

version = "0.8.11"

setup(
    name="python-docx-stubs",
    version=version,
    author="Skelmis",
    author_email="ethan@koldfusion.xyz",
    description="Stubs for python-docx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Homepage": "https://github.com/Skelmis/python-docx-stubs",
    },
    package_data={"docx-stubs": ["py.typed", "*.pyi", "**/*.pyi"]},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
