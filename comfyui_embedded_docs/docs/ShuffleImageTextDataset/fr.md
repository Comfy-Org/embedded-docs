Ce nœud mélange une liste d'images et une liste de textes ensemble, tout en conservant leurs appariements intacts. Il utilise une graine aléatoire pour déterminer l'ordre de mélange, garantissant que les mêmes listes d'entrée seront mélangées de la même manière à chaque réutilisation de la graine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Liste d'images à mélanger. | IMAGE | Oui | - |
| `texts` | Liste de textes à mélanger. | STRING | Oui | - |
| `seed` | Graine aléatoire. L'ordre de mélange est déterminé par cette valeur (par défaut : 0). | INT | Non | 0 à 18446744073709551615 |

**Remarque :** Les entrées `images` et `texts` doivent être des listes de même longueur. Le nœud appariera la première image avec le premier texte, la deuxième image avec le deuxième texte, et ainsi de suite, avant de mélanger ces paires ensemble.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | La liste mélangée d'images. | IMAGE |
| `texts` | La liste mélangée de textes, conservant leurs appariements d'origine avec les images. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/fr.md)

---
**Source fingerprint (SHA-256):** `c87cef780c98b1cf2a58a7d5faf4399c85edd647a9fdba693d008152e43d9c99`
