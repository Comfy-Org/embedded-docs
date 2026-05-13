> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/fr.md)

Le nœud EmptyMochiLatentVideo crée un tenseur latent vidéo vide avec des dimensions spécifiées. Il génère une représentation latente remplie de zéros pouvant servir de point de départ pour des workflows de génération vidéo. Ce nœud permet de définir la largeur, la hauteur, la longueur et la taille du lot pour le tenseur latent vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `largeur` | INT | Oui | 16 à MAX_RESOLUTION | La largeur de la vidéo latente en pixels (par défaut : 848, doit être divisible par 16) |
| `hauteur` | INT | Oui | 16 à MAX_RESOLUTION | La hauteur de la vidéo latente en pixels (par défaut : 480, doit être divisible par 16) |
| `longueur` | INT | Oui | 7 à MAX_RESOLUTION | Le nombre d'images dans la vidéo latente (par défaut : 25, doit être divisible par 6 après soustraction de 1) |
| `taille_du_lot` | INT | Non | 1 à 4096 | Le nombre de vidéos latentes à générer dans un lot (par défaut : 1) |

**Remarque :** Les dimensions latentes réelles sont calculées comme largeur/8 et hauteur/8, et la dimension temporelle est calculée comme ((longueur - 1) // 6) + 1. Le paramètre `length` doit satisfaire la condition que `(length - 1)` soit divisible par 6, ce qui signifie que les valeurs valides sont 7, 13, 19, 25, etc.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `samples` | LATENT | Un tenseur latent vidéo vide avec les dimensions spécifiées, contenant uniquement des zéros |

---
**Source fingerprint (SHA-256):** `6876a739355b2dcde42f8c02eb67405678798b818865ec1a73e19076b738554b`
