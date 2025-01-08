import os
import shutil


def copy_files_to_destination(source_dir: str, destination_dir: str):
    """
    Copies files from one source to a destination
    """
    # Delete contents in destination directory
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)

    os.mkdir(destination_dir)

    if not os.path.exists(source_dir):
        raise ValueError("Directory not found")
    # Copy all files and subdirectories
    contents = os.listdir(source_dir)

    for content in contents:
        content_path = os.path.join(source_dir, content)
        if os.path.isfile(content_path):
            destination_path = os.path.join(destination_dir, content)
            shutil.copy(content_path, destination_path)
        else:
            source_path = os.path.join(source_dir, content)
            destination_path = os.path.join(destination_dir, content)
            os.mkdir(destination_path)
            copy_files_to_destination(source_path, destination_path)
