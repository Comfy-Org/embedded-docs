> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/fr.md)

Le nœud LatentOperationSharpen applique un effet d'accentuation aux représentations latentes à l'aide d'un noyau gaussien. Il fonctionne en normalisant les données latentes, en appliquant une convolution avec un noyau d'accentuation personnalisé, puis en restaurant la luminance d'origine. Cela améliore les détails et les contours dans la représentation de l'espace latent.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `rayon_d'affûtage` | INT | Non | 1-31 | Le rayon du noyau d'accentuation (par défaut : 9) |
| `sigma` | FLOAT | Non | 0,1-10,0 | L'écart type pour le noyau gaussien (par défaut : 1,0) |
| `alpha` | FLOAT | Non | 0,0-5,0 | Le facteur d'intensité de l'accentuation (par défaut : 0,1) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `operation` | LATENT_OPERATION | Renvoie une opération d'accentuation pouvant être appliquée aux données latentes |

---
**Source fingerprint (SHA-256):** `542754746ab462eb27229ab9b949bb66054ab4c87c77cc59d405b35a2cc27bce`
