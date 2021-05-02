#!/usr/bin/env python3
"""File Renamer Program"""

# from datetime import datetime
import os


def file_renamer():
    path = input("What is the folder/directory location of the files? ")
    start_of_name = input("What should the beginning of each file be called? ")
    start_number = input("What number should the files start being numbered at? ")
    file_number = int(start_number)

    for file_name in os.listdir(path):
        # date = datetime.fromtimestamp(os.path.getctime(file_name)).strftime('%m_%d_%Y-%H_%M_%S')
        if file_name.lower().endswith(".png"):
            os.rename(os.path.join(path,file_name), os.path.join(path, start_of_name + file_number + ".png"))
            file_number = file_number + 1
        elif file_name.lower().endswith(".jpg"):
            os.rename(os.path.join(path,file_name), os.path.join(path, start_of_name + file_number + ".jpg"))
            file_number = file_number + 1
        elif file_name.lower().endswith(".jpeg"):
            os.rename(os.path.join(path,file_name), os.path.join(path, start_of_name + file_number + ".jpeg"))
            file_number = file_number + 1
        elif file_name.lower().endswith(".mp4"):
            pass


if __name__ == '__main__':
    file_renamer()
