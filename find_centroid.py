from multiprocessing import Pool
from pathlib import Path
import shutil
import sys
import numpy as np
import OpenEXR
import cv2
import glob
import os
import Imath
import array
import matplotlib.pyplot as plt
import pandas as pd
import csv
import math
from tqdm import tqdm



### CALC CENTROID FOR EACH FOLDERS AND SORT FILES AND SAVE IN SEPARATE TEXT FILES #####
def Readexr_file(common_dir):
  a=[];dirs=list();
  sub_df = pd.DataFrame(columns=["folder_names", "file_names"])
  for directory, subdir, files in os.walk(common_dir):
    #print('files',files)
    #print('dir',directory)
    if directory.endswith('exr_f'):
      #print(directory)
      dirs.append(directory)
  #print('dirs',dirs)
  for i in range(len(dirs)): # iterate thru directory path list
    a=dirs[i]
    listfiles=list()
    #print('a',a)
    for files in os.listdir(a): 
      listfiles.append(files.split('.')[0])  
    batch_df = pd.DataFrame({"folder_names": a,"file_names":listfiles}) 
    sub_df = pd.concat([sub_df, batch_df])
    #print(sub_df) 
  df = sub_df.groupby('folder_names')['file_names'].apply(list).reset_index(name="dummy")
  df["dummy"] = df["dummy"].apply(lambda x: sorted(list(x))) 
  #df.to_csv('csv_arun1.csv',index=False)  
  return df  
 

def calc_centroid(path):
  I = OpenEXR.InputFile(path)
  dw = I.header()['displayWindow']
  size = (dw.max.y - dw.min.y + 1, dw.max.x - dw.min.x + 1)
  FLOAT = Imath.PixelType(Imath.PixelType.FLOAT)
  (U)=[array.array('f', I.channel(Chan, FLOAT)).tolist() for Chan in ("U")]
  u_data = np.array(U).reshape(2048,2048)
  u_nonzero_indices=np.array(np.transpose(np.nonzero(u_data)))
  #print(u_nonzero_indices)
  first=u_nonzero_indices[0]
  #print('first is',first)
  last=u_nonzero_indices[len(u_nonzero_indices)-1]
  #print('last is',last)
  xmin_u=first[0]; ymin_u=first[1]; xmax_u=last[0]; ymax_u=last[1] 
  centroid_per_image_Uchan= (math.ceil((xmin_u+xmax_u)/2), math.ceil((ymin_u+ymax_u)/2))
  #centroid_all.append(centroid_per_image_Uchan) 
  #df_centroid = pd.DataFrame(centroid_all)  
  return centroid_per_image_Uchan
  
  
def main():
  common_dir='/mnt/dst_datasets2/own_omni_dataset/omniflow/'
  df=Readexr_file(common_dir)
  for i in tqdm(range(len(df))):
    row=df.iloc[i]
    #print('row',row)
    fileroot=row.folder_names
    dummy=row.dummy              #LIST
    filename=fileroot.split('/')[5]
    #print (filename) 
    a=[]  
    for j in dummy:
      sus=fileroot+'/'+j+'.exr'
      #print('sus',sus)
      centroid_real=calc_centroid(sus)
      a.append(centroid_real)
      with open(filename+'_'+j+'.txt','w') as f:
       f.write(str(a))  

main() 

def plot():
  fig, ax = plt.subplots(figsize=(10, 10))
  ax.add_patch(plt.Circle((1024,1024),1024,fill=False,lw=0.1))
  for txtfiles in tqdm(os.listdir('savedtxt/')):
    tupleList=[]
    with open('savedtxt/'+txtfiles, 'r') as infile:
      for line in infile:
        line=line.replace(' ', '')
        line_split = line.split()
        #print('line_split',line)
      for l in line_split:
        tupleList.append(createTuple(l))
      arr=np.array(tupleList)        
      #print('arr',arr)
      x,y=arr.T
      strt_x=x[0]              ## x array of starting points to be plotted in red
      strt_y=y[0]              ## y array of starting points to be plotted in red
      #print(rep_y.shape)
      rest_x = x[1::]
      rest_y = y[1::]
      plt.scatter(rest_x,rest_y,s=0.2,c='b',alpha=0.6)
      plt.scatter(strt_x,strt_y,s=0.6,c='r',alpha=0.5)
  plt.Circle((1024,1024),1024,fill=False,lw=0.1)
  ax.xaxis.tick_top()
  plt.xlim(0, 2048)
  plt.ylim(0, 2048)
  ax.invert_yaxis()
  plt.xlabel('centroid of persons in x direction')
  plt.ylabel('centroid of persons in y direction')
  plt.title('Scatter plot of centroids of all optical forward flow objects')
  plt.savefig('centroid11.pdf',bbox_inches='tight')
  #plt.show()
  return 0
  
plot()     





