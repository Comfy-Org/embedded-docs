
Le nœud LoadImage est conçu pour charger et prétraiter des images à partir d'un chemin spécifié. Il gère les formats d'image avec plusieurs cadres, applique les transformations nécessaires telles que la rotation basée sur les données EXIF, normalise les valeurs des pixels et génère éventuellement un masque pour les images avec un canal alpha. Ce nœud est essentiel pour préparer les images à un traitement ou une analyse ultérieure dans un pipeline.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|--------------|-------------|
| `image`   | COMBO[STRING] | Le paramètre 'image' spécifie l'identifiant de l'image à charger et traiter. Il est crucial pour déterminer le chemin vers le fichier image et charger ensuite l'image pour la transformation et la normalisation. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | L'image traitée, avec des valeurs de pixels normalisées et des transformations appliquées si nécessaire. Elle est prête pour un traitement ou une analyse ultérieure. |
| `mask`    | `MASK`      | Une sortie optionnelle fournissant un masque pour l'image, utile dans les scénarios où l'image inclut un canal alpha pour la transparence. |
