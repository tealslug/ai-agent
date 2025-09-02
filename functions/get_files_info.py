import os

def generate_paths(working_directory, directory):
    dir = os.path.join(working_directory, directory)
    curdir = os.path.abspath(os.getcwd()) + f"/{working_directory}"
    abspath = os.path.abspath(dir)
    return (curdir, abspath)

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

def run_python_file(working_directory, file_path, args=[]):
    pass

