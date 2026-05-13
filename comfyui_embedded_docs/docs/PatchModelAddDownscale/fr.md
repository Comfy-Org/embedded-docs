> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/fr.md)

Le nœud PatchModelAddDownscale implémente la fonctionnalité Kohya Deep Shrink en appliquant des opérations de réduction et d'agrandissement à des blocs spécifiques d'un modèle. Il réduit la résolution des caractéristiques intermédiaires pendant le traitement, puis les restaure à leur taille d'origine, ce qui peut améliorer les performances tout en maintenant la qualité. Le nœud permet un contrôle précis du moment et de la manière dont ces opérations de mise à l'échelle se produisent pendant l'exécution du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle auquel appliquer le patch de réduction |
| `numéro de bloc` | INT | Non | 1-32 | Le numéro de bloc spécifique où la réduction sera appliquée (par défaut : 3) |
| `facteur de réduction` | FLOAT | Non | 0,1-9,0 | Le facteur de réduction des caractéristiques (par défaut : 2,0) |
| `pourcentage de départ` | FLOAT | Non | 0,0-1,0 | Le point de départ dans le processus de débruitage où la réduction commence (par défaut : 0,0) |
| `pourcentage de fin` | FLOAT | Non | 0,0-1,0 | Le point de fin dans le processus de débruitage où la réduction s'arrête (par défaut : 0,35) |
| `réduction après saut` | BOOLEAN | Non | - | Si la réduction doit être appliquée après les connexions de saut (par défaut : True) |
| `méthode de réduction` | COMBO | Non | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | La méthode d'interpolation utilisée pour les opérations de réduction |
| `méthode d'agrandissement` | COMBO | Non | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | La méthode d'interpolation utilisée pour les opérations d'agrandissement |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `modèle` | MODEL | Le modèle modifié avec le patch de réduction appliqué |

---
**Source fingerprint (SHA-256):** `93ece77ad2dce3c1cdd554583ae1f2e6be51a43ab072d408869dddbcc7798c40`
