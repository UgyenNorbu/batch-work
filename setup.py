from setuptools import setup, find_packages

setup(
    name="batch-work",
    version="0.2.0",
    packages=find_packages(),
    license="MIT",
    author_email='unorbu2007@gmail.com',
    entry_points={
        'console_scripts':[
            'bw_rename=batch_work.main:main',
            'bw_sort=batch_work.main:main',
            'bw_delempty=batch_work.main:main',
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