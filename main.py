################### Kael Facon
# ITK/VTK Project # Samuel Goncalves
################### Oscar Morand

from readData      import readData
from alignData     import alignData
from segmentData   import segmentData
from analyseData   import analyseData
from visualizeData import visualizeData

if __name__ == '__main__':
    print("Start")
    dataPath = "Data/"
    print("- Read data -")
    scan1, scan2 = readData(dataPath)
    print("- Align -")
    scan2 = alignData(scan1, scan2)
    print("- Segmentation -")
    segmentation1, segmentation2 = segmentData(scan1, scan2)
    print("- Analyzation -")
    analyseData(segmentation1, segmentation2)
    print("- Visualization -")
    visualizeData(segmentation1, segmentation2, scan1)
    print("End")
