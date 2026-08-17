# HyperTile

Le nœud HyperTile applique une technique de tuilage au mécanisme d'attention des modèles de diffusion afin d'optimiser l'utilisation de la mémoire lors de la génération d'images. Il divise l'espace latent en tuiles plus petites, les traite séparément, puis reassemble les résultats. Cela permet de travailler avec des tailles d'image plus grandes sans manquer de mémoire.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel appliquer l'optimisation HyperTile | MODEL | Oui | - |
| `tile_size` | La taille de tuile cible pour le traitement (par défaut : 256). La taille de tuile effective est arrondie à l'inférieur pour être un multiple de 8, avec un minimum de 32. | INT | Non | 1 - 2048 |
| `swap_size` | Le nombre de divisions de tuiles candidates envisagées lorsque le nœud choisit aléatoirement comment diviser l'image. Une valeur plus élevée permet plus de variation dans le découpage (par défaut : 2) | INT | Non | 1 - 128 |
| `max_depth` | Le niveau de profondeur maximal (échelle de résolution) auquel appliquer le tuilage. Une valeur de 0 applique le tuilage uniquement à la résolution la plus élevée (par défaut : 0) | INT | Non | 0 - 10 |
| `scale_depth` | Lorsque activé, la taille de tuile est mise à l'échelle proportionnellement aux niveaux de profondeur plus profonds. Cela peut aider à maintenir la qualité aux résolutions inférieures (par défaut : False) | BOOLEAN | Non | True / False |

Remarque : `scale_depth` n'a d'effet que lorsque `max_depth` est supérieur à 0, car au niveau de résolution le plus élevé (profondeur 0), la taille de tuile n'est jamais mise à l'échelle.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l'optimisation HyperTile appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/fr.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
