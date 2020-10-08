import setuptools

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
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    url="https://github.com/pypa/sampleproject",
    version="0.0.8",
)
