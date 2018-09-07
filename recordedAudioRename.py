# ref : https://blog.csdn.net/qq_25883823/article/details/52749279
# ref : https://blog.csdn.net/u014717398/article/details/72627125
# location :  /Volumes/RV51mini/RECORD

from pydub import AudioSegment
import os, re, shutil
import time
# 循环目录下所有文件
prePath = '/Volumes/RV51mini/RECORD'
recordAudios = []
audioCreateTimes = []
dates = []
for filename in os.listdir(prePath):
    print(filename)
    if filename[0] != '.' and (filename[-4:] == '.WAV' or filename[-4:] == '.mp3'):
        print(filename)
        audioPath = prePath + '/' + filename

        audioCreateTime = time.strftime('%Y%m%d %H:%M:%S',time.localtime(os.path.getctime(audioPath)))
        print(audioCreateTime)
        date = audioCreateTime[2:8]
        print(audioPath)
        print(dates)
        print(prePath+'/'+ date)
        newFilePath = prePath + '/'+date
        if not os.path.exists(prePath+'/'+date):
            print('not in')
            dates.append(date)
            os.mkdir(newFilePath)
            shutil.move(audioPath, newFilePath+'/0.WAV')
            
        else:
            print(os.listdir(prePath+'/'+date))
            if os.listdir(prePath+'/'+date):
                maxIndex = max(os.listdir(prePath+'/'+date))[0]
                index = int(maxIndex) + 1
                shutil.move(audioPath, newFilePath+ '/' + str(index)+'.WAV')
            else:
                shutil.move(audioPath, newFilePath+'/0.WAV')
        recordAudios.append(filename)
        audioCreateTimes.append(audioCreateTime[2:])

print(recordAudios) 
print(audioCreateTimes)  
print(dates)     



