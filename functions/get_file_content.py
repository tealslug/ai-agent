import os
from functions.util import generate_paths
from google.genai import types


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content from a file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file whose contents to get, relative to the working directory.",
            ),
        },
    ),
)


def get_file_content(working_directory, file_path):
    (curdir, abspath) = generate_paths(working_directory, file_path)

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



