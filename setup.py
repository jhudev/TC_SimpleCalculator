from setuptools import setup, find_packages

VERSION = "0.0.1" 
DESCRIPTION = "A simple calculator for basic arithmetics"
LONG_DESCRIPTION = """
The python package for "Calculator" class, which stores a number and
provides basic math operations (e.g, add, subtract, multiply, divide, root).
Values are cumulative and can be initially set and continually reset.
""".replace('\n',"")

# Setting up
setup(
      name = "mycalculator", 
      version = VERSION,
      author = "Jesse Huang",
      author_email = "<jessehuang80@email.com>",
      description = DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      packages = find_packages(),
      install_requires = [],
      keywords = ["calculator", "math",
                  "addition", "subtraction", "multiplication", "division",
                  "root"],
      license = "MIT",
      classifiers = [
          "Development Status :: 4 - Beta",
          "Intended Audience :: Education",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
          ]
)