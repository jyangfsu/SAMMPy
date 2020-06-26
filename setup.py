import setuptools

long_description = ''

setuptools.setup(
    name="sammpy",
    version="0.1.0",
    author="Jing Yang; Ming Ye",
    author_email="mye@fsu.edu",
    description="Process sensitivity analysis under multiple models",
    long_description=long_description,
    install_requires=['SALib>=1.3.8',
                      'numpy>=1.18.1'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
