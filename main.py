# Demo Converter v1.2

import os
# import moviepy
# import PIL
import shutil
from moviepy.editor import *
from PIL import Image

# path = os.path.dirname(os.path.dirname(os.path.realpath(sys.executable)))

INPUT_FILES = input("输入文件：")

INPUT_FILES = INPUT_FILES.replace("'", "")
dirName, originName = os.path.split(INPUT_FILES)
footageName = originName.replace('.mov', '')
sequenceDirName = dirName+f'/_{footageName}_Sequence'
os.mkdir(sequenceDirName)
outputVideoName = footageName + '_Demo.mp4'
outputVideo = os.path.join(dirName, outputVideoName)

# print(dirName)
# print(originName)
# print(footageName)
# print(sequenceDirName)
# print(outputVideoName)
# print(outputVideo)


# 转JPG序列
clip = VideoFileClip(INPUT_FILES)
fps = clip.reader.fps

for i, frame in enumerate(clip.iter_frames()):
    newSequenceFilepath = os.path.join(sequenceDirName, f"{i}.jpg")
    # print(f"frame at {i} seconds saved at {new_img_filepath}")
    newImg = Image.fromarray(frame)
    newImg.save(newSequenceFilepath)
    print(f"{i} ")


# 转MP4视频

this_dir = os.listdir(sequenceDirName)
filepaths = [os.path.join(sequenceDirName, fname)
             for fname in this_dir if fname.endswith("jpg")]

directory = {}

for root, dirs, files in os.walk(sequenceDirName):
    for fname in files:
        filepath = os.path.join(root, fname)
        try:
            key = float(fname.replace(".jpg", ""))
            # print(key)
        except:
            key = None
        if key != None:
            directory[key] = filepath

newPaths = []
for k in sorted(directory.keys()):
    # print(k)
    filepath = directory[k]
    newPaths.append(filepath)

clip = ImageSequenceClip(newPaths, fps)
clip.write_videofile(outputVideo)


# mp4 to m4v
os.rename(outputVideo, outputVideo.replace(".mp4", ".m4v"))


# Delete Sequence
shutil.rmtree(sequenceDirName)
