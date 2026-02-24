> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/fr.md)

Ce nœud mélange une liste d'images et une liste de textes ensemble, en préservant leurs associations. Il utilise une graine aléatoire pour déterminer l'ordre du mélange, garantissant que les mêmes listes d'entrée seront mélangées de la même manière à chaque fois que la graine est réutilisée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | - | Liste des images à mélanger. |
| `texts` | STRING | Oui | - | Liste des textes à mélanger. |
| `seed` | INT | Non | 0 à 18446744073709551615 | Graine aléatoire. L'ordre du mélange est déterminé par cette valeur (par défaut : 0). |

**Note :** Les entrées `images` et `texts` doivent être des listes de même longueur. Le nœud associera la première image avec le premier texte, la deuxième image avec le deuxième texte, et ainsi de suite, avant de mélanger ces paires ensemble.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `images` | IMAGE | La liste mélangée des images. |
| `texts` | STRING | La liste mélangée des textes, conservant leurs associations originales avec les images. |
