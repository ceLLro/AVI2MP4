import os
import sys
import json
import threading


#################################################:

# usage: Convert every AVI file found in specified folder to MP4 file format. 

# python 'script_name' 'ffmpeg exe location' 'avi file path location'
# EG: python main.py "scripts/ffmpeg.exe" "scripts/videos/"

#ffmpegExe = sys.argv[1]
#aviFilePath = sys.argv[2]

################################################

#Modify below for your needs

ffmpegExe = "C:\\Users\\adria\\Desktop\\Github\\AVI2MP4\\ffmpeg-4.3-win64-static\\bin\\ffmpeg.exe"

aviFilePath = "C:\\Users\\adria\\Desktop\\Github\\nodejs_local_server\\videos\\"

files = []

def get_avi_file_path(source):
    for file in os.listdir(source):
        if file.endswith(".avi") or file.endswith(".AVI"):
            files.append(source + file)

def convert_avi_to_mp4(avi_file_path, output_name):
    # print(
    # "{f} -i {input} -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f "
    # "mp4 {output}.mp4".format(
    # f=ffmpegExe, input=avi_file_path, output=output_name))

    os.popen("{f} -i {input} -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict "
             "experimental -f mp4 {output}.mp4".format(f=ffmpegExe, input=avi_file_path, output=output_name))

    return True


# get all avi files in specified folder
get_avi_file_path(aviFilePath)

threads = []
print("Start? yes/no")
if(input() == 'yes'):
    try:
        for f in files:
            t = threading.Thread(target=convert_avi_to_mp4, args=(str("\"" + f + "\""), str("\"" + f + "\"")))
            threads.append(t)
            t.start()
    except:
        print("Some error occured")
        sys.exit()
else:
    sys.exit()

