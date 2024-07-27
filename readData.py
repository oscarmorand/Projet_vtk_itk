import itk

scans_paths = ["case6_gre1.nrrd", "case6_gre2.nrrd"]

def readData(path):
    scans = []
    for scan_path in scans_paths:
        complete_path = path + scan_path
        scan = itk.imread(complete_path, itk.F)
        scans.append(scan)

    return scans
