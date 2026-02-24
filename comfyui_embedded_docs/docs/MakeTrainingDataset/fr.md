> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/fr.md)

Ce nœud prépare des données pour l'entraînement en encodant des images et du texte. Il prend une liste d'images et une liste correspondante de légendes textuelles, puis utilise un modèle VAE pour convertir les images en représentations latentes et un modèle CLIP pour convertir le texte en données de conditionnement. Les paires de latents et de conditionnements résultants sont fournis en sortie sous forme de listes, prêts à être utilisés dans des flux de travail d'entraînement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | N/A | Liste des images à encoder. |
| `vae` | VAE | Oui | N/A | Modèle VAE pour encoder les images en latents. |
| `clip` | CLIP | Oui | N/A | Modèle CLIP pour encoder le texte en conditionnement. |
| `texts` | STRING | Non | N/A | Liste des légendes textuelles. Peut avoir une longueur n (correspondant aux images), 1 (répétée pour toutes) ou être omise (utilise une chaîne vide). |

**Contraintes des paramètres :**

* Le nombre d'éléments dans la liste `texts` doit être 0, 1, ou correspondre exactement au nombre d'éléments dans la liste `images`. S'il est 0, une chaîne vide est utilisée pour toutes les images. S'il est 1, ce texte unique est répété pour toutes les images.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `latents` | LATENT | Liste de dictionnaires de latents. |
| `conditioning` | CONDITIONING | Liste de listes de conditionnement. |
