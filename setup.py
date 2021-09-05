from setuptools import setup
import re


with open("plp/__init__.py", "r") as f:
    version = re.search("\"(([0-9]+\.){2}[0-9]+([abrf]c*)*)\"", f.read())

if not version:
    raise RuntimeError("Version set improperly.")
version = version.group(1)

with open("C:/Users/shlok/PyLangProcessor/README.rst", "r") as f:
    long_description = f.read()

packages = [
    'plp'
]

setup(
    name="PyLangProcessor",
    author="Shlok",
    author_email="wizard1net@gmail.com",
    url="https://github.com/Shlol762/PyLangProcessor",
    project_urls={
        "Issue Tracker": "https://github.com/Shlol762/PyLangProcessor/issues"
    },
    version=version,
    packages=packages,
    license="MIT",
    description="A speech pattern recognition and response module.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    python_requires=">=3.6.0",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ]
)
