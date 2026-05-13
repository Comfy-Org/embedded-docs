> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextImageScale/fr.md)

Ce nœud redimensionne l'image d'entrée à une taille optimale utilisée lors de l'entraînement du modèle Flux Kontext, en utilisant l'algorithme de Lanczos et en se basant sur le rapport hauteur/largeur de l'image d'entrée. Ce nœud est particulièrement utile pour les images de grande taille, car des entrées surdimensionnées peuvent dégrader la qualité de sortie du modèle ou provoquer des problèmes tels que l'apparition de plusieurs sujets dans le résultat.

## Entrées

| Nom du paramètre | Type de données | Type d'entrée | Valeur par défaut | Plage de valeurs | Description |
|------------------|----------------|---------------|-------------------|------------------|-------------|
| `image` | IMAGE | Requis | - | - | Image d'entrée à redimensionner |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | Image redimensionnée |

## Liste des tailles prédéfinies

Voici la liste des tailles standard utilisées lors de l'entraînement du modèle. Le nœud sélectionnera la taille la plus proche du rapport hauteur/largeur de l'image d'entrée :

| Largeur | Hauteur | Rapport hauteur/largeur |
|---------|---------|-------------------------|
| 672     | 1568    | 0,429                   |
| 688     | 1504    | 0,457                   |
| 720     | 1456    | 0,494                   |
| 752     | 1392    | 0,540                   |
| 800     | 1328    | 0,603                   |
| 832     | 1248    | 0,667                   |
| 880     | 1184    | 0,743                   |
| 944     | 1104    | 0,855                   |
| 1024    | 1024    | 1,000                   |
| 1104    | 944     | 1,170                   |
| 1184    | 880     | 1,345                   |
| 1248    | 832     | 1,500                   |
| 1328    | 800     | 1,660                   |
| 1392    | 752     | 1,851                   |
| 1456    | 720     | 2,022                   |
| 1504    | 688     | 2,186                   |
| 1568    | 672     | 2,333                   |