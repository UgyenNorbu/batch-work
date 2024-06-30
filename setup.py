from setuptools import setup, find_packages

setup(
    name="batch_work",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts':[
            'bw_rename=batch_work.main:main',
            'bw_sort=batch_work.main:main'
        ],
    },
    install_requires=[
        "tree",
    ],
    author="Ugyen Norbu",
    description="CLI tool to organize and rename files.",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
)