import itk
import vtk

# Create merged image
def merge_segmentation(segmentation1, segmentation2, scan1):
    # Create a new image
    merged_image = vtk.vtkImageData()
    merged_image.DeepCopy(scan1)
    
    # Get the image data
    seg_data1 = segmentation1.GetPointData().GetScalars()
    seg_data2 = segmentation2.GetPointData().GetScalars()
    data_merged = merged_image.GetPointData().GetScalars()
    
    # Merge the images
    for i in range(seg_data1.GetNumberOfTuples()):
        value1 = seg_data1.GetTuple1(i)
        value2 = seg_data2.GetTuple1(i)
        if (value1 == 255):
            data_merged.SetTuple1(i, 255)
        elif (value2 == 255):
            data_merged.SetTuple1(i, 200)
        else:
            if (data_merged.GetTuple1(i) <= 20):
                data_merged.SetTuple1(i, 0)
            elif (20 < data_merged.GetTuple1(i) < 60):
                data_merged.SetTuple1(i, 100)
            else:
                data_merged.SetTuple1(i, 150)
    
    return merged_image

# Vtk display
def display_tumor(merged_segmentation):
    # Create a rendering window and renderer
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)

    # Create a renderwindowinteractor
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Create a volume
    volumeMapper = vtk.vtkSmartVolumeMapper()
    volumeMapper.SetInputData(merged_segmentation)
    volume = vtk.vtkVolume()
    volume.SetMapper(volumeMapper)

    # Create transfer mapping scalar value to opacity
    opacityTransferFunction = vtk.vtkPiecewiseFunction()
    opacityTransferFunction.AddPoint(0, 0.0)
    opacityTransferFunction.AddPoint(99, 0.0)
    opacityTransferFunction.AddPoint(100, 0.01)
    opacityTransferFunction.AddPoint(150, 0.01)
    opacityTransferFunction.AddPoint(199, 0.01)
    opacityTransferFunction.AddPoint(200, 0.1)
    opacityTransferFunction.AddPoint(254, 0.1)
    opacityTransferFunction.AddPoint(255, 0.5)

    # Create transfer mapping scalar value to color
    colorTransferFunction = vtk.vtkColorTransferFunction()
    colorTransferFunction.AddRGBPoint(0.0, 0.0, 0.0, 0.0)
    colorTransferFunction.AddRGBPoint(99.0, 0.0, 0.0, 0.0)
    colorTransferFunction.AddRGBPoint(100.0, 1., 0.5, 0.5)
    colorTransferFunction.AddRGBPoint(150.0, 0.95, 0.85, 0.75)
    colorTransferFunction.AddRGBPoint(192.0, 1.0, 0.0, 0.0)
    colorTransferFunction.AddRGBPoint(255.0, 0.0, 0.0, 1.0)

    # The property describes how the data will look
    volumeProperty = vtk.vtkVolumeProperty()
    volumeProperty.SetColor(colorTransferFunction)
    volumeProperty.SetScalarOpacity(opacityTransferFunction)
    volumeProperty.SetInterpolationTypeToLinear()
    # volumeProperty.ShadeOn()

    # The mapper / ray cast function know how to render the data
    volumeMapper.SetBlendModeToComposite()
    volume.SetProperty(volumeProperty)
    ren.AddViewProp(volume)

    # Set background color
    ren.SetBackground(0.7, 0.7, 0.8)

    # Set window size
    renWin.SetSize(600, 600)

    # Initialize the interactor and start the rendering loop
    iren.Initialize()
    renWin.Render()
    iren.Start()

    # Clean up
    iren.GetRenderWindow().Finalize()
    iren.TerminateApp()

def visualizeData(segmentation1, segmentation2, scan1):
    scan1 = itk.vtk_image_from_image(scan1)
    merged_image = merge_segmentation(segmentation1, segmentation2, scan1)
    display_tumor(merged_image)
