from setuptools import setup, find_packages

setup(
    name='jFormat',
    version='0.0.1',
    description='reformats json file to stdout',
    install_requires= ['click', 'colorama'],
    entry_points="""
    [console_scripts]
    jFormat=jFormat.main:main
    """,
    author='me!',
    author_email='metoo@hotmail.com',
    packages=find_packages()
)