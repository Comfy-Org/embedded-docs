> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/fr.md)

Le nœud Shuffle Dataset prend une liste d'images et modifie aléatoirement leur ordre. Il utilise une valeur de `seed` pour contrôler le caractère aléatoire, garantissant que le même ordre de mélange peut être reproduit. Cela est utile pour randomiser la séquence des images dans un ensemble de données avant le traitement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | - | La liste d'images à mélanger. |
| `seed` | INT | Non | 0 à 18446744073709551615 | Graine aléatoire. Une valeur de 0 produira un mélange différent à chaque fois. (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `images` | IMAGE | La même liste d'images, mais dans un ordre nouvellement mélangé de manière aléatoire. |

---
**Source fingerprint (SHA-256):** `0b8442029995bdcedf1df0cb8d27d87aa529fb1021d911ed3016a6a7e788b246`
