# batchwork_tools to Organize and Rename File

## Introduction
This is a command-line utility tool written in Python that helps you organize and rename files in a directory. It sorts files into different folders based on their file extensions and renames files with a specified prefix.

## Features

1. **File sorting**: The script sorts files into the following categories:
   - Image files (.jpg, .png, .gif, etc.)
   - Audio files (.mp3, .wav, .flac, etc.)
   - Video files (.mp4, .avi, .mov, etc.)
   - Document files (.pdf, .doc, .txt, etc.)
   - Other files

2. **File renaming**: The script renames files in a directory with a specified prefix and sequential numbers.


## Usage

1. **File sorting**:
    ```bash
   bw_sort <directory_path>

Replace <directory_path> with the path to the directory containing the files you want to sort.

2. **File renaming**:
    ```bash
    bw_rename <prefix> <directory_path>

Replace <prefix> with the desired prefix for the files and <directory_path> with the path to the directory containing the files you want to rename.

## Installation
1. Clone the repository to your machine
    ```bash
    git clone https://github.com/UgyenNorbu/batchwork_tools.git

2. Navigate to the project directory:
    ```bash
    cd batchwork_tools

3. Run the command
    ```bash
    python setup.py install

For this, `setuptools` is required if not already installed. 
[You can install `setuptools` by running the command below;
    ```bash
    pip install setuptools
]

## Dependencies

## Contributing
## License
