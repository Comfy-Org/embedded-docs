# Opération d'Affûtage Latent

Le nœud LatentOperationSharpen crée une opération d’accentuation pour les représentations latentes à l’aide d’un noyau gaussien. Il normalise les données latentes, applique un noyau d’accentuation personnalisé par convolution, puis rétablit la luminance d’origine. Cela améliore les détails et les contours dans l’espace latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `rayon_d'affûtage` | Le rayon du noyau d’accentuation, qui contrôle la taille de la zone utilisée pour l’accentuation (par défaut : 9) | INT | Oui | 1-31 |
| `sigma` | L’écart type du noyau gaussien utilisé pour construire le noyau d’accentuation (par défaut : 1.0) | FLOAT | Oui | 0.1-10.0 |
| `alpha` | Le facteur d’intensité de l’accentuation ; des valeurs plus élevées produisent un effet d’accentuation plus fort (par défaut : 0.1) | FLOAT | Oui | 0.0-5.0 |

Ces trois entrées sont des paramètres avancés et ont des valeurs par défaut, le nœud peut donc être utilisé sans les modifier. Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `operation` | Renvoie une opération d’accentuation qui peut être appliquée aux données latentes | LATENT_OPERATION |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/fr.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
