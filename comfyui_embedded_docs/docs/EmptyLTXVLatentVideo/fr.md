> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/fr.md)

Le nœud EmptyLTXVLatentVideo crée un tenseur latent vide pour le traitement vidéo. Il génère un point de départ vierge avec des dimensions spécifiées qui peut être utilisé comme entrée pour les flux de travail de génération vidéo. Le nœud produit une représentation latente remplie de zéros avec la largeur, la hauteur, la longueur et la taille de lot configurées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `largeur` | INT | Oui | 64 à MAX_RESOLUTION | La largeur du tenseur vidéo latent (par défaut : 768, pas : 32) |
| `hauteur` | INT | Oui | 64 à MAX_RESOLUTION | La hauteur du tenseur vidéo latent (par défaut : 512, pas : 32) |
| `longueur` | INT | Oui | 1 à MAX_RESOLUTION | Le nombre d'images dans la vidéo latente (par défaut : 97, pas : 8) |
| `taille_du_lot` | INT | Non | 1 à 4096 | Le nombre de vidéos latentes à générer dans un lot (par défaut : 1) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | Le tenseur latent vide généré avec des valeurs nulles dans les dimensions spécifiées |