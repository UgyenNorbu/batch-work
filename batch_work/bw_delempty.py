import os

def bw_delempty(directory_path):
    if not os.path.isdir(directory_path):
        print("This is not a folder")

    content = os.listdir(directory_path)
    if content == []:
        os.rmdir(directory_path)
        deleted_folder = os.path.basename(directory_path)
        print(f"{deleted_folder} >> deleted.")
        return
    else:
        if all(os.path.isfile(os.path.join(directory_path, f)) for f in content):
            all_files = os.path.basename(directory_path)
            print(f'{all_files} contains only files and cannot be deleted.')
        else:
            for f in content:
                item_path = os.path.join(directory_path, f)
                if os.path.isdir(item_path):
                    bw_delempty(item_path)