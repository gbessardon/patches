# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:45:02 2019

@author: gbessardon
"""
import numpy as np

#reads the cover fraction data from ECOCLIMAP_II and ECOCLIMAP_SG
#filename='/home/gbessardon/ECOCLIMAP/ECOCLIMAP_II_cover_data.csv'

def cover_fraction(filename):
    data=open(filename)
    covernum=[]
    covername=[]
    cityfrac=[]
    vegfrac=[]
    inwaterfrac=[]
    seafrac=[]
    for i,d in enumerate(data):
        if i==0:
            fieldnames=d.split(',')
        else:
#            print(d.split(','))
            covernum.append(int(d.split(',')[0]))
            covername.append(d.split(',')[1])
            cityfrac.append(float(d.split(',')[2]))
            vegfrac.append(float(d.split(',')[3]))
            inwaterfrac.append(float(d.split(',')[4]))
            seafrac.append(float(d.split(',')[5]))
    return(fieldnames,np.array(covernum),covername,np.array(cityfrac),np.array(vegfrac),
           np.array(inwaterfrac),np.array(seafrac))




def convert_to_cover_fraction(DSG,cityfrac):
    Tfrac=np.zeros(DSG.shape)
    for i, c  in enumerate(cityfrac):
        idi=np.where(DSG==i+1)
        Tfrac[idi]=c
    return(Tfrac)