import itk
import numpy as np

tumor_points = [(82, 69, 49), (124, 63, 79), (98, 77, 82)]

def segmentScan(scan, seed):
    smoother = itk.GradientAnisotropicDiffusionImageFilter.New(Input=scan, NumberOfIterations=20, TimeStep=0.04, ConductanceParameter=3)
    smoother.Update()
    
    connected_threshold = itk.ConnectedThresholdImageFilter.New(smoother.GetOutput())

    connected_threshold.SetReplaceValue(255)
    connected_threshold.SetLower(70)
    connected_threshold.SetUpper(255)
    connected_threshold.SetSeed(seed)
    connected_threshold.Update()
    segmented_image = connected_threshold.GetOutput()

    return segmented_image

def segmentData(scan1, scan2):
    scans = [scan1, scan2]
    segmentations = []
    for scan in scans:
        segmentation = np.zeros(scan.shape)
        for tumor_point in tumor_points:
            segmentation = np.maximum(segmentation, segmentScan(scan, tumor_point))
        segmentations.append(segmentation)

    return segmentations
