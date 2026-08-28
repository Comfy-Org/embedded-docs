# HyperTile

Le nœud HyperTile applique une technique de tuilage au mécanisme d'attention des modèles de diffusion afin d'optimiser l'utilisation de la mémoire lors de la génération d'images. Il divise l'espace latent en tuiles plus petites, les traite séparément, puis reassemble les résultats. Cela permet de travailler avec des tailles d'image plus grandes sans épuiser la mémoire.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer l'optimisation HyperTile | MODEL | Oui | - |
| `taille_tuile` | La taille de tuile cible pour le traitement (par défaut : 256). En interne, la valeur est bornée à un minimum de 32 puis divisée par 8 pour obtenir la taille de tuile effective. | INT | Oui | 1 - 2048 |
| `taille_échange` | Contrôle la façon dont les tuiles sont réarrangées pendant le traitement pour améliorer l'efficacité. Des valeurs plus élevées permettent une plus grande variation des tailles de tuiles (par défaut : 2) | INT | Oui | 1 - 128 |
| `profondeur_max` | Le niveau de profondeur maximal (échelle de résolution) auquel appliquer le tuilage. Une valeur de 0 applique le tuilage uniquement à la plus haute résolution (par défaut : 0) | INT | Oui | 0 - 10 |
| `échelle_profondeur` | Lorsque activé, la taille des tuiles est mise à l'échelle proportionnellement aux niveaux de profondeur plus profonds. Cela peut aider à maintenir la qualité aux résolutions inférieures (par défaut : False) | BOOLEAN | Oui | True / False |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l'optimisation HyperTile appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/fr.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
