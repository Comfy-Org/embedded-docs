Voici la traduction en français de la documentation du nœud SD_4XUpscale_Conditioning :

Le nœud SD_4XUpscale_Conditioning prépare les données de conditionnement pour la mise à l'échelle d'images à l'aide de modèles de diffusion. Il prend des images d'entrée et des données de conditionnement, puis applique une mise à l'échelle et une augmentation de bruit pour créer un conditionnement modifié qui guide le processus de mise à l'échelle. Le nœud produit à la fois un conditionnement positif et négatif, ainsi que des représentations latentes pour les dimensions mises à l'échelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Images d'entrée à mettre à l'échelle | IMAGE | Oui | - |
| `positive` | Données de conditionnement positif qui guident la génération vers le contenu souhaité | CONDITIONING | Oui | - |
| `négatif` | Données de conditionnement négatif qui éloignent la génération du contenu indésirable | CONDITIONING | Oui | - |
| `ratio_d'échelle` | Facteur de mise à l'échelle appliqué aux images d'entrée (par défaut : 4.0) | FLOAT | Non | 0.0 - 10.0 |
| `augmentation_du_bruit` | Quantité de bruit à ajouter pendant le processus de mise à l'échelle (par défaut : 0.0) | FLOAT | Non | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec les informations de mise à l'échelle appliquées | CONDITIONING |
| `négatif` | Conditionnement négatif modifié avec les informations de mise à l'échelle appliquées | CONDITIONING |
| `latent` | Représentation latente vide correspondant aux dimensions mises à l'échelle | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `ede1ea8f5a95e7f9e52070b5132a4ed3e87f92230d14a74b9d713f547c74d785`
