#!/usr/bin/env python3
"""File Renamer Program"""

import os


def file_renamer():
    path = input("What is the folder/directory location of the files? ")
    file_names = input("What should the beginning of each file be called? ")
    start_number = input("What number should the files start being numbered at? ")
    file_number = int(start_number)

    for filename in os.listdir(path):
        if filename.lower().endswith(".png"):
            os.rename(os.path.join(path,filename), os.path.join(path, file_names + str(start_number)+'.png'))
            file_number = file_number + 1
        elif filename.lower().endswith(".jpg"):
            os.rename(os.path.join(path,filename), os.path.join(path, file_names + str(start_number)+'.jpg'))
            file_number = file_number + 1
        elif filename.lower().endswith(".jpeg"):
            os.rename(os.path.join(path,filename), os.path.join(path, file_names + str(start_number)+'.jpeg'))
            file_number = file_number + 1
        elif filename.lower().endswith(".mp4"):
            pass


if __name__ == '__main__':
    file_renamer()
