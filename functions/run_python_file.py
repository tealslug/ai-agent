import os
import subprocess
from functions.util import generate_paths
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the the given python file with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="The optional arguments to pass to the Python file.",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
            ),
        },
    ),
)



def run_python_file(working_directory, file_path, args=[]):
    (curdir, abspath) = generate_paths(working_directory, file_path)

    if not abspath.startswith(curdir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abspath):
        return f'Error: File "{file_path}" not found.'
    if not os.path.isfile(abspath) or not abspath.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        res = subprocess.run(["python3", file_path] + args, cwd=curdir, timeout=30, capture_output=True, text=True)
    except Exception as e:
        return f"Error: executing Python file: {e}"

    output = []
    if res.stdout:
        output.append(f'STDOUT:\n{res.stdout}')
    if res.stderr:
        output.append(f'STDERR:\n{res.stderr}')
    if res.returncode != 0:
        output.append(f'Process exited with code {res.returncode}')

    return "\n".join(output) if output else "No output produced."
