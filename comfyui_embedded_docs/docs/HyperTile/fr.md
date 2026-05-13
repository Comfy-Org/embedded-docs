> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/fr.md)

Le nœud HyperTile applique une technique de tuilage au mécanisme d'attention des modèles de diffusion afin d'optimiser l'utilisation de la mémoire lors de la génération d'images. Il divise l'espace latent en tuiles plus petites, les traite séparément, puis reassemble les résultats. Cela permet de travailler avec des tailles d'image plus grandes sans manquer de mémoire.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer l'optimisation HyperTile |
| `tile_size` | INT | Non | 1 - 2048 | La taille cible des tuiles pour le traitement (par défaut : 256). La taille effective des tuiles est arrondie à l'inférieur à un multiple de 8, avec un minimum de 32. |
| `swap_size` | INT | Non | 1 - 128 | Contrôle la façon dont les tuiles sont réarrangées pendant le traitement pour améliorer l'efficacité (par défaut : 2) |
| `max_depth` | INT | Non | 0 - 10 | Le niveau de profondeur maximal (échelle de résolution) auquel appliquer le tuilage. Une valeur de 0 applique le tuilage uniquement à la résolution la plus élevée (par défaut : 0) |
| `scale_depth` | BOOLEAN | Non | Vrai / Faux | Lorsque cette option est activée, la taille des tuiles est mise à l'échelle proportionnellement aux niveaux de profondeur plus profonds. Cela peut aider à maintenir la qualité aux résolutions inférieures (par défaut : Faux) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec l'optimisation HyperTile appliquée |

---
**Source fingerprint (SHA-256):** `d3c55e6a38abecc8fe612dbb91a3ba26de9bc5cf8a187f01cf4746550f62f40a`
