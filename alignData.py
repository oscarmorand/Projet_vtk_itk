import itk

def alignData(scan1, scan2, save=None, log=False):
    dimension = scan1.GetImageDimension()
    FixedImageType = type(scan1)
    MovingImageType = type(scan2)

    # Initialiser la transformation
    TransformType = itk.TranslationTransform[itk.D, dimension]
    initial_transform = TransformType.New()


    # Initialiser la métrique
    metric = itk.MeanSquaresImageToImageMetricv4[FixedImageType, MovingImageType].New()
    fixed_interpolation = itk.LinearInterpolateImageFunction[FixedImageType, itk.D].New()
    metric.SetFixedInterpolator(fixed_interpolation)
    metric.SetFixedImage(scan1)
    metric.SetMovingImage(scan2)


    # Initialiser l'optimiseur
    optimizer = itk.RegularStepGradientDescentOptimizerv4.New()

    optimizer.SetLearningRate(1)
    optimizer.SetMinimumStepLength(0.001)
    optimizer.SetNumberOfIterations(400)


    # Configurer le recalage
    RegistrationType = itk.ImageRegistrationMethodv4[FixedImageType, MovingImageType]
    registration = RegistrationType.New()

    registration.SetFixedImage(scan1)
    registration.SetMovingImage(scan2)
    registration.SetMetric(metric)
    registration.SetOptimizer(optimizer)
    registration.SetInitialTransform(initial_transform)


    # Calculer la valeur de la métrique avant le recalage
    metric.Initialize()
    if log:
        initial_metric_value = metric.GetValue()
        print(f"Metric value before transformation: {initial_metric_value}")

    # Effectuer le recalage
    registration.Update()

    # Appliquer la transformation
    resampler = itk.ResampleImageFilter.New(
        Input=scan2,
        Transform=registration.GetTransform(),
        UseReferenceImage=True,
        ReferenceImage=scan1
    )
    resampler.update()
    aligned_image = resampler.GetOutput()

    if log:
        # Calculer la valeur de la métrique après le recalage
        final_metric_value = metric.GetValue()
        print(f"Metric value after transformation: {final_metric_value}")

    # Sauvegarder l'image recalée
    if save is not None:
        itk.imwrite(aligned_image, save)

    return aligned_image
