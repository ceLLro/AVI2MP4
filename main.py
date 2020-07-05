import os, sys

#usage: Convert every AVI file found in specified folder to MP4 file format. 

#python 'script_name' 'ffmpeg exe location' 'avi file path location'
#EG: python main.py "scripts/ffmpeg.exe" "scripts/videos/"


ffmpegExe = sys.argv[1]

aviFilePath = sys.argv[2]


ffmpegExe = "ffmpeg-4.3-win64-static\\bin\\ffmpeg.exe"

files = []

def get_avi_file_path(source):
    for file in os.listdir(source):
        if file.endswith(".avi") or file.endswith(".AVI"):
            files.append(source + file)
    print(files)


def convert_avi_to_mp4(avi_file_path, output_name):
    os.popen("{f} -i {input} -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 {output}.mp4".format(f = ffmpegExe, input = avi_file_path, output = output_name))
    return True

#get all avi files in specified folder
get_avi_file_path(aviFilePath)

for f in files:
    convert_avi_to_mp4(f, f)