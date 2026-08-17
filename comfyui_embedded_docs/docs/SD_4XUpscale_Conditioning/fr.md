# SD_4XUpscale_Conditioning

Le nœud SD_4XUpscale_Conditioning prépare les données de conditionnement pour l'agrandissement d'images à l'aide de modèles de diffusion. Il prend en entrée des images et des données de conditionnement, puis applique une mise à l'échelle et une augmentation de bruit pour créer un conditionnement modifié qui guide le processus d'agrandissement. Le nœud produit à la fois un conditionnement positif et négatif ainsi que des représentations latentes pour les dimensions agrandies.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Images d'entrée à agrandir | IMAGE | Oui | - |
| `positive` | Données de conditionnement positives qui guident la génération vers le contenu souhaité | CONDITIONING | Oui | - |
| `negative` | Données de conditionnement négatives qui éloignent la génération du contenu indésirable | CONDITIONING | Oui | - |
| `scale_ratio` | Facteur d'échelle appliqué aux images d'entrée (par défaut : 4.0) | FLOAT | Oui | 0.0 - 10.0 |
| `noise_augmentation` | Quantité de bruit à ajouter pendant le processus d'agrandissement (par défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 |

Les dimensions d'agrandissement cibles sont calculées en multipliant les dimensions de l'image d'entrée par `scale_ratio`. L'image intégrée dans le conditionnement et le latent de sortie sont tous deux créés à un quart de ces dimensions cibles.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec informations d'agrandissement appliquées | CONDITIONING |
| `negative` | Conditionnement négatif modifié avec informations d'agrandissement appliquées | CONDITIONING |
| `latent` | Représentation latente vide correspondant aux dimensions agrandies | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
