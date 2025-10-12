> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/fr.md)

Le nœud EmptyCosmosLatentVideo crée un tenseur vidéo latent vide avec des dimensions spécifiées. Il génère une représentation latente remplie de zéros qui peut être utilisée comme point de départ pour les flux de travail de génération vidéo, avec des paramètres configurables pour la largeur, la hauteur, la longueur et la taille de lot.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | La largeur de la vidéo latente en pixels (par défaut : 1280, doit être divisible par 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | La hauteur de la vidéo latente en pixels (par défaut : 704, doit être divisible par 16) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Le nombre d'images dans la vidéo latente (par défaut : 121) |
| `taille_du_lot` | INT | Non | 1 à 4096 | Le nombre de vidéos latentes à générer dans un lot (par défaut : 1) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | Le tenseur vidéo latent vide généré avec des valeurs zéro |
