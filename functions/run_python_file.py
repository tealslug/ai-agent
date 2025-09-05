import os
import subprocess
from functions.util import generate_paths


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
