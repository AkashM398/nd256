import os
    
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    matching_files = []
    if os.path.isdir(path):
        for f_d in [f for f in os.listdir(path) if not f.startswith(".")]:
            if os.path.isdir(os.path.join(path, f_d)):
                matching_files = matching_files + find_files(suffix, os.path.join(path, f_d))
            elif f_d.endswith(suffix):
                matching_files.append(os.path.join(path, f_d))

    return matching_files

print(find_files(".c", "./testdir"))