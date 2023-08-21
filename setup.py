from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='article-generator',
    version='1.0',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'article-generator = src.mymodule.summarization:main'  # Change this to your main script
        ]
    },
    author='K.Prashanth',
    author_email='prashanth010171995@gmail.com',
    description='Article Generator Project',
    url='https://github.com/techwithaibuddies/article-generator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
