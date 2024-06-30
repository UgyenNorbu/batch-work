# `batch-work`: A Tool to Organize and Rename File

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
   ```

Replace <directory_path> with the path to the directory containing the files you want to sort. Recommended to `cd` to the directory that contains the folder you want to sort.

2. **File renaming**:
    ```bash
    bw_rename <prefix> <directory_path>
    ```

Replace <prefix> with the desired prefix for the files and <directory_path> with the path to the directory containing the files you want to rename. 
Recommended to `cd` to the directory that contains the folder whose contents you want to rename.

## Installation
Recommended method: Install the latest version:

    ```bash
    pip install batch-work
    ```

Or install from Github:

    ```bash
    pip install https://github.com/UgyenNorbu/batch-work/releases/download/v0.1.1/batch_work-0.1.2.tar.gz
    ```
## Dependencies
Package `tree` is required. Install the latest version:

    ```bash
    pip install tree
    ```

## Contributing
We appreciate your interest in contributing to the `batch-work` project. Your contributions can help improve this tool for everyone. Here's how you can get involved:

### Reporting Issues

If you encounter any bugs or have suggestions for improvements:

1. Check the [existing issues](https://github.com/UgyenNorbu/batch-work/issues) to see if it has already been reported.
2. If not, [open a new issue](https://github.com/UgyenNorbu/batch-work/issues/new), providing as much detail as possible:
   - Steps to reproduce the bug
   - Expected vs. actual behavior
   - Your environment (OS, Python version, etc.)
   - Any relevant screenshots or error messages

### Submitting Changes

To contribute code or documentation:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeatureName`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to your branch (`git push origin feature/YourFeatureName`)
6. Open a Pull Request against the `main` branch

### Questions or Suggestions

For general questions or suggestions about the `batch-work` project, please open a [new discussion](https://github.com/UgyenNorbu/batch-work/discussions) in our GitHub Discussions area.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## TODO 
- Add functions to delete empty folders
- Find dublicate files and delete
