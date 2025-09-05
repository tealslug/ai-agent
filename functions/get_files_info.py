import os
import subprocess
from functions.util import generate_paths


def get_files_info(working_directory, directory="."):
    (curdir, abspath) = generate_paths(working_directory, directory)

    if not abspath.startswith(curdir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abspath):
        return f'Error: "{directory}" is not a directory'

    items = []
    for item in sorted(os.listdir(abspath)):
        d = os.path.join(abspath, item)
        items.append(f" - {item}: file_size={os.path.getsize(d)} bytes, is_dir={os.path.isdir(d)}")

    return "\n".join(items)
