# Projet VTK/ITK
# Mini projet - Etude longitudinale de l’évolution d’une tumeur
## Auteurs
- Kael Facon (kael.facon@epita.fr)
- Samuel Gonçalves (samuel.goncalves@epita.fr)
- Oscar Morand (oscar.morand@epita.fr)

## Bibliothèques utilisées
- `itk (5.4.0)`
- `vtk (9.3.0)`

## Lecture des données
La lecture des données est réalisée de façon classique via `itk.imread`. Les valeurs des voxels sont ensuite converties en `itk.F` pour permettre l'utilisation d'algorithmes pré-définis.

## Recalage d'images
TODO

## Segmentation des tumeurs
La segmentation des tumeurs est réalisée via une méthode semi-automatique. Pour chaque tumeur :
- Un point est considéré comme faisant partie de la tumeur, et est donné à l'algorithme via ses coordonnées.
  ![Points choisis de la tumeur](Images/Points.png)
- Ces coordonnées sont utilisées pour détecter les hyperintensitées formant une composante connexes comportant ce point (autrement dit, la tumeur) via `itk.ConnectedThresholdImageFilter`.
- Un filtre de diffusion anisotrope est appliqué sur le scan d'entrée via `itk.GradientAnisotropicDiffusionImageFilter` afin d'éviter que les composantes connexes ne s'agrègent au crâne, dont l'intensité est également importante.

## Analyse des changements
TODO

## Visualisation des changements
TODO
