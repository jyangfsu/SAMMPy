import setuptools
import sys

# trap someone trying to install flopy with something other than python 3
if not sys.version_info[0]==3:
    print('Sorry, Flopy not supported in your Python version')
    print('  Supported versions: 3')
    print('  Your version of Python: {}'.format(sys.version_info[0]))
    sys.exit(1)  

long_description = ''

setuptools.setup(
    name="sammpy",
    version="0.1.0",
    author="Jing Yang, Ming Ye",
    author_email="jyang7@fsu.edu, mye@fsu.edu",
    description="SAMMPy is a Python package for process sensitivity analysis under multiple models",
    long_description=long_description,
    install_requires=['SALib=1.3.8',
                      'numpy=1.18.1',
                      'matplotlib=3.1.3'],
    url="https://github.com/jyangfsu/SAMMPy",
    packages=setuptools.find_packages(),
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
