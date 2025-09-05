import os
from functions.util import generate_paths

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



