import os

def generate_paths(working_directory, directory):
    dir = os.path.join(working_directory, directory)
    curdir = os.path.abspath(os.getcwd()) + f"/{working_directory}"
    abspath = os.path.abspath(dir)
    return (curdir, abspath)
