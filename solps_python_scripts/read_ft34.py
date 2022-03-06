import numpy as np

def read_ft34(file):
   
   # cells = read_ft34(file)
   #
   # Read fort.34-files (nodes composing each triangle). 
   #
   #

   # Author: Wouter Dekeyser
   # E-mail: wouter.dekeyser@kuleuven.be
   # November 2016
   #
   # Re-writte in python by: Matteo Moscheni
   # E-mail: matteo.moscheni@tokamakenergy.co.uk
   # February 2022

   fid = open(file, "r")

   ## Read data

   # number of triangels
   ntria = int(fid.readline().split()[0])

   cells = np.zeros((ntria,3))

   for i in range(ntria):
      line = fid.readline().split()
      for j in range(1, len(line)):
         cells[i, j - 1] = int(line[j]) - 1

   # close file
   fid.close()

   return cells
