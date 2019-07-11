#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Cut audio function 
# Input: source, dst, start, end
from pydub import AudioSegment

def takeAudioSegment(source, dst, start, end):
    #source: path to source audio file 
    #dst: destination to audio file 
    start = start * 1000 # Pydub works in milliseconds
    end = end * 1000 # Pydub works in milliseconds
    src_Audio = AudioSegment.from_wav(source)
    #Cut the right part
    output_audio = src_Audio[start:end]
    #Export the file 
    output_audio.export(dst, format="wav") 


# In[ ]:


import os
#need to convert and write to another metadata
def split_by_label(source_path, dst_path, label_path):
    filenames = os.listdir(source_path)
    metaInfo=[["",""]]
    for filename in filenames:
        filename =  filename.split(".")[0] #take the file name without dot
        #get wav file name path
        wav_path = source_path + filename + ".wav"
        #get label filename path
        csv_path = label_path + filename + ".txt"
        #read the label file path 
        label = pd.read_csv(csv_path, delim_whitespace= True)
        #Loop all over the csv file in print start:end, 
        i = 0   
        for index, row in label.iterrows():
            print (i)      
            start = row['Start']
            print("start:" + str(start))
            end = row['End']
            print("start:" + str(end))
            status = row['Status']
            output_name = str(i) + "-" + status + "-" + filename +".wav"
            dst = dst_path + output_name
            print("dst = " + dst)
            takeAudioSegment(wav_path, dst, start, end)
            #write the metadata file 
            metaInfo.append([output_name, status])
            i += 1
        #save the metadata file
        df = pd.DataFrame(metaInfo, columns = ['File_name', 'Label']) 
        df.to_csv(dst_path + "result.csv", sep='\t', encoding='utf-8')
     

    


# In[ ]:


inputPath = "C:/Users/tupa7/Desktop/Do An/Datasets/Breath_datasets_wav/Test/input/"
outputPath = "C:/Users/tupa7/Desktop/Do An/Datasets/Breath_datasets_wav/Test/output/"
labelPath = "C:/Users/tupa7/Desktop/Do An/Datasets/Breath_datasets_wav/Test/label/"

split_by_label(inputPath, outputPath, labelPath)


# In[ ]:





# In[ ]:




