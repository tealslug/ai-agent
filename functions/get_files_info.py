import os
from functions.util import generate_paths
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


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
