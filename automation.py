import os
import shutil

def organize_files(directory):
    """Organizes files in a directory by their extension.

    Args:
        directory: The path to the directory to organize.
    """

    for filename in os.listdir(directory):
        if filename == "organize_files.py" or filename == ".git": # Exclude script and .git
            continue
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            name, ext = os.path.splitext(filename)
            ext = ext[1:]  # Remove the leading dot
            if ext:  # Ensure there's an extension
                ext_folder = os.path.join(directory, ext)
                if not os.path.exists(ext_folder):
                    os.makedirs(ext_folder)
                shutil.move(filepath, os.path.join(ext_folder, filename))
            else: # Files with no extension
                no_ext_folder = os.path.join(directory, "no_extension")
                if not os.path.exists(no_ext_folder):
                    os.makedirs(no_ext_folder)
                shutil.move(filepath, os.path.join(no_ext_folder, filename))


if __name__ == "__main__":
    directory_to_organize = input("Enter the path to the directory you want to organize: ")

    # Remove quotes if they are provided by the user
    directory_to_organize = directory_to_organize.strip('"').strip("'")

    if os.path.exists(directory_to_organize):
        organize_files(directory_to_organize)
        print(f"Files in '{directory_to_organize}' organized successfully!")
    else:
        print(f"Error: Directory '{directory_to_organize}' not found.")