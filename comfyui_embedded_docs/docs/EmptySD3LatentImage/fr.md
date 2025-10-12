> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/fr.md)

Le nœud EmptySD3LatentImage crée un tenseur d'image latente vide spécifiquement formaté pour les modèles Stable Diffusion 3. Il génère un tenseur rempli de zéros qui possède les dimensions et la structure correctes attendues par les pipelines SD3. Ceci est couramment utilisé comme point de départ pour les flux de travail de génération d'images.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) | La largeur de l'image latente de sortie en pixels (par défaut : 1024) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION (pas : 16) | La hauteur de l'image latente de sortie en pixels (par défaut : 1024) |
| `taille_du_lot` | INT | Oui | 1 à 4096 | Le nombre d'images latentes à générer dans un lot (par défaut : 1) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Un tenseur latent contenant des échantillons vides avec des dimensions compatibles SD3 |
