Le nœud HyperTile applique une technique de tuilage au mécanisme d'attention des modèles de diffusion afin d'optimiser l'utilisation de la mémoire lors de la génération d'images. Il divise l'espace latent en tuiles plus petites, les traite séparément, puis reassemble les résultats. Cela permet de travailler avec des tailles d'image plus grandes sans manquer de mémoire.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer l'optimisation HyperTile | MODEL | Oui | - |
| `taille_tuile` | La taille cible des tuiles pour le traitement (par défaut : 256). La taille effective des tuiles est arrondie à l'inférieur à un multiple de 8, avec un minimum de 32. | INT | Non | 1 - 2048 |
| `taille_échange` | Contrôle la façon dont les tuiles sont réarrangées pendant le traitement pour améliorer l'efficacité (par défaut : 2) | INT | Non | 1 - 128 |
| `profondeur_max` | Le niveau de profondeur maximal (échelle de résolution) auquel appliquer le tuilage. Une valeur de 0 applique le tuilage uniquement à la résolution la plus élevée (par défaut : 0) | INT | Non | 0 - 10 |
| `échelle_profondeur` | Lorsque cette option est activée, la taille des tuiles est mise à l'échelle proportionnellement aux niveaux de profondeur plus profonds. Cela peut aider à maintenir la qualité aux résolutions inférieures (par défaut : Faux) | BOOLEAN | Non | Vrai / Faux |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec l'optimisation HyperTile appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/fr.md)

---
**Source fingerprint (SHA-256):** `d3c55e6a38abecc8fe612dbb91a3ba26de9bc5cf8a187f01cf4746550f62f40a`
