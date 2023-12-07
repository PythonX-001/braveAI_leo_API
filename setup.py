from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="braveAi-leo",
    version="0.1.0",
    author="salah ch",
    author_email="salahch535@gmail.com",
    description="Python wrapper for Brave's Leo AI chat functionality based on Llama",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PythonX-001/braveAI_leo_API",
    packages=find_packages(),
    classifiers=[

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=requirements,
    python_requires=">=3.6",
)
