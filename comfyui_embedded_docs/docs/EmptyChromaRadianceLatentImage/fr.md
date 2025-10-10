> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/fr.md)

Le nœud EmptyChromaRadianceLatentImage crée une image latente vierge avec des dimensions spécifiées pour une utilisation dans les workflows de chrominance et de rayonnement. Il génère un tenseur rempli de zéros qui sert de point de départ pour les opérations dans l'espace latent. Le nœud permet de définir la largeur, la hauteur et la taille du lot de l'image latente vide.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Oui | 16 à MAX_RESOLUTION | La largeur de l'image latente en pixels (par défaut : 1024, doit être divisible par 16) |
| `height` | INT | Oui | 16 à MAX_RESOLUTION | La hauteur de l'image latente en pixels (par défaut : 1024, doit être divisible par 16) |
| `batch_size` | INT | Non | 1 à 4096 | Le nombre d'images latentes à générer dans un lot (par défaut : 1) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | Le tenseur d'image latente vide généré avec les dimensions spécifiées |