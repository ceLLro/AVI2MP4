import os
import sys


aviFilePath = "c:\\Users\\adria\\Desktop\\Github\\Local_server\\videos\\"

files = []

def get_avi_file_path(source):
    idx = 0
    for file in os.listdir(source):
        if file.endswith(".mp4") or file.endswith(".MP4"):
            files.append("{" + "\"Index\""":" + str(
                idx) + "," + "\"Path\""":" + '"' + source + file + '"' + "," + "\"FileName\""":" + '"' + file + '"' + "}")
            idx = idx + 1
    ff = str(files)

    with open('data.json', 'w') as f:
        f.write(ff)
        f.close()

get_avi_file_path(aviFilePath)
print("done")
