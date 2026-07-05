# PatchModelAddDownscale (Kohya Deep Shrink)

Le nœud PatchModelAddDownscale implémente la fonctionnalité Kohya Deep Shrink en appliquant des opérations de réduction et d'agrandissement à des blocs spécifiques d'un modèle. Il réduit la résolution des caractéristiques intermédiaires pendant le traitement, puis les restaure à leur taille d'origine, ce qui peut améliorer les performances tout en maintenant la qualité. Le nœud permet un contrôle précis du moment et de la manière dont ces opérations de mise à l'échelle se produisent pendant l'exécution du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer le patch de réduction | MODEL | Oui | - |
| `numéro de bloc` | Le numéro de bloc spécifique où la réduction sera appliquée (par défaut : 3) | INT | Non | 1-32 |
| `facteur de réduction` | Le facteur de réduction des caractéristiques (par défaut : 2,0) | FLOAT | Non | 0,1-9,0 |
| `pourcentage de départ` | Le point de départ dans le processus de débruitage où la réduction commence (par défaut : 0,0) | FLOAT | Non | 0,0-1,0 |
| `pourcentage de fin` | Le point de fin dans le processus de débruitage où la réduction s'arrête (par défaut : 0,35) | FLOAT | Non | 0,0-1,0 |
| `réduction après saut` | Si la réduction doit être appliquée après les connexions de saut (par défaut : True) | BOOLEAN | Non | - |
| `méthode de réduction` | La méthode d'interpolation utilisée pour les opérations de réduction | COMBO | Non | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `méthode d'agrandissement` | La méthode d'interpolation utilisée pour les opérations d'agrandissement | COMBO | Non | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec le patch de réduction appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/fr.md)

---
**Source fingerprint (SHA-256):** `93ece77ad2dce3c1cdd554583ae1f2e6be51a43ab072d408869dddbcc7798c40`
