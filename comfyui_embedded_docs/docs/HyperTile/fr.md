# HyperTile

HyperTile applique une technique de découpage en tuiles au mécanisme d'attention à l'intérieur des modèles de diffusion afin de réduire l'utilisation de la mémoire pendant la génération d'images. Il divise l'espace latent en tuiles plus petites, traite l'attention pour chaque tuile séparément, puis réassemble les résultats. Cela permet de travailler avec des tailles d'image plus grandes sans épuiser la mémoire.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel appliquer l'optimisation HyperTile | MODEL | Oui | - |
| `tile_size` | Taille de tuile cible pour le traitement (par défaut : 256). En interne, la valeur est limitée à un minimum de 32, puis divisée par 8 pour obtenir la taille de tuile effective. | INT | Oui | 1 - 2048 |
| `swap_size` | Contrôle la façon dont les tuiles sont réorganisées pendant le traitement afin d'améliorer l'efficacité. Des valeurs plus élevées permettent davantage de variation dans les tailles de tuiles (par défaut : 2) | INT | Oui | 1 - 128 |
| `max_depth` | Niveau de profondeur maximal (échelle de résolution) auquel appliquer le découpage en tuiles. Une valeur de 0 applique le découpage en tuiles uniquement à la résolution la plus élevée (par défaut : 0) | INT | Oui | 0 - 10 |
| `scale_depth` | Lorsque cette option est activée, la taille des tuiles est mise à l'échelle proportionnellement aux niveaux de profondeur plus élevés. Cela peut aider à maintenir la qualité aux résolutions inférieures (par défaut : False) | BOOLEAN | Oui | True / False |

Remarque : `tile_size`, `swap_size`, `max_depth` et `scale_depth` sont marqués comme entrées avancées, elles ne sont donc affichées que lorsque les options avancées sont activées dans l'interface.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l'optimisation HyperTile appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/fr.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
