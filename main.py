__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile


def clean_cache():
    path = r"C:\Winc\files\cache"
    if os.path.isdir(path):  # if map exists,
        shutil.rmtree(path)  # remove map and all contents (including subdirs)

    os.mkdir(path)
    return


def cache_zip(zip_file_path, cache_dir_path):
    # if  (os.path.exists(str(zip_file_path)) == True
    # and os.path.exists(str(cache_dir_path)) == True):  #Check not necessary, following wincpy !
    with zipfile.ZipFile(str(zip_file_path), mode="r") as archive:
        archive.extractall(str(cache_dir_path))
    return


def cached_files():
    path = r"C:\Winc\files\cache"
    pathnames = []
    filenames = os.listdir(path)

    for file in filenames:
        path_test_file = os.path.join(path, file)
        if os.path.isfile(path_test_file):
            pathnames.append(os.path.join(path, file))
    return pathnames


def find_password(filenames):
    line_password = ""
    end_loop = False

    for filename in filenames:
        file = open(str(filename), "r")
        end_loop = False
        for line in file:
            index = line.find("password")
            if index != -1:
                index_space = line.find(" ")
                index_newline = line.find("\n")
                line_password = line[index_space + 1 : index_newline]
                end_loop = True
                break
        file.close()
        if end_loop:  # if password is found, also escape the main loop
            break

    return line_password


# clean_cache()
# cache_zip("data.zip", "cache")
# cache_test = []
# cache_test = cached_files()
# print(cache_test)
# print(find_password(cache_test))

# print(cached_files())
# print('getcwd:', os.getcwd())
# cache_zip("/Winc/files/data.zip", "/Winc/files/cache")
# cache_zip("data.zip", "cache")

# if os.path.exists("/Winc/files"):
# if os.path.exists("\\Winc\\files"):
# if os.path.exists("C:\\Winc\\files"):
# if os.path.exists("C:/Winc/files"):
#    print("ja")
# else:
#    print("nee")
# print('getcwd:', os.getcwd())
