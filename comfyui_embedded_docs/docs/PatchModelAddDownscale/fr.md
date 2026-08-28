# PatchModelAddDownscale (Kohya Deep Shrink)

PatchModelAddDownscale (Kohya Deep Shrink) implémente la technique Kohya Deep Shrink en appliquant des opérations de réduction et d'augmentation de résolution à des blocs spécifiques d'un modèle. Elle réduit la résolution des caractéristiques intermédiaires pendant le traitement, puis les restaure à leur taille d'origine, ce qui peut améliorer les performances tout en maintenant la qualité. Le nœud permet un contrôle précis du moment et de la manière dont ces opérations de mise à l'échelle se produisent pendant l'exécution du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer le patch de réduction d'échelle | MODEL | Oui | - |
| `numéro de bloc` | Le numéro de bloc spécifique où la réduction d'échelle sera appliquée (par défaut : 3) | INT | Oui | 1-32 |
| `facteur de réduction` | Le facteur de réduction d'échelle des caractéristiques (par défaut : 2.0) | FLOAT | Oui | 0.1-9.0 |
| `pourcentage de départ` | Le point de départ du processus de débruitage où la réduction d'échelle commence (par défaut : 0.0) | FLOAT | Oui | 0.0-1.0 |
| `pourcentage de fin` | Le point de fin du processus de débruitage où la réduction d'échelle s'arrête (par défaut : 0.35) | FLOAT | Oui | 0.0-1.0 |
| `réduction après saut` | Indique si la réduction d'échelle est appliquée après les connexions de saut (par défaut : True) | BOOLEAN | Oui | - |
| `méthode de réduction` | La méthode d'interpolation utilisée pour les opérations de réduction d'échelle | COMBO | Oui | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `méthode d'agrandissement` | La méthode d'interpolation utilisée pour les opérations d'augmentation d'échelle | COMBO | Oui | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

Le patch de réduction d'échelle n'est appliqué que lorsque l'étape de débruitage actuelle se situe dans la plage définie par `start_percent` et `end_percent`, et uniquement au bloc sélectionné par `block_number`. Lorsque `downscale_after_skip` est activé, le patch est appliqué après la connexion de saut ; lorsqu'il est désactivé, il est appliqué avant la connexion de saut.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le patch de réduction d'échelle appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/fr.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
