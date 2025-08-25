import os

def get_files_info(working_directory, directory="."):
    dir = os.path.join(working_directory, directory)
    curdir = os.path.abspath(os.getcwd()) + f"/{working_directory}"
    abspath = os.path.abspath(dir)
    if not abspath.startswith(curdir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abspath):
        return f'Error: "{directory}" is not a directory'

    items = []
    for item in sorted(os.listdir(abspath)):
        d = os.path.join(abspath, item)
        items.append(f" - {item}: file_size={os.path.getsize(d)} bytes, is_dir={os.path.isdir(d)}")

    return "\n".join(items)

def get_file_content(working_directory, file_path):
    dir = os.path.join(working_directory, file_path)
    curdir = os.path.abspath(os.getcwd()) + f"/{working_directory}"
    abspath = os.path.abspath(dir)
    if not abspath.startswith(curdir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abspath):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000
    with open(abspath, "r") as f:
        file_content_string = f.read(MAX_CHARS)

    if os.path.getsize(abspath) >= MAX_CHARS:
        file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

    return file_content_string
