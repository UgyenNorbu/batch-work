from setuptools import setup, find_packages

setup(
    name="batch_work",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts':[
            'bw_rename=batch_work.main:main',
        ],
    },
)