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
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="Example Author",
    maintainer_email="author@example.com",
    name="zmath",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    python_requires=">=3.8",
    url="https://github.com/pypa/sampleproject",
    version="0.0.10",
)
