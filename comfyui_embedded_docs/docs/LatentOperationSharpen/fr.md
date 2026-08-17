# Opération d'Affûtage Latent

Le nœud `LatentOperationSharpen` applique un effet d'accentuation aux représentations latentes à l'aide d'un noyau gaussien. Il fonctionne en normalisant les données latentes, en appliquant une convolution avec un noyau d'accentuation personnalisé, puis en restaurant la luminance d'origine. Cela améliore les détails et les contours dans la représentation de l'espace latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `sharpen_radius` | Le rayon du noyau d'accentuation. La taille totale du noyau est calculée comme le double de cette valeur plus un (défaut : 9). | INT | Oui | 1-31 |
| `sigma` | L'écart type du noyau gaussien (défaut : 1.0). | FLOAT | Oui | 0.1-10.0 |
| `alpha` | Le facteur d'intensité de l'accentuation qui contrôle la force de l'effet (défaut : 0.1). | FLOAT | Oui | 0.0-5.0 |

Toutes les entrées sont des paramètres avancés. Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `operation` | Une opération d'accentuation qui peut être appliquée à des données latentes. Son application à un latent renvoie une version accentuée avec la luminance d'origine préservée. | LATENT_OPERATION |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/fr.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
