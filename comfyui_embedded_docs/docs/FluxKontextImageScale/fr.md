Ce nœud redimensionne l'image d'entrée à une taille optimale utilisée lors de l'entraînement du modèle Flux Kontext en utilisant l'algorithme Lanczos, basé sur le rapport d'aspect de l'image d'entrée. Ce nœud est particulièrement utile lors de l'entrée d'images de grande taille, car les entrées surdimensionnées peuvent entraîner une dégradation de la qualité de sortie du modèle ou des problèmes tels que l'apparition de plusieurs sujets dans la sortie.

## Entrées

| Nom du Paramètre | Type de Données | Type d'Entrée | Valeur par Défaut | Plage de Valeurs | Description |
|-----------------|-----------------|----------------|-------------------|------------------|-------------|
| `image` | IMAGE | Requis | - | - | Image d'entrée à redimensionner |

## Sorties

| Nom de Sortie | Type de Données | Description |
|---------------|-----------------|-------------|
| `image` | IMAGE | Image redimensionnée |

## Liste des Tailles Prédéfinies

Voici une liste des tailles standard utilisées pendant l'entraînement du modèle. Le nœud sélectionnera la taille la plus proche du rapport d'aspect de l'image d'entrée :

| Largeur | Hauteur | Rapport d'Aspect |
|---------|---------|------------------|
| 672     | 1568    | 0.429           |
| 688     | 1504    | 0.457           |
| 720     | 1456    | 0.494           |
| 752     | 1392    | 0.540           |
| 800     | 1328    | 0.603           |
| 832     | 1248    | 0.667           |
| 880     | 1184    | 0.743           |
| 944     | 1104    | 0.855           |
| 1024    | 1024    | 1.000           |
| 1104    | 944     | 1.170           |
| 1184    | 880     | 1.345           |
| 1248    | 832     | 1.500           |
| 1328    | 800     | 1.660           |
| 1392    | 752     | 1.851           |
| 1456    | 720     | 2.022           |
| 1504    | 688     | 2.186           |
| 1568    | 672     | 2.333           |
