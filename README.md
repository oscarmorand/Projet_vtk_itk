# Projet VTK/ITK
# Mini projet - Etude longitudinale de l’évolution d’une tumeur
## Auteurs
- Kael Facon (kael.facon@epita.fr)
- Samuel Gonçalves (samuel.goncalves@epita.fr)
- Oscar Morand (oscar.morand@epita.fr)

## Bibliothèques utilisées
- `itk (5.4.0)`
- `vtk (9.3.0)`
- `numpy (1.26.4)`

## Lecture des données
La lecture des données est réalisée de façon classique via `itk.imread`. Les valeurs des voxels sont ensuite converties en `itk.F` pour permettre l'utilisation d'algorithmes pré-définis.

## Recalage d'images
TODO

## Segmentation des tumeurs
La segmentation des tumeurs est réalisée via une méthode semi-automatique. Pour chaque tumeur :
- Un point (illustré en vert clair) est considéré comme faisant partie de la tumeur, et est donné à l'algorithme via ses coordonnées.
  ![Points choisis de la tumeur](Images/Points.png)
- Ces coordonnées sont utilisées pour détecter les hyperintensitées formant une composante connexe comportant ce point (autrement dit, la tumeur) via `itk.ConnectedThresholdImageFilter`.
  ![Segmentation 1](Images/Segmentation1.png)
- Un filtre de diffusion anisotrope est appliqué sur le scan d'entrée via `itk.GradientAnisotropicDiffusionImageFilter` afin d'éviter que la composante connexe représentant la tumeur ne s'agrège à d'autres composantes dont l'intensité est également importante.
  ![Segmentation 2](Images/Segmentation2.png)

## Analyse des changements
TODO

## Visualisation des changements
TODO
