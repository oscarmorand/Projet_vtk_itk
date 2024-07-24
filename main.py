################### Kael Facon
# ITK/VTK Project # Samuel Goncalves
################### Oscar Morand

from readData      import readData
from alignData     import alignData
from segmentData   import segmentData
from analyseData   import analyseData
from visualizeData import visualizeData

if __name__ == '__main__':
    dataPath = "Data/"
    scan1, scan2 = readData(path)
    scan2 = alignData(scan1, scan2)
    segmentation1, segmentation2 = segmentData(scan1, scan2)
    evolution = analyseData(segmentation1, segmentation2)
    visualizeData(evolution)
