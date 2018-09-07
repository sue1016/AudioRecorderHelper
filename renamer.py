from pydub import AudioSegment
import os, re, shutil
import time

prePath = '/Volumes/RV51mini/'
filename = input("input the filename:")
filepath = prePath + filename 
for audioName in os.listdir(filepath):
    index  = audioName[-6:-4] 
    print(index)
    shutil.move(filepath+'/'+audioName, filepath+'/'+index+'.mp3')

