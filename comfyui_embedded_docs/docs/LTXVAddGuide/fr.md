> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/fr.md)

Le nœud LTXVAddGuide ajoute un guidage de conditionnement vidéo aux séquences latentes en encodant les images ou vidéos d'entrée et en les incorporant comme images clés dans les données de conditionnement. Il traite l'entrée via un encodeur VAE et place stratégiquement les latents résultants aux positions de frame spécifiées tout en mettant à jour le conditionnement positif et négatif avec les informations des images clés. Le nœud gère les contraintes d'alignement des frames et permet de contrôler l'intensité de l'influence du conditionnement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Entrée de conditionnement positive à modifier avec le guidage par images clés |
| `negative` | CONDITIONING | Oui | - | Entrée de conditionnement négative à modifier avec le guidage par images clés |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder les images/frames vidéo d'entrée |
| `latent` | LATENT | Oui | - | Séquence latente d'entrée qui recevra les frames de conditionnement |
| `image` | IMAGE | Oui | - | Image ou vidéo sur laquelle conditionner la vidéo latente. Doit avoir 8*n + 1 frames. Si la vidéo n'a pas 8*n + 1 frames, elle sera rognée au nombre de frames 8*n + 1 le plus proche. |
| `frame_idx` | INT | Non | -9999 à 9999 | Index de frame pour démarrer le conditionnement. Pour les images à frame unique ou les vidéos avec 1-8 frames, toute valeur de frame_idx est acceptable. Pour les vidéos avec 9+ frames, frame_idx doit être divisible par 8, sinon il sera arrondi au multiple de 8 inférieur le plus proche. Les valeurs négatives sont comptées depuis la fin de la vidéo. (par défaut : 0) |
| `strength` | FLOAT | Non | 0.0 à 1.0 | Intensité de l'influence du conditionnement, où 1.0 applique un conditionnement complet et 0.0 n'applique aucun conditionnement (par défaut : 1.0) |

**Note :** L'image/vidéo d'entrée doit avoir un nombre de frames suivant le motif 8*n + 1 (par exemple, 1, 9, 17, 25 frames). Si l'entrée dépasse ce motif, elle sera automatiquement rognée au nombre de frames valide le plus proche.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Conditionnement positif mis à jour avec les informations de guidage par images clés |
| `negative` | CONDITIONING | Conditionnement négatif mis à jour avec les informations de guidage par images clés |
| `latent` | LATENT | Séquence latente avec les frames de conditionnement incorporées et le masque de bruit mis à jour |