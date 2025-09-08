import os
from functions.util import generate_paths
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the given content to a given file_path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file where to write the contents, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)


def write_file(working_directory, file_path, content):
    (curdir, abspath) = generate_paths(working_directory, file_path)

    if not abspath.startswith(curdir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abspath):
        try:
            os.makedirs(os.path.dirname(abspath), exist_ok=True)
        except Exception as e:
            return f"Error: {e}"

    with open(abspath, "w") as f:
        try:
            f.write(content)
        except Exception as e:
            return f"Error: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'



