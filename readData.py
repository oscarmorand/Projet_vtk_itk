import itk

scans_paths = ["case6_gre1.nrrd", "case6_gre2.nrrd"]

def readData(path):
    scans = []
    for scan_path in scans_paths:
        complete_path = path + scan_path
        scan = itk.imread(complete_path)

        # Conversion
        caster = itk.CastImageFilter[scan, itk.Image[itk.F, 3]].New()
        caster.SetInput(scan)
        caster.Update()

        scan = caster.GetOutput()

        img = itk.GetArrayFromImage(scan)
        min_val = img.min()
        max_val = img.max()
    
        img = 255 * (img - min_val) / (max_val - min_val)
    
        scans.append(itk.GetImageFromArray(img))

    return scans
