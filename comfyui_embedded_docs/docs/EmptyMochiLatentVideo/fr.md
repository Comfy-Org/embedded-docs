> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/fr.md)

Le nœud EmptyMochiLatentVideo crée un tenseur vidéo latent vide avec des dimensions spécifiées. Il génère une représentation latente remplie de zéros qui peut être utilisée comme point de départ pour les workflows de génération vidéo. Le nœud vous permet de définir la largeur, la hauteur, la longueur et la taille de lot pour le tenseur vidéo latent.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | La largeur de la vidéo latente en pixels (par défaut : 848, doit être divisible par 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | La hauteur de la vidéo latente en pixels (par défaut : 480, doit être divisible par 16) |
| `longueur` | INT | Oui | 7 à MAX_RESOLUTION | Le nombre d'images dans la vidéo latente (par défaut : 25) |
| `taille_du_lot` | INT | Non | 1 à 4096 | Le nombre de vidéos latentes à générer dans un lot (par défaut : 1) |

**Note :** Les dimensions latentes réelles sont calculées comme largeur/8 et hauteur/8, et la dimension temporelle est calculée comme ((longueur - 1) // 6) + 1.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | Un tenseur vidéo latent vide avec les dimensions spécifiées, contenant uniquement des zéros |
