import os
import sys
import subprocess

def bw_sort(directory_path):
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a directory.")
        return

    if len(os.listdir(directory_path)) == 0:
        print(f"Error: {directory_path} is empty.")
        return

    image_ext = ['.jpg', '.jpeg','.png', '.gif', '.tiff', '.tif', '.bmp', '.webp', '.svg', '.raw', '.psd', '.ai','.eps','.ico','.heic', '.heif']
    audio_ext = ['.mp3', '.wav', '.aac', '.ogg', '.flac', '.m4a', '.wma', '.aiff', '.alac', '.mid', '.midi', '.amr', '.ape', '.opus', '.ra', '.rm', '.wv', '.webm', '.ac3', '.dts']
    movie_ext = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp', '.rmvb', '.vob', '.ts', '.divx', '.asf']
    document_ext = ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.html', '.htm', '.xml', '.md', '.pages', '.numbers', '.key', '.odp', '.ods']

    for f in os.listdir(directory_path):
        file_ext = os.path.splitext(f)[1]
        file_ext = file_ext.lower()

        if file_ext in image_ext:
            path_to_new_dir = os.path.join(directory_path, "Image_files")
            os.makedirs(path_to_new_dir, exist_ok=True)
            source = os.path.join(directory_path, f)
            destination = os.path.join(path_to_new_dir, f)
            os.rename(source, destination)
            continue

        elif file_ext in audio_ext:
            path_to_new_dir = os.path.join(directory_path, "Audio_files")
            os.makedirs(path_to_new_dir, exist_ok=True)
            source = os.path.join(directory_path, f)
            destination = os.path.join(path_to_new_dir, f)
            os.rename(source, destination)
            continue
        
        elif file_ext in movie_ext:
            path_to_new_dir = os.path.join(directory_path, "Movie_files")
            os.makedirs(path_to_new_dir, exist_ok=True)
            source = os.path.join(directory_path, f)
            destination = os.path.join(path_to_new_dir, f)
            os.rename(source, destination)
            continue

        elif file_ext in document_ext:
            path_to_new_dir = os.path.join(directory_path, "Document_files")
            os.makedirs(path_to_new_dir, exist_ok=True)
            source = os.path.join(directory_path, f)
            destination = os.path.join(path_to_new_dir, f)
            os.rename(source, destination)
            continue
        
        else:
            path_to_new_dir = os.path.join(directory_path, "Other_files")
            os.makedirs(path_to_new_dir, exist_ok=True)
            source = os.path.join(directory_path, f)
            destination = os.path.join(path_to_new_dir, f)
            os.rename(source, destination)

    print('File sorting completed and structured as below: \n')
    subprocess.run(["tree", directory_path], check=True)