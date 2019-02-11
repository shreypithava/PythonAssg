# this function returns a set of file names
# including their paths, e.g.,
# start/38ask9sd/adsf928/saf828a/blub.lnk
# the output is hard coded; their should be no executed
# code in this function!
import os


def file_path(starting_path, lists=[]):
    for i in os.listdir(starting_path):
        try:
            if '.' not in i:
                file_path(starting_path + '/' + i, lists)
            else:
                lists.append(starting_path + '/' + i)
        except NotADirectoryError:
            lists.append(starting_path + '/' + i)
    return set(lists)


def get_files():
    list_of_paths = file_path('start')
    print(list_of_paths)
    return set(list_of_paths)


# return {}


# this function only returns the file names (without the path)
# it should use get_files() to create the return value
def get_file_names():
    files_list = []
    A = get_files()
    for path in A:
        index_rem = 0
        for index in range(len(path)):
            if path[len(path) - index - 1] != '/':
                index_rem += 1
            else:
                break
        files_list.append(path[len(path) - index_rem:])
    return set(files_list)


# this function returns a set containing
# the full path to a capitalized folder
# start/38ask9sd/ADSF928/
# the output is hard coded; their should be no executed
# code in this function!
def get_cap_folders(starting_path='start', lists=[]):
    for i in os.listdir(starting_path):
        try:
            for letter in i:
                if letter.isupper():
                    lists.append(starting_path + '/' + i)
                    break
            get_cap_folders(starting_path + '/' + i, lists)
        except NotADirectoryError:
            continue
    return set(lists)


# parses the folder structure and prints
# the paths to the files and upper case
# folders respectively
# note: this function is not evaluated by the unit tests;
#  we will verify it manually by running it!
def parse_folder_structure(start='start'):
    print("all upper case folder paths'")
    print("all file paths'")


# if you implemented additional things, please
# copy below
print(get_file_names())
print(get_cap_folders())
