# PatchModelAddDownscale (Kohya Deep Shrink)

PatchModelAddDownscale (Kohya Deep Shrink) applique la technique Kohya Deep Shrink à un modèle en réduisant les caractéristiques intermédiaires à un bloc choisi, puis en les redimensionnant à leur taille d'origine. La réduction ne se produit que pendant une partie sélectionnée du processus de débruitage, ce qui peut réduire le coût de traitement tout en gardant le résultat final proche de l'original.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer le patch de réduction d'échelle | MODEL | Oui | - |
| `block_number` | Le numéro de bloc spécifique où la réduction d'échelle sera appliquée (par défaut : 3) | INT | Oui | 1-32 |
| `downscale_factor` | Le facteur par lequel réduire l'échelle des caractéristiques (par défaut : 2.0) | FLOAT | Oui | 0.1-9.0 |
| `start_percent` | Le point de départ dans le processus de débruitage où commence la réduction d'échelle (par défaut : 0.0) | FLOAT | Oui | 0.0-1.0 |
| `end_percent` | Le point de fin dans le processus de débruitage où la réduction d'échelle s'arrête (par défaut : 0.35) | FLOAT | Oui | 0.0-1.0 |
| `downscale_after_skip` | Indique s'il faut appliquer la réduction d'échelle après les connexions de saut (par défaut : True) | BOOLEAN | Oui | - |
| `downscale_method` | La méthode d'interpolation utilisée pour les opérations de réduction d'échelle (par défaut : "bicubic") | COMBO | Oui | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `upscale_method` | La méthode d'interpolation utilisée pour les opérations d'agrandissement d'échelle (par défaut : "bicubic") | COMBO | Oui | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

Le patch de réduction d'échelle est appliqué uniquement lorsque l'étape de débruitage actuelle se situe dans la plage définie par `start_percent` et `end_percent`, et uniquement au bloc sélectionné par `block_number`. Lorsque `downscale_after_skip` est activé, le patch est appliqué après la connexion de saut ; lorsqu'il est désactivé, il est appliqué avant la connexion de saut. Les caractéristiques sont ensuite redimensionnées à leur taille d'origine, mais uniquement lorsque la taille actuelle des caractéristiques ne correspond plus à la taille enregistrée avant la réduction d'échelle.

Les paramètres `block_number`, `start_percent`, `end_percent` et `downscale_after_skip` sont marqués comme options avancées dans l'interface du nœud.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le patch de réduction d'échelle appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/fr.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
