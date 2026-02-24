> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/fr.md)

Le nœud Shuffle Dataset prend une liste d'images et modifie aléatoirement leur ordre. Il utilise une valeur de graine (`seed`) pour contrôler l'aléatoire, garantissant que le même ordre de mélange puisse être reproduit. Ceci est utile pour randomiser la séquence d'images dans un jeu de données avant leur traitement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | - | La liste d'images à mélanger. |
| `seed` | INT | Non | 0 à 18446744073709551615 | Graine aléatoire. Une valeur de 0 produira un mélange différent à chaque exécution. (par défaut : 0) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `images` | IMAGE | La même liste d'images, mais dans un nouvel ordre aléatoire. |
