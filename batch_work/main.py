import os
import sys

def bw_rename(directory_path, prefix):
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        return
    
    directory_name = os.path.basename(directory_path)
    
    files = []
    for f in os.listdir(directory_path):
        full_path = os.path.join(directory_path, f)
        if os.path.isfile(full_path):
            files.append(f)
    
    files.sort()
    
    for index, filename in enumerate(files, start=1):
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{prefix}_{index}{file_extension}"
        os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
        print(f"Renamed: {filename} -> {new_filename}")

def main():
    if len(sys.argv) != 3:
        print("Enter a directory path as an argument.")
        print("Usage: bw_rename <prefix> <directory_path>")
        sys.exit(1)

    prefix = sys.argv[1]
    directory_path = sys.argv[2]
    bw_rename(directory_path, prefix)

if __name__ == "__main__":
    main()