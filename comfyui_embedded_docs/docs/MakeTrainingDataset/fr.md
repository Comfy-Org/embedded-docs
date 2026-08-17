# Créer un jeu de données d’entraînement

Ce nœud prépare les données pour l'entraînement en encodant les images et le texte. Il prend une liste d'images et une liste correspondante de légendes textuelles, puis utilise un modèle VAE pour convertir les images en représentations latentes et un modèle CLIP pour convertir le texte en données de conditionnement. Les latents et conditionnements appariés résultants sont fournis sous forme de listes, prêts à être utilisés dans les flux de travail d'entraînement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Liste des images à encoder. | IMAGE | Oui | N/A |
| `vae` | Modèle VAE pour encoder les images en latents. | VAE | Oui | N/A |
| `clip` | Modèle CLIP pour encoder le texte en conditionnement. | CLIP | Oui | N/A |
| `texts` | Liste de légendes textuelles. Peut être de longueur n (correspondant aux images), 1 (répétée pour toutes), ou omise (utilise une chaîne vide). | STRING | Non | N/A |

**Contraintes de paramètres :**

* Le nombre d'éléments dans la liste `texts` doit être 0, 1, ou correspondre exactement au nombre d'éléments dans la liste `images`. Si elle est 0, une chaîne vide est utilisée pour toutes les images. Si elle est 1, ce texte unique est répété pour toutes les images. Si le nombre est autre, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latents` | Liste de dictionnaires latents. | LATENT |
| `conditioning` | Liste de listes de conditionnement. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/fr.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`
