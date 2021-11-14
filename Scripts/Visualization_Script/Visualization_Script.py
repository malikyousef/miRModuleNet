# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:33:28 2020

@author: goygokhanPC
"""

#import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#
#
#df = pd.read_excel('D:\\YaptigimCalismalar\\Malik Hoca\\Data Visualization\\whole_Results.xlsx')
#fig = plt.figure(num=None, figsize=(50, 15), dpi=300)
#index = ['BLCA-maTE',
#'BLCA-miRcorrNet',
#'BLCA-svm-rfe-8',
#'BLCA-svm-rfe-125',
#'BRCA-maTE',
#'BRCA-miRcorrNet',
#'BRCA-svm-rfe-8',
#'BRCA-svm-rfe-125',
#'KICH-maTE',
#'KICH-miRcorrNet',
#'KICH-svm-rfe-8',
#'KICH-svm-rfe-125',
#'KIRC-maTE',
#'KIRC-miRcorrNet',
#'KIRC-svm-rfe-8',
#'KIRC-svm-rfe-125',
#'KIRP-maTE',
#'KIRP-miRcorrNet',
#'KIRP-svm-rfe-8',
#'KIRP-svm-rfe-125',
#'LUAD-maTE',
#'LUAD-miRcorrNet',
#'LUAD-svm-rfe-8',
#'LUAD-svm-rfe-125',
#'LUSC-maTE',
#'LUSC-miRcorrNet',
#'LUSC-svm-rfe-8',
#'LUSC-svm-rfe-125',
#'PRAD-maTE',
#'PRAD-miRcorrNet',
#'PRAD-svm-rfe-8',
#'PRAD-svm-rfe-125',
#'STAD-maTE',
#'STAD-miRcorrNet',
#'STAD-svm-rfe-8',
#'STAD-svm-rfe-125',
#'THCA-maTE',
#'THCA-miRcorrNet',
#'THCA-svm-rfe-8',
#'THCA-svm-rfe-125',
#'UCEC-maTE',
#'UCEC-miRcorrNet',
#'UCEC-svm-rfe-8',
#'UCEC-svm-rfe-125'
#]
#
#barWidth = 0.04
#
#ax = fig.add_subplot(111) # Create matplotlib axes
#ax2 = ax.twinx()
#
#
#
##df = pd.read_excel('C:\\Users\\goygokhanPC\\Dropbox\\Samed_Burcue\\Results\\Figure Result Summary.xlsx')
#
#df.index=index;
#
#df.Number_Of_Genes.plot(kind='bar', color='green', ax=ax, width=barWidth, position=3,rot=0)
#df.Accuracy.plot(kind='bar',color='yellow',width=barWidth,position=2)
#df.Sensitivity.plot(kind='bar', color='black',width=barWidth, position=1)
#df.Area_Under_Curve.plot(kind='bar', color='red', ax=ax2, width=barWidth, position=0,rot=0)
#
#
#ax.set_ylabel('Number Of Genes',fontsize=15)
#ax2.set_ylabel('Area Under Curve',fontsize=15)
##ax.legend(loc='bottom center', bbox_to_anchor=(0.5, 1.05),ncol=3, fancybox=True, shadow=True)
#ax2.legend(loc='upper center', bbox_to_anchor=(0.595, 1),ncol=3, fancybox=True, shadow=True,fontsize=12)
#ax.legend(loc='upper center', bbox_to_anchor=(0.4, 1),ncol=3, fancybox=True, shadow=True,fontsize=12)
#
#
##ax.tick_params(axis='x', rotation=0,labelsize=20)
#ax.tick_params(axis='x',rotation=90,labelsize=10)
#
#plt.title(label="Cluster Level 2" , loc="center",fontsize=25)
#
#plt.show();


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 28}

plt.rc('font', **font)

df = pd.read_excel('C:\\Users\\GökhanGöy\\Dropbox\\Gokhan_Burcu\\miRModuleNet\\Manuscript\\Figures\\Figure_Z\\Data_Visualization\\UCEC\\Data\\UCEC_0.5.xlsx')
fig = plt.figure(num=None, figsize=(30, 10), dpi=75)
index = ['UCEC_1','UCEC_2','UCEC_3','UCEC_4','UCEC_5','UCEC_6','UCEC_7','UCEC_8','UCEC_9','UCEC_10'];

barWidth = 0.08

ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx()
#ax3 = ax.twinx()



#df = pd.read_excel('C:\\Users\\goygokhanPC\\Dropbox\\Samed_Burcue\\Results\\Figure Result Summary.xlsx')

df.index=index;

df.Number_Of_Genes.plot(kind='bar', color='#58D68D', ax=ax2, width=barWidth, position=0.3,rot=0)
df.Accuracy.plot(kind='bar',color='#F4D03F', ax=ax, width=barWidth,position=1.8)
df.Area_Under_Curve.plot(kind='bar', color='#3498DB', ax=ax, width=barWidth, position=3.5,rot=0)


ax.set_ylabel('Area Under Curve',fontsize=35)
ax2.set_ylabel('Number Of Genes',fontsize=35)
#ax3.set_ylabel('Accuracy',fontsize=25)
#ax.legend(loc='bottom center', bbox_to_anchor=(0.5, 1.05),ncol=3, fancybox=True, shadow=True)
ax2.legend(loc='lower center', bbox_to_anchor=(0.832, 1),ncol=3, fancybox=True, shadow=True,fontsize=35)
ax.legend(loc='lower center', bbox_to_anchor=(0.44, 1),ncol=3, fancybox=True, shadow=True,fontsize=35)
#ax3.legend(loc='lower center', bbox_to_anchor=(0.895, 1),ncol=3, fancybox=True, shadow=True,fontsize=30)

plt.rcParams.update({'font.size': 28})

#ax.tick_params(axis='x', rotation=0,labelsize=20)
ax.tick_params(axis='x',rotation=90,labelsize=35)
ax.grid();

plt.title(label="Group Level 2" , loc="left",fontsize=35)

plt.show();


