import setuptools
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="Pyschool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="Chad B. Hovey",
    name="pyschool",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    python_requires=">=3.9",
    url="https://github.com/hovey/pyschool",
    version="0.0.2",
)
