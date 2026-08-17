# PatchModelAddDownscale (Kohya Deep Shrink)

Le nœud `PatchModelAddDownscale` implémente la fonctionnalité Kohya Deep Shrink en appliquant des opérations de réduction et d’agrandissement à des blocs spécifiques d’un modèle. Il réduit la résolution des caractéristiques intermédiaires pendant le traitement, puis les restaure à leur taille d’origine, ce qui peut améliorer les performances tout en maintenant la qualité. Le nœud permet un contrôle précis du moment et de la manière dont ces opérations de mise à l’échelle se produisent pendant l’exécution du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer le patch de réduction | MODEL | Oui | - |
| `block_number` | Le numéro de bloc spécifique où la réduction sera appliquée (par défaut : 3) | INT | Non | 1-32 |
| `downscale_factor` | Le facteur par lequel réduire les caractéristiques (par défaut : 2.0) | FLOAT | Non | 0.1-9.0 |
| `start_percent` | Le point de départ dans le processus de débruitage où la réduction commence (par défaut : 0.0) | FLOAT | Non | 0.0-1.0 |
| `end_percent` | Le point de fin dans le processus de débruitage où la réduction s’arrête (par défaut : 0.35) | FLOAT | Non | 0.0-1.0 |
| `downscale_after_skip` | Indique si la réduction est appliquée après les connexions de saut (par défaut : True) | BOOLEAN | Non | - |
| `downscale_method` | La méthode d’interpolation utilisée pour les opérations de réduction | COMBO | Non | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `upscale_method` | La méthode d’interpolation utilisée pour les opérations d’agrandissement | COMBO | Non | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le patch de réduction appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/fr.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
