from os import (
    getcwd,
    listdir,
    mkdir,
    path,
    replace
)


def is_hidden_file(file_name):
    return path.basename(file_name).startswith('.')


def sort_file(directory_path):
    dir_content = listdir(directory_path)
    dir_content.remove(path.basename(__file__))
    for file_name in dir_content:
        extension = file_name.split('.')[-1]
        extension_dir = path.join(directory_path, extension)
        if not is_hidden_file(file_name):
            if not path.isdir(extension_dir):
                mkdir(extension_dir)
            replace(path.join(directory_path, file_name), path.join(directory_path, extension, file_name))


if __name__ == '__main__':
    sort_file(directory_path=getcwd())
